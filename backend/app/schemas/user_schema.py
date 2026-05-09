# schemas/user_schema.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    preferences: Optional[dict] = None

    class Config:
        orm_mode = True
