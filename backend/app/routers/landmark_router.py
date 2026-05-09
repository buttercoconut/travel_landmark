"""Router for landmark endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from ..crud.landmark import (
    create_landmark,
    delete_landmark,
    get_landmark,
    get_landmarks,
    update_landmark,
)
from ..schemas.landmark import (
    Landmark,
    LandmarkCreate,
    LandmarkList,
    LandmarkUpdate,
)

router = APIRouter()

@router.get("/", response_model=LandmarkList)
async def read_landmarks(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    landmarks = get_landmarks(db, skip=skip, limit=limit)
    return LandmarkList(items=landmarks, total=len(landmarks))

@router.post("/", response_model=Landmark, status_code=status.HTTP_201_CREATED)
async def create_new_landmark(
    landmark_in: LandmarkCreate,
    db: Session = Depends(get_db),
):
    return create_landmark(db, landmark=landmark_in)

@router.get("/{landmark_id}", response_model=Landmark)
async def read_landmark(
    landmark_id: int,
    db: Session = Depends(get_db),
):
    db_landmark = get_landmark(db, landmark_id)
    if db_landmark is None:
        raise HTTPException(status_code=404, detail="Landmark not found")
    return db_landmark

@router.put("/{landmark_id}", response_model=Landmark)
async def update_existing_landmark(
    landmark_id: int,
    updates: LandmarkUpdate,
    db: Session = Depends(get_db),
):
    db_landmark = get_landmark(db, landmark_id)
    if db_landmark is None:
        raise HTTPException(status_code=404, detail="Landmark not found")
    return update_landmark(db, db_landmark, updates)

@router.delete("/{landmark_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_landmark(
    landmark_id: int,
    db: Session = Depends(get_db),
):
    db_landmark = get_landmark(db, landmark_id)
    if db_landmark is None:
        raise HTTPException(status_code=404, detail="Landmark not found")
    delete_landmark(db, db_landmark)
    return None
