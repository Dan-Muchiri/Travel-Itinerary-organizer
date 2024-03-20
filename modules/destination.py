# destination.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from init import Base

class Destination(Base):
    __tablename__ = 'destinations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    trip_id = Column(Integer, ForeignKey('trips.id'))

    # Relationship with Trip (many-to-one)
    trip = relationship("Trip", back_populates="destinations")

    # Relationship with Activity (one-to-many)
    activities = relationship("Activity", back_populates="destination")

    # Relationship with Accommodation (one-to-many)
    accommodations = relationship("Accommodation", back_populates="destination")

    def __repr__(self):
        return f"Destination(id={self.id}, name={self.name}, location={self.location})"
