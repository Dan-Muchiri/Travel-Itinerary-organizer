# trip.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from init import Base


class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    description = Column(String)

    # Relationship with Destination (one-to-many)
    destinations = relationship("Destination", back_populates="trip")

    # Relationship with Transportation (one-to-many)
    transportations = relationship("Transportation", back_populates="trip")

    def __repr__(self):
        return f"Trip(id={self.id}, name={self.name}, start_date={self.start_date}, end_date={self.end_date})"
