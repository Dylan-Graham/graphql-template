import strawberry

from app.models.user import User, Users


@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User:
        for user in Users:
            if user.id == id:
                return user
        raise ValueError(f"User with id {id} not found")
