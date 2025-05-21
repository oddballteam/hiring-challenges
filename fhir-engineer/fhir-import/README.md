# Challenge: Import and Transform

## Overview: Transform CSV Data to FHIR Resources

In this challenge, you are tasked with transforming healthcare data from multiple CSV files into FHIR-compliant resources. You will be provided with several CSV files containing patient, encounter, and observation data, and your goal is to convert this data into corresponding FHIR **Patient**, **Encounter**, and **Observation** resources.

This can be executed in any way that you like: a webpage, command line interface, or native application. The desired outcome is to convert the date found in the CSVs into valid FHIR JSON format.

This task will evaluate your ability to:

- Parse and transform data from CSV into JSON.
- Map data to FHIR resources, ensuring proper structure and compliance with the FHIR standard.
- Handle common healthcare data transformations and workflows.

## Problem Statement

You are given the following CSV files:

1. **patients.csv**: Contains patient information.
2. **encounters.csv**: Contains encounter details related to the patients.
3. **observations.csv**: Contains observation data for each encounter.

Your task is to perform the following:

### Tasks

1. **Parse the CSV Data**: Write a function to read and parse the CSV files containing the patient, encounter, and observation data.

2. **Create FHIR Patient Resources**: For each row in the **patients.csv**, create a FHIR-compliant **Patient** resource with the following attributes:

   - **Patient ID** (from CSV)
   - **Name** (from CSV: First Name + Last Name)
   - **Gender** (from CSV)
   - **Date of Birth** (from CSV)
   - **Address** (from CSV)

3. **Create FHIR Encounter Resources**: For each row in the **encounters.csv**, create an **Encounter** resource for the patient, including:

   - **Patient Reference**: Reference the appropriate **Patient** resource.
   - **Visit Date** (from CSV)
   - **Encounter Type** (e.g., "Outpatient", "Routine Checkup", based on the encounter data)

4. **Create FHIR Observation Resources**: For each row in the **observations.csv**, create an **Observation** resource for the observation data, including:

   - **Patient Reference**: Reference the appropriate **Patient** resource.
   - **Encounter Reference**: Reference the appropriate **Encounter** resource.
   - **Code**: The type of observation (e.g., "Blood Pressure").
   - **Value**: The value of the observation (e.g., 120/80).
   - **Effective Date/Time**: The date the observation was taken, with the time from each observation row and the date from the corresponding **Visit Date** in the `encounters.csv`.

5. **Return the FHIR Resources**: Once the data is transformed, return a list of FHIR-compliant JSON objects including the relevant references to ensure proper linking. The FHIR resources should be saved as JSON files on the local file system.

6. **Handle Errors**: If there is invalid or missing data in any of the CSV files (e.g., missing required fields), return an error or provide feedback.

### Data Files

You will be provided with the following CSV files:

1. **[patients.csv](patients.csv)**:
   This file contains the patient data. Below is the structure of the CSV:
2. **[encounters.csv](encounters.csv)**:
   This file contains encounter data related to the patients. Below is the structure of the CSV:
3. **[observations.csv](observations.csv)**:
   This file contains observation data for the patients. Below is the structure of the CSV:

### Instructions

1. **Setup**:

   - Use any programming language or framework you are comfortable with to process the CSV data and generate the FHIR JSON data.
   - You may use libraries such as **pandas (Python)** or **csv-parser (JavaScript)** for reading and parsing the CSV data.

2. **FHIR Data Structure**:

   - Familiarize yourself with the **FHIR specification** for Patient, Encounter, and Observation resources. Ensure you generate valid JSON for these resources.

3. **Error Handling**:

   - Handle common errors such as missing or invalid data. Provide clear messages when something is wrong with the input CSV files (e.g., missing "First Name", invalid "Date of Birth").

4. **Deliverables**:

   - Provide a link to your solution as a public GitHub repository.
   - Include a README file explaining how to run your solution and any dependencies you used.
   - Demonstrate the solution through well-organized code with clear comments and documentation.

## Evaluation Criteria

- **Correctness**: Does the solution correctly transform the CSV data into FHIR-compliant JSON resources for Patient, Encounter, and Observation?
- **Code Quality**: Is the code clean, readable, and well-organized with clear documentation?
- **FHIR Data Structure**: Does the solution properly format data in FHIR-compliant JSON format for all resources (Patient, Encounter, Observation)?
- **Error Handling**: Does the solution handle errors effectively and return appropriate feedback when data is missing or malformed?
- **Efficiency**: How efficient is the solution in terms of processing large CSV files and generating the corresponding FHIR resources?

## Optional Enhancements

- Implement support for **multiple observation types** (e.g., adding lab results or vital signs).
- Add **validation** to ensure CSV data is in the correct format before processing.
- Write **unit tests** for the CSV parsing, data transformation, and FHIR resource generation.

## Resources

- **FHIR Specification**: [FHIR Official Documentation](https://www.hl7.org/fhir/)

---

## Preparing for the Interview

**[Next Steps...](../../next-steps-real-time.md)**
