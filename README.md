# GraphQL Template with Python and FastAPI
This template provides a starting point for building GraphQL APIs using Python and FastAPI. GraphQL is a powerful query language for APIs, allowing clients to request exactly the data they need. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python.

## Features
GraphQL: Implement GraphQL endpoints to provide a flexible query interface for clients.
FastAPI: Utilize FastAPI for building high-performance asynchronous APIs with automatic interactive API documentation (Swagger UI and ReDoc).
Pydantic Models: Define data models with Pydantic for input validation and serialization.
AsyncIO: Leverage asyncio for handling asynchronous operations efficiently.
Dependency Injection: Use FastAPI's dependency injection system for managing dependencies and shared resources.
GraphQL Playground: Integrate GraphQL Playground for interactive exploration of the GraphQL schema and queries.
Custom Middleware: Extend functionality with custom middleware for handling cross-cutting concerns.

## Getting Started
Clone the repository:
bash
Copy code
git clone https://github.com/Dylan-Graham/graphql-template.git
Navigate into the project directory:
bash
Copy code
cd graphql-template
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run the application:
bash
Copy code
python3 main.py
The application should now be running locally. Visit http://localhost:8000 to access the GraphQL Playground and interact with the API.

## Project Structure
app/: Contains the main application code.
database/: Contains connections to SQLite database.
models/: Contains models.
resolvers/: Contains resolver functions for GraphQL queries and mutations.
main.py: Entry point for the FastAPI application.
requirements.txt: Lists all Python dependencies required for the project.
README.md: Documentation for the project.


## Usage
GraphQL Endpoint
The GraphQL endpoint is available at /graphql. You can send POST requests to this endpoint with GraphQL queries and mutations in the request body.

Example query:

graphql
Copy code
query {
  users {
    id
    name
    email
  }
}





