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

**[Next Steps](../../next-steps.md)**
