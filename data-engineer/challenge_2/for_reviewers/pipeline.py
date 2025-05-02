import pandas as pd
from datetime import datetime
import pytz
from pathlib import Path
import logging
import os
import argparse
import json
from typing import List, Optional, Dict

# Set up logging
log_dir = Path("for_reviewers")
log_dir.mkdir(exist_ok=True, parents=True)
log_file = log_dir / "pipeline.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class DataProcessor:
    def __init__(self, data_dir: str):
        # Use absolute path for data directory
        self.data_dir = Path(os.path.abspath(data_dir))
        self.initial_dir = self.data_dir / "initial"
        self.delta_dir = self.data_dir / "delta"

        # Initialize processed files tracking
        self.processed_files_file = log_dir / "processed_files.json"
        self.processed_files = self._load_processed_files()

        # Log directory paths for debugging
        logger.info(f"Data directory: {self.data_dir}")
        logger.info(f"Initial directory: {self.initial_dir}")
        logger.info(f"Delta directory: {self.delta_dir}")
        logger.info(f"Log file: {log_file}")
        logger.info(f"Processed files log: {self.processed_files_file}")

    def _load_processed_files(self) -> set:
        """Load the list of previously processed files"""
        if self.processed_files_file.exists():
            try:
                with open(self.processed_files_file, 'r') as f:
                    return set(json.load(f))
            except json.JSONDecodeError:
                logger.warning(
                    "Error reading processed files log, starting fresh")
                return set()
        return set()

    def _save_processed_files(self):
        """Save the list of processed files"""
        self.processed_files_file.parent.mkdir(exist_ok=True, parents=True)
        with open(self.processed_files_file, 'w') as f:
            json.dump(list(self.processed_files), f)

    def get_available_months(self) -> List[str]:
        """Get all available months from delta files"""
        months = set()
        for file in self.delta_dir.glob("*_delta_*.csv"):
            month = file.stem.split('_delta_')[1]
            months.add(month)
        return sorted(list(months))

    def load_initial_data(self) -> Dict[str, pd.DataFrame]:
        """Load initial dimension and fact tables"""
        logger.info("Loading initial data...")
        tables = {}
        for file in self.initial_dir.glob("*.csv"):
            table_name = file.stem
            # Handle the renamed file
            if table_name == 'call_centers':
                logger.warning(
                    "Found 'call_centers.csv', expected 'contact_centers.csv'. Renaming key.")
                table_name = 'contact_centers'  # Use the new name internally

            tables[table_name] = pd.read_csv(file)
            logger.info(
                f"Loaded {table_name} with {len(tables[table_name])} records")
        # Ensure contact_centers key exists if file wasn't found but expected
        if 'contact_centers' not in tables and (self.initial_dir / "contact_centers.csv").exists():
            tables['contact_centers'] = pd.read_csv(
                self.initial_dir / "contact_centers.csv")
            logger.info(
                f"Loaded contact_centers with {len(tables['contact_centers'])} records")
        elif 'contact_centers' not in tables:
            logger.error("Could not load initial contact_centers data.")
            # Optionally raise an error or return an empty DataFrame
            tables['contact_centers'] = pd.DataFrame()

        return tables

    def process_delta(self, current_state: Dict[str, pd.DataFrame], month: str):
        """Process delta files for a given month"""
        logger.info(f"Processing delta files for {month}...")
        delta_files = list(self.delta_dir.glob(f"*_delta_{month}.csv"))

        for file in delta_files:
            # Use absolute path for consistency
            abs_file_path = str(file.absolute())
            if abs_file_path in self.processed_files:
                logger.info(f"Skipping already processed file: {file}")
                continue

            # Handle renamed file
            table_name = file.stem.split('_delta_')[0]
            if table_name == 'call_centers':
                table_name = 'contact_centers'  # Adjust internally

            delta_df = pd.read_csv(file)
            delta_df['action'] = delta_df['action'].str.strip()
            logger.info(
                f"Processing {table_name} delta file with columns: {delta_df.columns.tolist()}")
            logger.info(f"Current state of {table_name} before update:")
            logger.info(current_state[table_name])

            if table_name not in current_state:
                logger.warning(
                    f"Table {table_name} not found in current state, skipping delta processing.")
                # Mark file as processed even if skipped to avoid reprocessing attempts
                self.processed_files.add(abs_file_path)
                self._save_processed_files()
                continue

            # Process each action type
            for action in delta_df['action'].unique():
                action_df = delta_df[delta_df['action'] == action]
                logger.info(
                    f"Processing {len(action_df)} {action} records for {table_name}")
                logger.info(f"Action data:")
                logger.info(action_df)

                if action == 'add':
                    # Rename columns in delta if needed before concat
                    if table_name == 'contact_centers' and 'center_id' in action_df.columns:
                        action_df = action_df.rename(
                            columns={'center_id': 'contact_center_id', 'center_name': 'contact_center_name'})
                    elif table_name == 'agents' and 'center_id' in action_df.columns:
                        action_df = action_df.rename(
                            columns={'center_id': 'contact_center_id'})

                    current_state[table_name] = pd.concat(
                        [current_state[table_name], action_df.drop('action', axis=1)], ignore_index=True)
                elif action == 'update':
                    # Determine the ID column based on table name
                    id_column = {
                        'interactions': 'interaction_id',
                        'agents': 'agent_id',
                        'contact_centers': 'contact_center_id',  # Updated
                        'service_categories': 'category_id'
                    }.get(table_name)

                    if not id_column:
                        logger.warning(
                            f"Unknown table {table_name}, skipping updates")
                        continue

                    # Ensure delta columns match the state columns
                    delta_cols_renamed = action_df.copy()
                    if table_name == 'contact_centers':
                        delta_cols_renamed = delta_cols_renamed.rename(
                            columns={'center_id': 'contact_center_id', 'center_name': 'contact_center_name'})
                    elif table_name == 'agents' and 'center_id' in delta_cols_renamed.columns:
                        delta_cols_renamed = delta_cols_renamed.rename(
                            columns={'center_id': 'contact_center_id'})

                    for _, row in delta_cols_renamed.iterrows():
                        record_id = row[id_column]
                        logger.info(
                            f"Replacing {table_name} record with {id_column} = {record_id}")
                        # Remove old record(s)
                        current_state[table_name] = current_state[table_name][current_state[table_name]
                                                                              [id_column] != record_id]
                        # Insert new record (drop action column)
                        new_row = row.drop('action')
                        # Convert to DataFrame and append
                        current_state[table_name] = pd.concat([
                            current_state[table_name],
                            pd.DataFrame([new_row])
                        ], ignore_index=True)
                elif action == 'delete':
                    # Determine the ID column based on table name
                    id_column = {
                        'interactions': 'interaction_id',
                        'agents': 'agent_id',
                        'contact_centers': 'contact_center_id',  # Updated
                        'service_categories': 'category_id'
                    }.get(table_name)

                    if not id_column:
                        logger.warning(
                            f"Unknown table {table_name}, skipping deletes")
                        continue

                    # Ensure the correct ID column from delta is used for deletion
                    delta_id_col = id_column  # Default to the state's ID column
                    if table_name == 'contact_centers' and 'center_id' in action_df.columns:
                        delta_id_col = 'center_id'
                    # No specific handling needed for agents delete ID column,
                    # as the primary key is agent_id, not center_id.

                    ids_to_delete = action_df[delta_id_col].tolist()

                    logger.info(
                        f"Deleting {len(ids_to_delete)} records from {table_name} using state column '{id_column}' based on delta column '{delta_id_col}' values: {ids_to_delete}")

                    current_state[table_name] = current_state[table_name][~current_state[table_name][id_column].isin(
                        ids_to_delete)]

            logger.info(f"Current state of {table_name} after all updates:")
            logger.info(current_state[table_name])

            # Mark file as processed using absolute path
            self.processed_files.add(abs_file_path)
            self._save_processed_files()  # Save after each file is processed
            logger.info(f"Processed {len(delta_df)} records for {table_name}")

    def save_current_state(self, current_state: Dict[str, pd.DataFrame], output_dir: Path):
        """Save the current state of all tables"""
        output_dir.mkdir(exist_ok=True, parents=True)
        for table_name, df in current_state.items():
            # Save interactions as UTC, do not add month or convert timezone
            df.to_csv(output_dir / f"{table_name}_final.csv", index=False)
            logger.info(
                f"Saved final state of {table_name} to {output_dir / f'{table_name}_final.csv'}")

    def run_pipeline(self, months: Optional[List[str]] = None) -> Dict[str, pd.DataFrame]:
        """Run the complete data pipeline and return the current state"""
        # Load initial data
        current_state = self.load_initial_data()

        # Process deltas chronologically
        if months is None:
            months = self.get_available_months()
            logger.info(f"Processing all available months: {months}")
        else:
            logger.info(f"Processing specified months: {months}")

        for month in months:
            self.process_delta(current_state, month)

        # Save processed files log
        self._save_processed_files()

        # Save final state
        output_dir = log_dir / "output"
        self.save_current_state(current_state, output_dir)

        logger.info("Pipeline completed successfully")
        return current_state


def parse_args():
    parser = argparse.ArgumentParser(
        description='Process customer support interaction data')
    parser.add_argument(
        '--months', type=str, help='Comma-separated list of months to process (e.g., 202502,202503). If not provided, all available months will be processed.')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    months = args.months.split(',') if args.months else None

    # Use absolute path to data directory
    data_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "..", "data")
    processor = DataProcessor(data_dir)
    current_state = processor.run_pipeline(months)
