# JSONPlaceholder API End-to-End Tests

## Description

You are tasked with writing automated tests for the **JSONPlaceholder** public API (<https://jsonplaceholder.typicode.com/>), specifically focusing on the **/todos** endpoint. This assessment aims to evaluate your ability to:

- Write clean, maintainable, and efficient test code for APIs.
- Utilize an API testing framework/library effectively.
- Understand and interact with different API request methods and response formats (primarily JSON).
- Apply best practices for test design, including data validation and handling different response scenarios.

## Instructions

1. **Select a Testing Tool/Library:**

    - Choose a testing tool or library that you are proficient in. Common choices include:
        - Python with `requests` and `pytest` or `unittest`
        - JavaScript with `axios` and `Mocha` or `Jest`
        - Java with `RestAssured` and `JUnit` or `TestNG`
        - Postman/Newman (if you prefer a UI-based approach, but focus on demonstrating scripting capabilities if possible)
    - Clearly state the testing tool/library you have chosen in your README.

2. **Test Scenarios:**

    - **Retrieve a single Todo:**
        - Send a GET request to retrieve a specific todo item using its ID (e.g., `/todos/1`).
        - Validate the response status code (e.g., 200 OK).
        - Validate the presence of key fields in the response body: `userId`, `id`, `title`, and `completed`.
        - Validate that the `id` in the response matches the ID you requested.
        - Validate the data types of the key fields (e.g., `userId` and `id` are numbers, `title` is a string, `completed` is a boolean).

    - Implement **at least two** additional test scenarios for the `/todos` endpoint. These scenarios should cover other aspects of the API or demonstrate your ability to handle different API interactions. Here are some ideas:

        - **List all Todos:** Send a GET request to retrieve all todo items (`/todos`). Validate the response status code (e.g., 200 OK) and that the response is a non-empty array. Optionally, validate the structure of the first few elements in the array.
        - **Filter Todos by User ID:** Send a GET request to retrieve todos filtered by a `userId` (e.g., `/todos?userId=2`). Validate the response status code (e.g., 200 OK) and that all returned todos have the specified `userId`.
        - **Create a new Todo:** Send a POST request to create a new todo (`/todos`) with a sample request body (e.g., `{ "userId": 1, "title": "Buy groceries", "completed": false }`). Validate the response status code (e.g., 201 Created) and that the response body contains the newly created data, including a generated `id`.
        - **Update an existing Todo:** Send a PUT request to update an existing todo (`/todos/1`) with an updated request body (e.g., `{ "id": 1, "completed": true }`). Validate the response status code (e.g., 200 OK) and that the updated `completed` status is present in the response body.
        - **Handle an invalid Todo ID:** Send a GET request to retrieve a todo with a non-existent ID (e.g., `/todos/9999`). Validate the response status code (e.g., 404 Not Found) or any other appropriate error response.

3. **Code Implementation:**

    - Write the automated tests using your chosen tool/library.
    - Focus on writing clean, well-structured, and maintainable code.
    - Use appropriate methods/functions provided by your chosen tool/library for making HTTP requests (GET, POST, PUT, DELETE) and handling responses.
    - Implement robust validation of the API responses, including status codes, headers (if relevant), and the JSON response body.
    - Consider using data-driven testing if applicable (e.g., testing the creation of posts with different user IDs and content).
    - Include comments in your code to explain the purpose of each test and the logic behind your implementation.

4. **Test Execution and Reporting:**

    - Include instructions in your README on how to set up and run your tests (e.g., installing dependencies, running specific commands).
    - If your chosen tool/library provides test reporting features, demonstrate how to generate and interpret the test results (e.g., outputting test summaries, generating reports in specific formats).

---

## Preparing for the Interview

**[Next Steps...](../../next-steps.md)**
