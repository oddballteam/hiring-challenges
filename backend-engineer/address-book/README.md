# Address Book

## Product Requirements

Using industry best practices, create a RESTful API that allows clients to view and search for contacts. The database backend is SQLite; install any needed libraries to query it.

### Endpoints

Create endpoints that do each of the following things. You should decide appropriate naming and methods.

- List all contacts, with options for pagination and sorting.
- View details for a specific contact.
- Edit a contact.
- Search contacts by name or other fields.

## Database

The file [oddballs.db] contains the data. It has a single table called `oddballs` with these columns:

- id
- firstName
- lastName
- street
- city
- state
- zip
- phone
- email