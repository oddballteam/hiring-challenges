# Data Transformation Pipeline

Your task is to build a data pipeline that ingests, processes, and aggregates the provided datasets. The pipeline should support exporting the processed data in a format specified by the user (e.g., CSV, Parquet, or JSON).

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

3. **Transformations & Aggregations:**  

   Create the following aggregated views/tables:
   - **Customer Summary:** For each customer, calculate:
     - Total number of transactions.
     - Total amount spent.
     - Average transaction value.
   - **Product Summary:** For each product, calculate:
     - Total units sold.
     - Total revenue generated.
   - **Daily Transactions:** Calculate:
     - Total transactions and revenue for each day.

4. **Exporting:**  
   - Implement a command-line interface (CLI) to run the pipeline.
   - Allow the user to specify the output format (CSV, Parquet, or JSON).
   - Save the outputs into separate files for each aggregated view.

5. **Documentation:**  
   - Write a `README` explaining:
     - How to set up and run the project.
     - Assumptions made during development.
     - Description of each aggregated view.

---

## Submission

We encourage you not to spend more than a few hours in completing this project. We are not necessarily looking for a production ready application. The goal is to get a feel for how you think and set up a great conversation.

Please submit the project at least 4 hours before your scheduled interview. This will allow us time to preview it before the interview.

### GitHub Repository

- Create a **public GitHub repository** to submit your solution. The repository should contain the full implementation, including any required files (HTML, CSS, JavaScript, etc.) to build and run the web application.
- The repository must include:
  - A **clear, concise README** with the following:
    - Description of the project.
    - How to build and run it locally.
    - Any other details that would help us understand your implementation (e.g., architectural decisions, libraries used, etc.).
  - **Code Comments**: Ensure your code is well-commented to explain key sections of your logic, especially any complex or non-obvious parts.
