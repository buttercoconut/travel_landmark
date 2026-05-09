# services/review_service.py
from sqlalchemy.orm import Session
from app.models.review import Review as ReviewModel
from app.schemas.review_schema import ReviewCreate

class ReviewService:
    def __init__(self, db: Session):
        self.db = db

    def create_review(self, review: ReviewCreate):
        db_review = ReviewModel(**review.dict())
        self.db.add(db_review)
        self.db.commit()
        self.db.refresh(db_review)
        return db_review
