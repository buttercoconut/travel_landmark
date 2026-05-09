# routes/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, User
from app.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)
