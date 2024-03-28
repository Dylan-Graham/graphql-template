from typing import List
import uvicorn

import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


# Model
@strawberry.type
class User:
    id: int
    name: str
    age: int
    gender: str


# "Database"
Users: List[User] = [User(id=1, name="Patrick", age=100, gender="Male")]


# Query
@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User:
        for user in Users:
            if user.id == id:
                return user
        raise ValueError(f"User with id {id} not found")


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
