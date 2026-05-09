# routes/landmark.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.landmark_service import LandmarkService
from app.schemas.landmark_schema import LandmarkCreate, Landmark
from app.models.landmark import Landmark as LandmarkModel
from app.database import get_db

router = APIRouter(prefix="/landmarks", tags=["landmarks"])

@router.post("/", response_model=Landmark)
def create_landmark(landmark: LandmarkCreate, db: Session = Depends(get_db)):
    service = LandmarkService(db)
    return service.create_landmark(landmark)

@router.get("/{landmark_id}", response_model=Landmark)
def read_landmark(landmark_id: int, db: Session = Depends(get_db)):
    service = LandmarkService(db)
    landmark = service.get_landmark(landmark_id)
    if not landmark:
        raise HTTPException(status_code=404, detail="Landmark not found")
    return landmark
