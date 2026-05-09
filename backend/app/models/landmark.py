"""ORM model for a travel landmark."""

from sqlalchemy import Column, Float, Integer, String
from . import Base

class Landmark(Base):
    """Database model representing a travel landmark."""

    __tablename__ = "landmarks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    country = Column(String, nullable=True)
    city = Column(String, nullable=True)
    category = Column(String, nullable=True)
    image_url = Column(String, nullable=True)

    def __repr__(self) -> str:
        return f"<Landmark(id={self.id}, name={self.name})>"
