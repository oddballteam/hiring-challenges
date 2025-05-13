## Automated Testing for a Public Website

**Description:**

You are tasked with writing automated tests for the **search functionality** on the **Wikipedia** website's main page (www.wikipedia.org). This assessment aims to evaluate your ability to:

- Write clean, maintainable, and efficient test code.
- Utilize a test automation framework effectively.
- Identify and handle various web elements.
- Apply best practices for test design, including minimizing flakiness.

**Instructions:**

1.  **Select a Test Automation Framework:**

    - Choose a test automation framework that you are proficient in. Common choices include:
      - Selenium WebDriver
      - Playwright
      - Cypress
      - Puppeteer
    - Clearly state the framework you have chosen in your README.

2.  **Define Test Scenarios:**

    - Implement the following test scenario:

      1.  **Homepage Search:**

          - Open the Wikipedia homepage (www.wikipedia.org).
          - Enter a search term (e.g., "Software testing") in the search input field.
          - Submit the search query (e.g., by pressing Enter or clicking the search button).
          - Validate that the search results page loads successfully. This could involve checking for a specific element on the results page, such as the presence of search result entries or a heading.
          - Click the first link in the search results.
          - Validate that the page for the term you searched for loads successfully. This could involve checking the page title or a key element on that page.

    - Implement **at least two** additional test scenarios. These scenarios should cover other aspects of the Wikipedia search functionality or related elements on the homepage, and demonstrate your ability to handle various UI elements and interactions. Here are a couple of examples:

      - **Check for search suggestions:** Verify that search suggestions appear as the user types in the search box.
      - **Test different search terms:** Use a search term that should yield no results.

    - For each scenario, provide the following in your code and/or README:

      - A clear description of the test case.
      - The steps involved in the test.
      - The expected outcome.

3.  **Code Implementation:**

    - Write the automated tests using your chosen framework.
    - Focus on writing clean, well-structured, and maintainable code.
    - Use appropriate selectors to locate web elements. Prioritize robust selectors (e.g., using a combination of attributes, avoiding fragile CSS selectors) to minimize test flakiness.
    - Implement proper waiting mechanisms to handle asynchronous operations and dynamic content.
    - Include comments in your code to explain the purpose of each test and the logic behind your implementation.

4.  **Test Execution and Reporting:**

    - Include instructions in your README on how to set up and run your tests.
    - If your chosen framework provides test reporting features, demonstrate how to generate and interpret the test results.

5.  **Flakiness Considerations:**

    - In your README, discuss the strategies you have employed to minimize test flakiness. This is a critical aspect of test automation. Explain your approach to:
      - Selecting robust locators.
      - Handling asynchronous operations.
      - Managing test data.
      - Any other techniques you used to ensure test stability.

**Deliverables:**

- A README file with a description, which automation framework you chose, and instructions on how to set up and run the tests.
- All the code for your automated tests.

---

## Preparing for the Interview

**[Next Steps...](../../next-steps.md)**
