# NASA Astronomy Picture of the Day (APOD) App

![Astronomy Picture of the Day for 1/30/25](M33_1024.jpg)

## Overview

The goal of this challenge is to create an application that displays NASA’s Astronomy Picture of the Day (APOD) for a specified timeframe, allowing users to explore a week’s worth of celestial wonders. The application should feature a responsive, visually appealing interface and support the ability to toggle between different images from the past 7 days.

Candidates will be assessed on their ability to integrate with an API, manage local storage, create a responsive UI, and handle errors gracefully.

---

## Requirements

### 1. **API Integration**

- Fetch data from NASA’s APOD API. The documentation can be found [here](https://api.nasa.gov/). Use `DEMO_KEY` for the API key or register for your own key if you exceed the usage limit.
- Retrieve a list of images and their associated information for a **7-day period**. Display one image per day.
- **Caching**: Store the retrieved data locally to prevent repeated API calls for the same information. This can be done using browser storage (e.g., `localStorage` or `sessionStorage`) or in-memory storage if needed.
- **Error Handling**: Ensure proper error handling to manage issues such as failed API calls, rate limits, or connectivity problems.

### 2. **Image Display**

- **Date Navigation**: Allow users to toggle through dates to view images from the past 7 days relative to a selected date.
- **Carousel or Scrolling**: Implement an efficient scrolling mechanism or carousel to navigate between images.
- **Image Aspect Ratio**: Display each image in a **1:1 aspect ratio**, ensuring the layout looks visually appealing on multiple screen sizes (e.g., desktop, tablet, mobile).
- **Responsive Design**: The app should be fully mobile-friendly and utilize fluid resizing to ensure a seamless experience on various devices. This includes the use of CSS media queries and flexible layout techniques.
- **Best Practices**: Follow best practices for the frontend framework of your choice (e.g., React, Vue, or vanilla JS).

### 3. **Favoriting System**

- **Mark Favorites**: Implement a system that allows users to mark images as favorites. Use in-browser storage (e.g., `localStorage` or `IndexedDB`) to store favorite images so they persist even if the user refreshes the page or revisits the app.
- **View Favorites**: Allow users to access a dedicated page or section where they can view all of their favorited images.
- **Favorite Persistence**: Ensure that favorited images remain in the user’s favorites list even after closing the app or refreshing the page.

---

## Bonus (Optional)

- **Unit Tests**: Write unit tests for key components of the application (e.g., API requests, carousel functionality, or favorite mechanism).
- **UI Enhancements**: Add animations or transitions to improve the user experience (e.g., smooth scrolling, fade-in effects for images).
- **Advanced Search**: Implement additional functionality, such as searching for specific images or exploring pictures based on specific dates (e.g., "show me pictures from March 2024").
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

- Does the app correctly retrieve and display images for the past 7 days from the NASA API?
- Is there a working mechanism for favoriting images, and does it persist across sessions?
- Does the app handle API errors or other issues gracefully (e.g., show a friendly message when the API is down)?

### Creativity

- How creatively have you approached the UI design and user experience?
- Were additional features (such as advanced search, dark mode, or animations) implemented?
- Did you implement the project with a focus on accessibility and usability?

## Preparing for the Interview

By completing this challenge, you will demonstrate your technical ability to work with external APIs, build a responsive and user-friendly frontend, and manage local storage in a real-world scenario. We look forward to seeing your implementation!

**[Next Steps...](../../next-steps-real-time.md)**
