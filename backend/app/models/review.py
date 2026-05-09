# models/review.py
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    landmark_id = Column(Integer, ForeignKey("landmarks.id"))
    rating = Column(Float)
    comment = Column(String)
    user = relationship("User", backref="reviews")
    landmark = relationship("Landmark", backref="reviews")

    def __repr__(self):
        return f"<Review {self.id} by {self.user_id} for {self.landmark_id}>"
