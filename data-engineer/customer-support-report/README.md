# Customer Support Interaction Data Engineering Challenge

[Internal Notes](https://drive.google.com/drive/folders/1CpN3WScbUuBpDPKzTv13U-V4OYquszrL?usp=drive_link) _(For reviewer only)_

## Scenario

You are working with a national organization's enterprise operations department. They actively track contact center intake volume using data from various support channels.

Their reporting team receives monthly system-generated delta files that require processing to sync the data. Unfortunately, their analytics pipeline has stopped working and they have reached out to you for assistance.

Your task is to build a new pipeline that will ingest and process these files sequentially to bring the data up to date. Afterward, create a process that aggregates the data into a report and then use the result to answer key business questions.

---

## Data

**Data definitions:**

- Fact file: `interactions.csv`
- Dimension files: `agents.csv`, `contact_centers.csv`, `service_categories.csv`

**Directories:**

- [data/initial/] – _full extract generated end of January 2025_
- [data/delta/] – _delta files generated for February & March 2025_

> The initial and delta file structures are identical, except delta files include an `action` column denoting monthly changes (additions, updates, deletions).

---

## Constraints

- All system-generated timestamps in the data are in UTC format. The contact centers operate in Eastern Standard Time (EST).
- Some dimensions may be deleted in the delta files. Your analysis should handle any missing values that reference deleted categories by replacing them with `Unknown`.

---

## Requirements

### 1. Data Integration

- Process the data chronologically (`Jan initial` → `Feb delta` → `Mar delta`) to arrive at the final state of agents, contact centers, service categories, and interactions as of the end of March 2025.
- Process all tables similarly. Records can be updated or deleted based on their respective ID columns (`interaction_id`, `agent_id`, `contact_center_id`, `category_id`) in the delta files. The goal is to have the most current state for each record.

> **Note:** Persist the final state of the dimension tables and the complete interaction fact table in any format of your choice (e.g., database tables or CSV saved to disk).

---

### 2. Output Report

Create a report named `support_report` containing:

- The **count** of `interactions` and `phone calls`
- The **total sum** of `call duration`
- Grouped by `month`, `contact center`, and `department`

**Columns:**

- `month`
- `contact_center_name`
- `department`
- `total_interactions`
- `total_calls`
- `total_call_duration`

---

### 3. Business Questions

Using the generated `support_report`, answer the following:

1. **What were the total number of interactions handled by each contact center in Q1 2025?**
2. **Which month (Jan, Feb, or Mar) had the highest total interaction volume?**
3. **Which contact center had the longest average phone call duration (`total_call_duration`)?**
    - Why might this be the case based on the interactions data?
    - What approach would you recommend to measure agent work time more accurately?

> **For each question above, include code in your repository that demonstrates how you derived your answer using the files you generated from the data integration and output report steps.**

---

## Bonus Features (Optional)

- **Configurable Output Format:** Support `csv` (default), `json`, and `parquet` formats via command-line arguments.
- **Logging:** Add logging to track the pipeline's progress and potential issues.
- **Testing/Validation:** Include basic tests or data validation steps.
- **Incremental Processing:** Allow specifying months to process (e.g., `--months 202502,202503`). Track processed files to avoid reprocessing.

**Example usage:**

```bash
# Process specific months
python pipeline.py --months 202502,202503

# Process all available months
python pipeline.py
```

---

## Submission Guidelines

1. **You may use any programming language or software** (e.g., Python, R, SQL, Excel, etc.) to complete this challenge.
2. Your submission must include **clear, step-by-step instructions** on how to run your code and reproduce your results from raw data to final answers. If special dependencies or environments are required, please document them.
3. Push your final code, including the data processing pipeline, report generation script, and any supporting files, to a public GitHub repository.
4. Ensure the repository includes a clear `README.md` file.
5. In your `README.md`, provide the direct answers to the three business questions listed above. For each answer, briefly justify how you arrived at it, referencing your generated `support_report` or final processed data where appropriate.

---

## Preparing for the Interview

**[Next Steps...](h../../next-steps.md)**
