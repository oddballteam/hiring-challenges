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

The `friends` property contains a an array of IDs referencing their friends (within the same dataset). You can keep it in this format or feel free to transform it into another file structure or database engine.

## User Interface

Don't feel like you need to over design it. There should be at least two screens. One to find and select the two individuals. And, the second, to display the matching result of their relationship and mutual friends.

---

## Preparing for the Interview

**[Next Steps...](../../next-steps-real-time.md)**
