# schemas/landmark_schema.py
from pydantic import BaseModel
from typing import Optional

class LandmarkBase(BaseModel):
    name: str
    description: Optional[str] = None
    latitude: float
    longitude: float
    review_score: Optional[float] = None

class LandmarkCreate(LandmarkBase):
    pass

class Landmark(LandmarkBase):
    id: int

    class Config:
        orm_mode = True
