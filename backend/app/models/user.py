# models/user.py
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    preferences = Column(JSON)  # e.g., favorite categories

    def __repr__(self):
        return f"<User {self.username}>"
