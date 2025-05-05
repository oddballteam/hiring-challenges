# Basic Data Transformation Pipeline

Your task is to build a data pipeline that ingests, processes, and aggregates the provided datasets. The pipeline should support exporting the processed data in a format specified by the user (e.g., CSV, Parquet, or JSON).

You may use whatever language, framework, and dependencies that you choose. Most often it is completed using Python, but you may alternatively use R, JavaScript, etc.

---

## Datasets

You are provided with three datasets:

1. **Transactions Dataset:** Contains details of transactions made by customers.  
   - File: [transactions.csv](transactions.csv)

2. **Customers Dataset:** Contains information about the customers involved in transactions.  
   - File: [customers.csv](customers.csv)

3. **Products Dataset:** Contains details about the products involved in transactions.  
   - File: [products.csv](products.csv)

---

## Requirements

1. **Ingestion:**  
   - Read the datasets into your project from the provided CSV files.

2. **Data Cleaning:**  
   - Ensure all columns have consistent data types.
   - Convert any "dirty" data into more native database types such as float, booleans, date, datetime, etc.
   - Handle missing or null values appropriately.
   - Remove duplicate records if any.
   - Persist the cleaned data.

3. **Transformations & Aggregations:**
   As the next step in the pipeline, process your cleaned data files to generate calculated data marts.
   These aggregated views/tables should be saved as files. Create the following reports:

   - **Customer Summary:** For each customer, calculate:
     - Total number of transactions.
     - Total amount spent.
     - Average transaction value.
   - **Product Summary:** For each product, calculate:
     - Total units sold.
     - Total revenue generated.
   - **Daily Transactions:** Calculate:
     - Total transactions and revenue for each day.

4. **User Interface:**  
   - Implement a command-line interface (CLI) to run the pipeline.
   - Allow the user to specify the output format (CSV, Parquet, or JSON).
   - Save the outputs into separate files for each aggregated view.

5. **Documentation:**  
   - Write a `README` explaining:
     - Any requirements to set up the environment for the demo.
     - How to use the CLI, with example commands.
     - Assumptions made during development.
     - Description of each aggregated view.

---

## Preparing for the Interview

**[Next Steps...](../../next-steps.md)**
