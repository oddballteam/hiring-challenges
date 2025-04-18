# Address Book

## Overview

Create a RESTful API, using industry-recognized standards and best practices. You may build the API in any well-established backend language and library of your choice.

The API should allow clients to view, search, and edit the contact database. You will utilize a SQLite database; your application's build process should install any needed libraries to query it.

---

## Details

### Endpoints

Create endpoints that do each of the following things. You should decide appropriate naming and methods.

- List all contacts, with options for pagination and sorting.
- View details for a specific contact.
- Edit a contact.
- Search contacts by name or other fields.

### Database

The file [oddballs.db](oddballs.db) contains the data. It has a single table called `oddballs` with these columns:

- id
- firstName
- lastName
- street
- city
- state
- zip
- phone
- email

### Documentation/API Client

You do not need to create a front end. Optionally, you can create tests or Postman/Bruno collections to show your API's operation. As an alternative, at least provide some documentation in a README so we know how to make requests.

---

## Submission

We encourage you not to spend more than a few hours in completing this project. We are not necessarily looking for a production ready application. The goal is to get a feel for how you think and set up a great conversation.

Please submit the project at least 4 hours before your scheduled interview. This will allow us time to preview it before the interview.

### 1. GitHub Repository

- Create a **public GitHub repository** to submit your solution. The repository should contain the full implementation, including any required files (HTML, CSS, JavaScript, etc.) to build and run the web application.
- The repository must include:
  - A **clear, concise README** with the following:
    - Description of the project.
    - How to build and run it locally.
    - Any other details that would help us understand your implementation (e.g., architectural decisions, libraries used, etc.).
  - **Code Comments**: Ensure your code is well-commented to explain key sections of your logic, especially any complex or non-obvious parts.

### 2. Deployment (optional)

- Host your project on a service like Netlify, Vercel, Supabase, Cloudflare, GitHub Pages, or similar hosting options.
- Provide a link to the live project in your README file.

---

## Interview

During the interview itself, we'll ask you to give a demo of the application and walk through your technical implementation. We'll discuss your design decisions, challenges you faced, possible enhancements, etc.
