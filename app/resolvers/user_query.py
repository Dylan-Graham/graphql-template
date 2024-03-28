from sqlalchemy import select
import strawberry

from app.models.user import User
from app.database.database import DBUser, Session


# @strawberry.type
# class Query:
#     @strawberry.field
#     def user(self, id: int) -> User:
#         for user in Users:
#             if user.id == id:
#                 return user
#         raise ValueError(f"User with id {id} not found")


@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User:
        session = Session()
        db_user = session.query(DBUser).filter(DBUser.id == id).first()
        session.close()
        if db_user:
            return User(
                id=db_user.id, name=db_user.name, age=db_user.age, gender=db_user.gender
            )
        else:
            raise ValueError(f"User with id {id} not found")
