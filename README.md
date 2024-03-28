# GraphQL Template with Python and FastAPI
This template provides a starting point for building GraphQL APIs using Python and FastAPI. 

## Getting Started
Clone the repository:\
git clone https://github.com/Dylan-Graham/graphql-template.git\\

Navigate into the project directory:\
cd graphql-template\\

Install dependencies:\
pip install -r requirements.txt\\

Run the application:\
python3 main.py\\
The application should now be running locally. Visit http://localhost:8000/graphql to access the GraphQL Playground and interact with the API.

## Project Structure
app/: Contains the main application code.\
database/: Contains connections to SQLite database.\
models/: Contains models.\
resolvers/: Contains resolver functions for GraphQL queries and mutations.\
main.py: Entry point for the FastAPI application.\
requirements.txt: Lists all Python dependencies required for the project.\
README.md: Documentation for the project.\

## Usage
GraphQL Endpoint
The GraphQL endpoint is available at /graphql. You can send POST requests to this endpoint with GraphQL queries and mutations in the request body.

Example query:

graphql
Copy code\
query {\
  users {\
    id\
    name\
    email\
  }\
}





