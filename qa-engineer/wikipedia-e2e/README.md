# Wikipedia End-to-End Tests

## Description

You are tasked with writing automated tests for the **search functionality** on the **Wikipedia** website's main page (www.wikipedia.org). This assessment aims to evaluate your ability to:

- Write clean, maintainable, and efficient test code.
- Utilize a test automation framework effectively.
- Identify and handle various web elements.
- Apply best practices for test design, including minimizing flakiness.

## Instructions

1.  **Select a Test Automation Framework:**

    - Choose a test automation framework that you are proficient in. Common choices include:
      - Selenium WebDriver
      - Playwright
      - Cypress
      - Puppeteer
    - Clearly state the framework you have chosen in your README.

2.  **Test Scenarios:**

    - Search for term from homepage:

      - Open the Wikipedia homepage (www.wikipedia.org).
      - Enter a search term (e.g., "Software testing") in the search input field.
      - Submit the search query (e.g., by pressing Enter or clicking the search button).
      - Validate that the search results page loads successfully. This could involve checking for a specific element on the results page, such as the presence of search result entries or a heading.
      - Click the first link in the search results.
      - Validate that the page for the term you searched for loads successfully. This could involve checking the page title or a key element on that page.

    - Implement **at least two** additional test scenarios. These scenarios should cover other aspects of the Wikipedia search functionality or other features. This should demonstrate your ability to handle various UI elements and interactions. Here are some ideas:

      - **Check for search suggestions:** Verify that search suggestions appear as the user types in the search box.
      - **Test different search terms:** Use a search term that should yield no results.
      - **Navigate languages:** Use the language links to navigate to the language specific homepages.

3.  **Code Implementation:**

    - Write the automated tests using your chosen framework.
    - Focus on writing clean, well-structured, and maintainable code.
    - Use appropriate selectors to locate web elements, minimizing flakiness and fragility.
    - Implement proper waiting mechanisms to handle asynchronous operations and dynamic content.
    - Include comments in your code to explain the purpose of each test and the logic behind your implementation.

4.  **Test Execution and Reporting:**

    - Include instructions in your README on how to set up and run your tests.
    - If your chosen framework provides test reporting features, demonstrate how to generate and interpret the test results.

---

## Preparing for the Interview

**[Next Steps...](../../next-steps.md)**
