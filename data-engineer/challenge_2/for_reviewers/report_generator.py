import pandas as pd
import pytz
import logging
from pathlib import Path
from typing import Dict

# Set up logging
log_dir = Path("for_reviewers")
log_dir.mkdir(exist_ok=True, parents=True)
log_file = log_dir / "report_generator.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ReportGenerator:
    def __init__(self, target_timezone: str = 'US/Eastern'):
        """Initialize with the target timezone for conversions."""
        try:
            self.target_tz_info = pytz.timezone(target_timezone)
            # logger.info(f"ReportGenerator initialized with target timezone: {target_timezone}") # Commented out
        except pytz.exceptions.UnknownTimeZoneError:
            # Keep error
            logger.error(
                f"Unknown timezone: {target_timezone}. Defaulting to UTC.")
            self.target_tz_info = pytz.utc

    def convert_to_target_timezone(self, df: pd.DataFrame) -> pd.DataFrame:
        """Convert UTC timestamps to the target timezone and add 'month' column based on target time."""
        # ... (no logger.info here)
        timestamp_cols = ['timestamp', 'interaction_start',
                          'agent_resolution_timestamp', 'interaction_end']
        for col in timestamp_cols:
            if col in df.columns:
                # Convert to datetime if not already
                df[col] = pd.to_datetime(df[col], errors='coerce')
                # If not timezone-aware, localize to UTC
                # Replace deprecated check
                if not isinstance(df[col].dtype, pd.DatetimeTZDtype):
                    df[col] = df[col].dt.tz_localize('UTC')
                # Convert to target timezone
                df[col] = df[col].dt.tz_convert(self.target_tz_info)
        # Add month column based on target timezone timestamp
        if 'timestamp' in df.columns:
            df['month'] = df['timestamp'].dt.strftime('%Y-%m')
        return df

    def generate_support_report(self, current_state: Dict[str, pd.DataFrame]) -> pd.DataFrame:
        """Generate the support report with the three service categories with longest resolution time, grouped by month"""
        # logger.info("Generating support report...") # Commented out

        # Join interactions with dimension tables
        interactions = current_state['interactions']
        contact_centers = current_state['contact_centers']
        service_categories = current_state['service_categories']

        # Convert timestamps to EST only for report generation
        interactions = self.convert_to_target_timezone(interactions)
        # Ensure month column exists (from pipeline)
        if 'month' not in interactions.columns:
            interactions['month'] = interactions['timestamp'].dt.strftime(
                '%Y-%m')

        # Join with dimension tables
        df = interactions.merge(
            contact_centers[['contact_center_id', 'contact_center_name']],
            on='contact_center_id',
            how='left'
        ).merge(
            service_categories[['category_id', 'category_name']],
            on='category_id',
            how='left'
        )

        # Group by month, center, and category
        report = df.groupby(['month', 'contact_center_name', 'category_name']).agg({
            'interaction_id': 'count',
            'call_duration_minutes': ['sum', lambda x: (x > 0).sum()]
        }).reset_index()

        # Rename columns
        report.columns = [
            'month', 'contact_center_name', 'category_name',
            'total_interactions', 'total_call_duration', 'total_calls'
        ]

        # Sort by total_call_duration and get top 3 categories (across all months/centers)
        top_categories = report.groupby('category_name')[
            'total_call_duration'].sum().nlargest(3).index
        report = report[report['category_name'].isin(top_categories)]

        return report

    def analyze_q1_interactions(self, current_state: Dict[str, pd.DataFrame]) -> pd.DataFrame:
        """Analyze total interactions by contact center in Q1 2025"""
        # logger.info("Analyzing Q1 interactions by contact center...") # Commented out

        interactions = current_state['interactions']
        contact_centers = current_state['contact_centers']

        # Convert timestamps to EST for analysis
        interactions = self.convert_to_target_timezone(interactions)

        # Filter for Q1 2025
        q1_start = pd.Timestamp('2025-01-01', tz=self.target_tz_info)
        q1_end = pd.Timestamp('2025-03-31', tz=self.target_tz_info)
        q1_interactions = interactions[
            (interactions['timestamp'] >= q1_start) &
            (interactions['timestamp'] <= q1_end)
        ]

        # Join with contact centers and count interactions
        analysis = q1_interactions.merge(
            contact_centers[['contact_center_id', 'contact_center_name']],
            on='contact_center_id',
            how='left'
        )

        result = analysis.groupby('contact_center_name')[
            'interaction_id'].count().reset_index()
        result.columns = ['contact_center_name', 'total_interactions']

        return result

    def analyze_monthly_volume(self, current_state: Dict[str, pd.DataFrame]) -> pd.DataFrame:
        """Analyze interaction volume by month"""
        # logger.info("Analyzing monthly interaction volume...") # Commented out

        interactions = current_state['interactions']

        # Convert timestamps to EST for analysis
        interactions = self.convert_to_target_timezone(interactions)

        # Extract month and count interactions
        interactions['month'] = interactions['timestamp'].dt.strftime('%Y-%m')
        result = interactions.groupby(
            'month')['interaction_id'].count().reset_index()
        result.columns = ['month', 'total_interactions']

        return result

    def analyze_call_duration(self, current_state: Dict[str, pd.DataFrame]) -> pd.DataFrame:
        """Analyze average call duration by contact center"""
        # logger.info("Analyzing call duration by contact center...") # Commented out

        interactions = current_state['interactions']
        contact_centers = current_state['contact_centers']

        # Convert timestamps to EST for analysis
        interactions = self.convert_to_target_timezone(interactions)

        # Join with contact centers and calculate average duration
        analysis = interactions.merge(
            contact_centers[['contact_center_id', 'contact_center_name']],
            on='contact_center_id',
            how='left'
        )

        result = analysis.groupby('contact_center_name')[
            'call_duration_minutes'].mean().reset_index()
        result.columns = ['contact_center_name', 'average_call_duration']

        return result

    def generate_all_reports(self, current_state: Dict[str, pd.DataFrame], output_dir: Path):
        """Generate support report, analyze other questions, and print answers."""
        output_dir.mkdir(exist_ok=True, parents=True)
        # logger.info("--- Generating Reports and Analysis ---") # Commented out

        # 1. Generate and save support report (as requested)
        support_report = self.generate_support_report(current_state)
        support_report_path = output_dir / "support_report.csv"
        support_report.to_csv(support_report_path, index=False)
        # logger.info(f"Saved support report to {support_report_path}") # Commented out
        print(f"\nReport generated: {support_report_path}")

        # --- Answer Business Questions ---
        print("\n--- Business Question Analysis ---")

        # 2. Q1 Interactions per Contact Center
        # logger.info("Analyzing Q1 interactions...") # Commented out
        q1_analysis = self.analyze_q1_interactions(current_state)
        print("\nQuestion: What were the total number of interactions handled by each contact center in Q1 2025?")
        if not q1_analysis.empty:
            for _, row in q1_analysis.iterrows():
                print(
                    f"- {row['contact_center_name']}: {row['total_interactions']} interactions")
        else:
            print("- No Q1 interaction data found.")
        # REMOVED: q1_analysis.to_csv(output_dir / "q1_interactions.csv", index=False)

        # 3. Month with Highest Interaction Volume
        # logger.info("Analyzing monthly volume...") # Commented out
        monthly_analysis = self.analyze_monthly_volume(current_state)
        print("\nQuestion: Which month (Jan, Feb, or Mar 2025) had the highest total interaction volume?")
        if not monthly_analysis.empty:
            highest_month = monthly_analysis.loc[monthly_analysis['total_interactions'].idxmax(
            )]
            print(
                f"- {highest_month['month']} had the highest volume with {highest_month['total_interactions']} interactions.")
        else:
            print("- No monthly interaction volume data found.")
        # REMOVED: monthly_analysis.to_csv(output_dir / "monthly_volume.csv", index=False)

        # 4. Call Center with Longest Average Call Duration
        # logger.info("Analyzing call duration...") # Commented out
        duration_analysis = self.analyze_call_duration(current_state)
        print("\nQuestion: Which contact center had the longest average phone call duration? Why might this be the case? Recommendations?")
        if not duration_analysis.empty:
            longest_duration_center = duration_analysis.loc[duration_analysis['average_call_duration'].idxmax(
            )]
            print(
                f"- {longest_duration_center['contact_center_name']} had the longest average duration: {longest_duration_center['average_call_duration']:.2f} minutes.")
            print("- Potential reasons: This center might handle more complex interaction types (e.g., technical support, claims) requiring longer calls, or it might have agents needing more training.")
            print("- Recommendation for measurement: Track 'Agent Handle Time' (AHT) which includes call time plus after-call work time for a more accurate picture of effort per interaction, rather than just call duration.")
        else:
            print("- No call duration data found.")
        # REMOVED: duration_analysis.to_csv(output_dir / "call_duration.csv", index=False)

        print("\n--- Analysis Complete ---")

        # Return the main report DataFrame, other results are printed
        return support_report  # Return only the main report df


if __name__ == "__main__":
    # Load final state CSVs from output directory
    output_dir = Path("for_reviewers/output")
    current_state = {
        'agents': pd.read_csv(output_dir / 'agents_final.csv'),
        'contact_centers': pd.read_csv(output_dir / 'contact_centers_final.csv'),
        'interactions': pd.read_csv(output_dir / 'interactions_final.csv'),
        'service_categories': pd.read_csv(output_dir / 'service_categories_final.csv'),
    }
    generator = ReportGenerator()
    generator.generate_all_reports(current_state, output_dir)
    # REMOVED: print("Reports generated in for_reviewers/output/")
