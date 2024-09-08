## Book API

### Endpoints:
- **GET /books/**: List all books.
- **GET /books/<id>/**: Retrieve a specific book.
- **POST /books/create/**: Create a new book (authenticated users only).
- **PUT /books/<id>/update/**: Update a book (authenticated users only).
- **DELETE /books/<id>/delete/**: Delete a book (authenticated users only).

### Permissions:
- Only authenticated users can create, update, or delete books.
