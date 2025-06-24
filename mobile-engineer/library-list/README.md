# Library App


## Overview

The goal of this challenge is to create an application that displays a search box, list of books, and details about a selected book.

Candidates will be assessed on their ability to integrate with an API, manage local storage, create a responsive UI, and handle errors gracefully.

---

## Requirements

### 1. **API Integration**

- Fetch data from the OpenLibrary API. The documentation can be found [here](https://openlibrary.org/dev/docs/api).
- Integrate the Book Search API - make sure to use `&fields=*` in your query to fetch all available information.
- **Caching**: Store the retrieved data locally to prevent repeated API calls for the same information.
- **Error Handling**: Ensure proper error handling to manage issues such as failed API calls, rate limits, or connectivity problems.

### 2. **Book Search**

- **Search**: The first screen of the app should have the application's name at the top, a search text bar vertically centered, and a search button below that.

### 3. **Book List**

- **List**: Display the returned results from OpenLibrary in a list; the list should display the book title in bolded text, and below it, the author of the book and the date it was published. Tapping a book in the list should navigate the user to the Book Detail screen.

### 4. **Book Detail**

- **Detail**: Display the details of the book returned from OpenLibrary. Render the book cover (if available) as the hero image of the screen, along with the pertinent available details of the book (title, author, publisher, publishing date, available formats, subjects).

---

## Bonus (Optional)

- **Unit Tests**: Write unit tests for key components of the application (e.g., API requests, carousel functionality, or favorite mechanism).
- **UI Enhancements**: Add animations or transitions to improve the user experience (e.g., smooth scrolling, fade-in effects for images).
- **Advanced Search**: Implement additional functionality, such as favoriting books.
- **Accessibility**: Make the app accessible by adding keyboard navigation, proper color contrast, and screen reader support.
- **Dark Mode**: Implement a dark mode toggle for users who prefer a darker interface.

---

## Evaluation Criteria

### Code Quality

- Is the code clean, modular, and organized?
- Are best practices followed, such as proper naming conventions, file structure, and code reuse?
- Is the code maintainable and scalable?

### UI/UX

- Is the application visually appealing and easy to use?
- Is the layout responsive, ensuring a good experience on desktop, tablet, and mobile devices?
- Does the image carousel or scroll mechanism provide smooth and intuitive navigation?

### Functionality

- Does the app correctly retrieve and display books from OpenLibrary?
- Does the app handle API errors or other issues gracefully (e.g., show a friendly message when the API is down)?

### Creativity

- How creatively have you approached the UI design and user experience?
- Were additional features (such as advanced search, dark mode, or animations) implemented?
- Did you implement the project with a focus on accessibility and usability?

## Preparing for the Interview

By completing this challenge, you will demonstrate your technical ability to work with external APIs, build a responsive and user-friendly frontend, and manage local storage in a real-world scenario. We look forward to seeing your implementation!

**[Next Steps...](../../next-steps-real-time.md)**
