# Simple HTTP1.1 Server in Python

This repository contains a simple HTTP server built using Python's `socket` module. The server is designed to listen for HTTP requests, process `GET` requests, and return responses based on the requested path.

## Features

- **Simple HTTP GET Handling**: The server handles basic `GET` requests and serves specific files based on the requested path.
- **Content Delivery**:
  - Serves `index.html` when the root path `/` is requested.
  - Serves `randm.json` when the `/randm` path is requested.

## How It Works

1. The server binds to `0.0.0.0` on port `8080` and starts listening for incoming connections.
2. For each client connection:
   - Receives and decodes the HTTP request.
   - Checks if the HTTP method is `GET`.
   - Depending on the request path:
     - Serves `index.html` for `/`.
     - Serves `randm.json` for `/randm`.
3. Constructs HTTP headers and sends the response back to the client.
4. Closes the client connection after responding.
5. For unsupported HTTP methods, returns a `405 METHOD NOT ALLOWED` response.
