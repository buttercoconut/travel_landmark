# services/landmark_service.py
from sqlalchemy.orm import Session
from app.models.landmark import Landmark as LandmarkModel
from app.schemas.landmark_schema import LandmarkCreate

class LandmarkService:
    def __init__(self, db: Session):
        self.db = db

    def create_landmark(self, landmark: LandmarkCreate):
        db_landmark = LandmarkModel(**landmark.dict())
        self.db.add(db_landmark)
        self.db.commit()
        self.db.refresh(db_landmark)
        return db_landmark

    def get_landmark(self, landmark_id: int):
        return self.db.query(LandmarkModel).filter(LandmarkModel.id == landmark_id).first()
