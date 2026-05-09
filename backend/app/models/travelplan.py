# models/travelplan.py
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class TravelPlan(Base):
    __tablename__ = "travel_plans"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)
    description = Column(String)
    landmarks = Column(JSON)  # list of landmark ids
    user = relationship("User", backref="travel_plans")

    def __repr__(self):
        return f"<TravelPlan {self.name}>"
