[← Back to all Mobile Engineer Challenges](../README.md)  
[← Back to main index](../../README.md)

# User Mapping

## Overview

Welcome to Oddball’s User Mapping challenge! In this exercise, you'll build a mobile app that displays a list of users and their locations on a map. This challenge is designed to assess your ability to integrate with APIs, manage local storage, create responsive UIs, and handle errors gracefully—all while showcasing your creativity and engineering best practices. We’re excited to see how you approach the problem!

## Background

Here is a free, public API that provides mock user data: https://dummyjson.com/users
The JSON response includes a list of `User`s, each providing a variety of information including contact details, an address, and a linked bank account.

### Data Description

Here is some of the user data returned from the endpoint response:

- **First Name**: User's first name.
- **Last Name**: User's last name.
- **Image**: User's profile picture.
- **Address**: An object containing address data, including coordinates.
- **Bank**: An object containing bank data.
- **Company**: An object containing company data.
- **... More!**: Explore the [endpoint](https://dummyjson.com/users) to better grasp the structure of the response.

## Requirements

1. **Create your Model**:

   - Examine the JSON response from the endpoint, https://dummyjson.com/users, and consider which data is most relevant for displaying a list of users and pinning their coordinates on a map.

2. **Create a User Service**:

   - Implement a User Service that calls the endpoint and returns a list of users.

3. **Determine which Architecture to Implement**:

   - Architect the app with your choice of common mobile architectural principles (MVVM, MVC, BLoC, etc.), and be able to explain your choice and the tradeoffs between them.
   - Keep in mind the pros and cons of each architecture, and how [SOLID principles](https://en.wikipedia.org/wiki/SOLID) and testability apply to your design.

4. **Create a UI**:
   - Create a UI that renders according to the underlying state.
     - A screen that displays a scrollable list of Users.
       - Tapping on a User in the list will present a new screen that accepts a User object and pins their location on a map.
   - Consider which views may qualify for reusable view components, and implement as needed.
   - Consider how your UI may render across various devices, including both small and large screens, on both Android and iOS.

### Deliverables

- **Pre-Interview Submission**: Please submit a **Zipped (Compressed) Project**.
- **During the Interview**: Be prepared to discuss:
  - **Architecture**: Describe your rationale for the architecture you chose, i.e., MVVM vs BloC, SOLID principles, maintainability, extensibility, and testability.
  - **Limitations and Assumptions**: Discuss any challenges you encountered parsing or modeling the data, choosing and implementing an architecture, or creating a UI
  - **Further Exploration**: Identify any potential areas for improvement in design, UI, testability, security, or features that may have been considered, yet not implemented due to time constraints.

## Bonus (Optional)

- **Unit Tests**: Write unit tests for key components of the application (e.g., API requests, user list rendering, map interactions).
- **UI Enhancements**: Add animations or transitions to improve the user experience (e.g., smooth scrolling, fade-in effects for images).
- **Advanced Search/Filtering**: Implement search or filtering for users by name, location, or company.
- **Accessibility**: Make the app accessible by adding proper color contrast, screen reader support, and accessible touch targets.
- **Dark Mode**: Implement a dark mode toggle for users who prefer a darker interface.

## Evaluation Criteria

Your submission will be evaluated based on:

- **Technical Implementation**: How well you were able to design and implement a mobile app that successfully consumes the given endpoint to render users and their location in a list and map, respectively.
- **Clarity of Communication**: How clearly and effectively you explain your decision-making process on architecture and building scalable, extensible, and testable apps.
- **Creativity**: How creatively you approach design, from architecture to UI.
- We value **quality** over the quantity of work. Focus on providing a scalable, extensible, and testable app. If you don't finish in the allotted time, that is okay.

## Preparing for the Interview

By completing this challenge, you’ll show your technical ability to work with external APIs, build a responsive and user-friendly frontend, and manage local storage in a real-world scenario. Most importantly, we hope you have fun and learn something new along the way!

We look forward to seeing your implementation and discussing your approach.

**[Next Steps...](../../next-steps-real-time.md)**

[← Back to all Mobile Engineer Challenges](../README.md)  
[← Back to main index](../../README.md)
