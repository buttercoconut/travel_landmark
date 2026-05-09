from pydantic import BaseModel
from typing import List, Optional

class Landmark(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    latitude: float
    longitude: float
    review_score: Optional[float] = None

class User(BaseModel):
    id: int
    username: str
    email: str

class Review(BaseModel):
    id: int
    user_id: int
    landmark_id: int
    rating: float
    comment: Optional[str] = None

class TravelPlan(BaseModel):
    id: int
    user_id: int
    name: str
    landmarks: List[int] = []