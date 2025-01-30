# Friends

....

## Data

You will find the file [friend-list.json](friend-list.json) that contains the data about our list of users and their friends. It is formated as JSON file with an array of `Friend` objects, in this format:

```typescript
type Friend {
  id: string
  first_name: string
  last_name: string
  email: string
  friends: string[]
}
```

The `friends` property contains a an array of IDs referencing their friends (within the same dataset).

