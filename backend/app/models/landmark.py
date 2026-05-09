# models/landmark.py
from sqlalchemy import Column, Integer, String, Float, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Landmark(Base):
    __tablename__ = "landmarks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    review_score = Column(Float)
    metadata = Column(JSON)  # flexible JSONB for extra fields

    def __repr__(self):
        return f"<Landmark {self.name}>"
