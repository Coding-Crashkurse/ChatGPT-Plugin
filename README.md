# ChatGPT Book Club Plugin - FastAPI API

In this repo you will find a plugin for ChatGPT based on a REST API with FastAPI.

## App Endpoints

The following four endpoints describe the core functionality of the app, typical REST endpoints. where you can add books to a list, update, delete and view them all.

### `POST /books/{username}`

This endpoint adds a book to a user's list. It expects a path parameter `username` and a JSON object in the body containing the book details.

### `GET /books/{username}`

This endpoint returns the list of a user's books. It expects a path parameter `username`.

### `DELETE /books/{username}`

This endpoint deletes a book from a user's list. It expects a path parameter `username` and a body containing the index of the book to be deleted.

### `PUT /books/{username}/{book_title}`

This endpoint updates the rating of a book in a user's list. It expects two path parameters: `username` and `book_title`, and optionally a request body containing the new rating.

# Plugin endpoints

These endpoints are needed to deliver the API as a plugin.

### `GET /logo.png`

This endpoint returns the application logo as a PNG file.

### `GET /.well-known/ai-plugin.json`

This endpoint returns the plugin manifest as a JSON file.

### `GET /openapi.yaml`

This endpoint returns the application's OpenAPI specification as a YAML file.
"# ChatGPT-Plugin" 
