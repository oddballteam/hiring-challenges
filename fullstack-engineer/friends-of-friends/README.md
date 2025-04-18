# Friends of Friends

![Shared Connections](shared-connections.png)

It's a small world, after all! We would like to examine who are the mutual friends, shared between two people. Create a user interface that allows us to select two people from the database. Indicate whether they are friends with each other and list their shared connections.

It should have a browser-based user interface. You can choose any framework of your choice (or none at all).

## Data

You will find the file [friend-list.json](friend-list.json) that contains the data about our list of users and their friends. It is formatted as JSON file with an array of `Friend` objects, in this format:

```typescript
type Friend {
  id: string
  first_name: string
  last_name: string
  email: string
  friends: string[]
}
```

The `friends` property contains a an array of IDs referencing their friends (within the same dataset).  You can keep it in this format or feel free to transform it into another file structure or database engine.

## User Interface

Don't feel like you need to over design it. There should be at least two screens. One to find and select the two individuals. And, the second, to display the matching result of their relationship and mutual friends.

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
