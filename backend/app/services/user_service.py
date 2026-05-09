# services/user_service.py
from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user_schema import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate):
        hashed_password = pwd_context.hash(user.password)
        db_user = UserModel(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password,
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
