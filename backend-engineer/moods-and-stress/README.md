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

## Preparing for the Interview

**[Next Steps...](../../next-steps-real-time.md)**
