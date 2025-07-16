![Oddball](https://oddball.io/wp-content/uploads/2024/01/Oddball-Logo-High-Res.png)

# Data Science Exploratory Analysis

Your task is to perofrm an exploratory analysis that summarizes the key statistics, and visualizes serveral features of the provided dataset.

---

## Datasets

You are provided with one dataset:

1. **P2-Mispriced-Diamonds:** Contains the pricing details of diamonds.

---

## Requirements

1. **ingestion**

   - Create a Jupyter notebook and ingest the file P2-Mispriced-Diamonds into it.

2. **Discovery:**

   - Explore the data set to determine shape, the feature data types and whether or not there is missing data:

3. **Data Cleaning:**

   - Ensure all columns have consistent data types.
   - Convert any "dirty" data into more native database types such as float, booleans, date, datetime, etc.
   - Handle missing or null values appropriately.
   - Remove duplicate records if any.

4. **Summary Statistics:**
   - Generate summary statistics (mean and standard deviation) for numeric features groupded by the categorical features.
   - Create a stacked bar chart for the categorical features.
5. **Create Exploratory Visualizations:**

   - Plot the quantiles and outliers for each of the categorical values.
   - Remove the price and caret outliers for each category of clarity and save the result to a new dataframe.

6. **Determine Relationships in the filtered Data**

   - Calculate the Correlation between the features in a heatmap.
   - Plot the relationship between price and carat for the various clarities,
   - Note any areas where pricing and carat overlaps between clarities.

7. **Business Questions**
   Using the generated support_report, answer the following:

   - What are the top 3 clarity categories by highest median price?
   - Are there any mean price/caret combinations common between the various clarity categories?

> **For each question above, include markdown in your notebook that explains how you derived your answers.**

9. **Documentation:**
   - Write a `README` explaining:
     - How to set up and run the project.
     - Assumptions made during development.
     - Description of each aggregated view.

---

## Deliverables

- Create a **public GitHub repository** for your solution. The repository should contain the full implementation, including any required files (HTML, CSS, JavaScript, etc.) to build and run the web application.
- The repository must include:
  - A **clear, concise README** with the following:
    - Description of the project.
    - How to build and run it locally.
    - Any other details that would help us understand your implementation (e.g., architectural decisions, libraries used, etc.).
  - **Code Comments**: Ensure your code is well-commented to explain key sections of your logic, especially any complex or non-obvious parts.

---

## Preparing for the Interview

**[Next Steps...](../../next-steps-real-time.md)**
