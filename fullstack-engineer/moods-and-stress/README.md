# Moods and Stresses

![Mood Scale](moods.png)

As a health care provider, we are concerned with the moods and stress levels of our patients. We want to examine our data to determine who is likely not doing well based on our readings.

## Data Dictionary

### Users

The [users.csv](users.csv) file contains a list of users with `user_name` and `full_name` fields. 

### Moods

In the [moods.csv](moods.csv) file, we have a daily log of each user's mood. The `mood` column evaluates them between 1 (very bad) and 5 (great). If a user's value is missing on a given day, we should default to a 3 (neutral).

### Stress

the [stess.csv](stress.csv) file similarly contains a daily log of the person's stress level. A value of 1 indicates low stress, while a value of 5 indicates very stressed.

## Product Requirements

Read in the three data files, creating a user interface showing a dashboard with the following:

- All users who had two or more bad days in the week beginning 2017-05-07, displaying their username and the number of bad days that week. The list should be ordered descending by number of bad days.
- Show the 5 longest streaks of consecutive bad days across the entire dataset. It should display the username and their consecutive bad day stream, ordered descending by length of streak.

A "bad day" is defined as a user's mood being in the 1-2 range or where their mood is a 3 and stress level is in the 4-5 range.

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
