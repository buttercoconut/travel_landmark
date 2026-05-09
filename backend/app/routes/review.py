# routes/review.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.review_service import ReviewService
from app.schemas.review_schema import ReviewCreate, Review
from app.database import get_db

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.post("/", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    service = ReviewService(db)
    return service.create_review(review)
