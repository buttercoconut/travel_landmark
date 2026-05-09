# schemas/review_schema.py
from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    rating: float
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    user_id: int
    landmark_id: int

class Review(ReviewBase):
    id: int
    user_id: int
    landmark_id: int

    class Config:
        orm_mode = True
