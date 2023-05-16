# ChatGPT Conversational Retrieval Plugin - FastAPI API

In this repo, you will find a plugin for ChatGPT based on a REST API with FastAPI.

## Prerequisites

You need an OpenAI API_KEY to run this project. You also need access to the ChatGPT Plugins. It has to be placed inside the `.env` file.

## App Endpoints

The following endpoint describes the core functionality of the app, where you can interact with a conversational retrieval model.

### `POST /chat`

This endpoint interacts with the conversational retrieval model. It expects a JSON object in the body containing the query.

## Plugin endpoints

These endpoints are needed to deliver the API as a plugin.

### `GET /logo.png`

This endpoint returns the application logo as a PNG file.

### `GET /.well-known/ai-plugin.json`

This endpoint returns the plugin manifest as a JSON file.

### `GET /openapi.yaml`

This endpoint returns the application's OpenAPI specification as a YAML file.
