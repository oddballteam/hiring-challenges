
# User Mapping

## Overview
The goal is to create a mobile app that utilizes a **User Service** that calls this endpoint to display a list of users and their coordinates on a map. Candidates will be assessed on their ability to integrate with an API, manage local storage, create a responsive UI, and handle errors gracefully.


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
  - **Architecture**: Describe your rationale for the architecture you chose, i.e.,  MVVM vs BloC, SOLID principles, maintainability, extensibility, and testability.
  - **Limitations and Assumptions**: Discuss any challenges you encountered parsing or modeling the data, choosing and implementing an architecture, or creating a UI
  - **Further Exploration**: Identify any potential areas for improvement in design, UI, testability, security, or features that may have been considered, yet not implemented due to time constraints.

## Bonus (Optional)

- **Unit Tests**: Write unit tests for key components of the application (e.g., API requests, carousel functionality, or favorite mechanism).
- **UI Enhancements**: Add animations or transitions to improve the user experience (e.g., smooth scrolling, fade-in effects for images).
- **Advanced Search**: Implement additional functionality, such as favoriting books.
- **Accessibility**: Make the app accessible by adding keyboard navigation, proper color contrast, and screen reader support.
- **Dark Mode**: Implement a dark mode toggle for users who prefer a darker interface.

## Evaluation Criteria
Your submission will be evaluated based on:
- **Technical Implementation**: How well you were able to design and implement a mobile app that successfully consumes the given endpoint to render users and their location in a list and map, respectively.
- **Clarity of Communication**: How clearly and effectively you explain your decision-making process on architecture and building scalable, extensible, and testable apps.
- **Creativity**: How creatively you approach design, from architecture to UI.
### Time Expectation
We expect this assignment to take **no more than 4 hours** to complete. We value **quality** over the quantity of work. Focus on providing a scalable, extensible, and testable app.