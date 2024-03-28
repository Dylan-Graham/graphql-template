from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define SQLAlchemy base
Base = declarative_base()


# Define SQLAlchemy User model
class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)


# Set up SQLAlchemy engine and session
engine = create_engine("sqlite:///app/database/user.sqlite")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
