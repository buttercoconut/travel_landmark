"""CRUD operations for landmarks."""

from typing import List, Optional

from sqlalchemy.orm import Session

from ..models.landmark import Landmark as LandmarkModel
from ..schemas.landmark import LandmarkCreate, LandmarkUpdate, Landmark


def get_landmark(db: Session, landmark_id: int) -> Optional[LandmarkModel]:
    return db.query(LandmarkModel).filter(LandmarkModel.id == landmark_id).first()


def get_landmarks(db: Session, skip: int = 0, limit: int = 10) -> List[LandmarkModel]:
    return db.query(LandmarkModel).offset(skip).limit(limit).all()


def create_landmark(db: Session, landmark: LandmarkCreate) -> LandmarkModel:
    db_landmark = LandmarkModel(**landmark.dict())
    db.add(db_landmark)
    db.commit()
    db.refresh(db_landmark)
    return db_landmark


def update_landmark(db: Session, db_landmark: LandmarkModel, updates: LandmarkUpdate) -> LandmarkModel:
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(db_landmark, key, value)
    db.commit()
    db.refresh(db_landmark)
    return db_landmark


def delete_landmark(db: Session, db_landmark: LandmarkModel) -> None:
    db.delete(db_landmark)
    db.commit()
