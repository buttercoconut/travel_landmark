from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..schemas.landmark_schema import LandmarkCreate, LandmarkOut, ReviewCreate, ReviewOut, TravelPlanCreate, TravelPlanOut
from ..models.landmark import Landmark, User, Review, TravelPlan

router = APIRouter(prefix="/api", tags=["travel"])

# In-memory storage for demo purposes
landmarks: List[Landmark] = []
users: List[User] = []
reviews: List[Review] = []
travel_plans: List[TravelPlan] = []

@router.post("/landmarks", response_model=LandmarkOut)
def create_landmark(landmark: LandmarkCreate):
    new_id = len(landmarks) + 1
    new_landmark = Landmark(id=new_id, **landmark.dict())
    landmarks.append(new_landmark)
    return new_landmark

@router.get("/landmarks", response_model=List[LandmarkOut])
def list_landmarks():
    return landmarks

@router.post("/reviews", response_model=ReviewOut)
def create_review(review: ReviewCreate):
    new_id = len(reviews) + 1
    new_review = Review(id=new_id, **review.dict())
    reviews.append(new_review)
    return new_review

@router.get("/reviews", response_model=List[ReviewOut])
def list_reviews():
    return reviews

@router.post("/travel-plans", response_model=TravelPlanOut)
def create_travel_plan(plan: TravelPlanCreate):
    new_id = len(travel_plans) + 1
    new_plan = TravelPlan(id=new_id, **plan.dict())
    travel_plans.append(new_plan)
    return new_plan

@router.get("/travel-plans", response_model=List[TravelPlanOut])
def list_travel_plans():
    return travel_plans
