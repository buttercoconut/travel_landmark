"""Pydantic schemas for request/response validation."""

from typing import Optional

from pydantic import BaseModel, Field

class LandmarkBase(BaseModel):
    name: str = Field(..., example="Eiffel Tower")
    description: Optional[str] = Field(None, example="Iconic Paris landmark")
    latitude: float = Field(..., example=48.8584)
    longitude: float = Field(..., example=2.2945)
    country: Optional[str] = Field(None, example="France")
    city: Optional[str] = Field(None, example="Paris")
    category: Optional[str] = Field(None, example="Monument")
    image_url: Optional[str] = Field(None, example="https://example.com/eiffel.jpg")

class LandmarkCreate(LandmarkBase):
    pass

class LandmarkUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    country: Optional[str] = None
    city: Optional[str] = None
    category: Optional[str] = None
    image_url: Optional[str] = None

class LandmarkInDBBase(LandmarkBase):
    id: int

    class Config:
        orm_mode = True

class Landmark(LandmarkInDBBase):
    pass

class LandmarkList(BaseModel):
    items: list[Landmark]
    total: int
