# ChatGPT Conversational Retrieval Plugin - FastAPI API

This repository contains a plugin for ChatGPT based on a REST API with FastAPI. The application is containerized using Docker and orchestrated with Docker Compose. Traffic is managed by an NGINX reverse proxy.

## Prerequisites

You need an OpenAI API_KEY to run this project. You also need access to the ChatGPT Plugins. These should be set as environment variables in the `docker-compose.yml` file.

## Docker and Docker Compose

To run this project, you need Docker and Docker Compose installed on your machine.

You can build and start the services using the following command:

```bash
docker-compose up --build
```

# Nginx

We use NGINX as a reverse proxy to route traffic to our FastAPI application. The configuration for NGINX is found in the `nginx.conf` file.

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
