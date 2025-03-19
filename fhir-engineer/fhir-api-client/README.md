# Create a FHIR API Client

## Overview

The goal of this challenge is to evaluate your understanding of the FHIR standard and your ability to interact with a FHIR-compliant API. You will demonstrate your ability to **create**, **query**, and **manipulate** healthcare data in FHIR format using the **Test FHIR Server** at [https://hapi.fhir.org/baseR4]. This mock API does not require authentication.

We do not prescribe a certain technology here. The client may be created in the technology of your choice, whether that is a web page, command line application (like Python), a native application, or even test suite.

## Problem Statement

You need to implement the following tasks using the FHIR API:

### 1. Create a Patient Resource

- Use the FHIR API to create a new **Patient** resource by submitting relevant patient data. Include fields such as the patient's name, gender, birth date, and address.
- Ensure that you **follow the FHIR data structure and schema carefully**. You will receive the patient’s **ID** upon successful creation.

### 2. Query Patient Resource

- After successfully creating the patient, use their **patient ID** to query the FHIR API and retrieve the newly created **Patient** resource.
- Ensure you extract the relevant details such as name, gender, and birthdate from the returned data.

### 3. Create an Observation Resource

- Create an **Observation** resource (e.g., a blood pressure reading) associated with the patient you just created.
- The observation should include:
  - The **code** for the observation (e.g., "Blood Pressure"),
  - The **value** of the observation (e.g., 120 mmHg),
  - The **effective date and time** of the observation.
- **Make sure the structure of the Observation resource complies with the FHIR format**, referencing the **Patient** resource you created earlier.

### 4. Update the Patient's Data

- Update the **Patient** resource by modifying a single field such as the address or birthdate. Submit the updated information and ensure the FHIR API properly accepts your update.

### 5. Search for Observations by Patient ID

- Query the **Observation** resources for the patient using their **ID**. You should retrieve a list of observations associated with that patient.
- **Pay attention to the structure of the FHIR search query and the returned results**.

### 6. Handle Errors and Edge Cases

- Ensure you handle edge cases such as when a patient is not found, when required fields are missing, or when the API returns an error (e.g., HTTP status codes like `404` or `400`).
- Handle these responses gracefully and report any issues appropriately.

## Expected Deliverables

1. **Code Repository**:
   - Provide a link to your solution in a public GitHub repository.
   - Include a README file explaining how to run your solution and any dependencies you used.

2. **Solution Demonstration**:

   - Ensure your solution interacts correctly with the FHIR API by creating, querying, updating, and searching resources.
   - Document how to interact with the solution (e.g., "run the Python script" or "execute the command in terminal").

3. **Clean Code and Documentation**:

   - Demonstrate clear, readable, and well-commented code. Explain the important parts of your codebase in the README file.

## Evaluation Criteria

- **Correctness**: Does the solution properly interact with the FHIR API and return the correct results based on the request structure?
- **Code Quality**: Is the code clean, readable, and well-organized with clear documentation?
- **FHIR Data Structure**: Does the solution properly format data in FHIR-compliant JSON format for all resources (Patient, Observation)?
- **Error Handling**: Does the solution handle errors effectively and return appropriate feedback?
- **Efficiency**: How efficient is the solution in terms of making API calls and handling responses?

## Optional Enhancements

- Implement **pagination** for querying observations, as the number of results could be large.
- Add **authentication** (e.g., OAuth2) to ensure secure API interactions.
- Write **unit tests** for the interactions with the FHIR API and data handling.

## Resources

- **FHIR Specification**: [FHIR Official Documentation](https://www.hl7.org/fhir/)
- **HAPI FHIR Test Server**: [https://hapi.fhir.org/baseR4](https://hapi.fhir.org/baseR4)
