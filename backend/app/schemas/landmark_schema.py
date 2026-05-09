from pydantic import BaseModel
from typing import List, Optional

class LandmarkCreate(BaseModel):
    name: str
    description: Optional[str] = None
    latitude: float
    longitude: float

class LandmarkOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    latitude: float
    longitude: float
    review_score: Optional[float]

class ReviewCreate(BaseModel):
    user_id: int
    landmark_id: int
    rating: float
    comment: Optional[str] = None

class ReviewOut(BaseModel):
    id: int
    user_id: int
    landmark_id: int
    rating: float
    comment: Optional[str]

class TravelPlanCreate(BaseModel):
    user_id: int
    name: str
    landmarks: List[int] = []

class TravelPlanOut(BaseModel):
    id: int
    user_id: int
    name: str
    landmarks: List[int]
