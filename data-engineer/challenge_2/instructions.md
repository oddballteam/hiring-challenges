# Customer Support Interaction Data Engineering Challenge

## Scenario

You are working with a national organization's customer support department. They want to analyze their operations performance using data from various support channels, primarily focusing on insights relevant to their **US Eastern Standard Time (EST) business hours**.

The analytics team receives monthly, system-generated data dumps that require processing and cleaning before analysis.

Your task is to build a pipeline to ingest and process this data, creating a clean, structured data store suitable for analysis, and then use that data to answer key business questions.
___
## Requirements

You are provided with an extract of the data as of the end of January 2025 and subsequent monthly delta files for February and March 2025.

1.  **Data Integration:**
    *   The initial dimension data (`agents.csv`, `contact_centers.csv`, `service_categories.csv`) and fact data (`interactions.csv`) are in the `data/initial/` directory.
    *   Monthly changes (additions, updates, deletions) for all tables are in the `data/delta/` directory (e.g., `agents_delta_202502.csv`, `interactions_delta_202502.csv`), indicated by an `action` column.
    *   Process the data chronologically (Jan initial -> Feb delta -> Mar delta) to arrive at the final state of agents, contact centers, and service categories as of the end of March 2025.
    *   Process all tables similarly. Records can be updated or deleted based on their respective ID columns (`interaction_id`, `agent_id`, `contact_center_id`, `category_id`) in the delta files. The goal is to have the most current state for each record.

2.  **Data Storage:** Persist the final state of the dimension tables and the complete, cleaned interaction fact table in a data store of your choice (e.g., database tables, csv saved to disk). The data should be structured to facilitate analysis.

3.  **Output Report:** Create a report named `support_report.csv` containing the **count** of `interactions` and `phone calls` as well as the **total sum** of `call duration`, broken down by `month`, `contact center`, and `department`. It should have the following columns:

    *   `month`
    *   `contact_center_name`
    *   `department`
    *   `total_interactions`
    *   `total_calls`
    *   `total_call_duration`
<br> 

4.  **Analysis & Reporting:** Using the final processed data (and potentially your generated report), answer the following business questions. Provide brief written answers supported by your data.
    *   What were the total number of interactions handled by each contact center in Q1 2025?
    *   Which month (Jan, Feb, or Mar) had the highest total interaction volume?
    *   Which contact center had the longest average phone call duration (`total_call_duration`)? 
        - Why might this be the case based on the data? 
        - What approach would you recommend to measure agent work time more accurately?
___

## Constraints

*   All system-generated timestamps in the data are in UTC format.
*   Some dimensions may be deleted in the delta files. Your analysis should handle any missing values that reference deleted categories by replacing them with `Unknown`.

## Bonus Features (Optional)

While the core focus is on the data processing logic and answering the business questions, consider implementing these optional features if time permits:

*   **Configurable Output Format:** Implement a command-line interface (e.g., using `argparse` in Python) allowing the user to specify the output format for the `support_report` file. Support `csv` (default), `json`, and `parquet` formats.
*   **Logging:** Add logging (e.g., using Python's `logging` module) to track the pipeline's progress and potential issues.
*   **Testing/Validation:** Include basic tests or data validation steps to ensure pipeline correctness.
*   **Incremental Processing:**
    *   Implement command-line arguments to specify which months to process (e.g., `--months 202502,202503`)
    *   If no months are specified, automatically detect and process all available delta files
    *   Track processed files to avoid reprocessing the same data
    *   Example usage:
        ```bash
        # Process specific months
        python pipeline.py --months 202502,202503
        
        # Process all available months
        python pipeline.py
        ``` 