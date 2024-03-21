# destination.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from init import Base, session

class Destination(Base):
    __tablename__ = 'destinations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    trip_id = Column(Integer, ForeignKey('trips.id'))

    # Relationship with Trip (many-to-one)
    trip = relationship("Trip", back_populates="destinations")

    # Relationship with Accommodation (one-to-many)
    accommodations = relationship("Accommodation", back_populates="destination")

    def __repr__(self):
        return f"Destination(id={self.id}, name={self.name})"
    
    @classmethod
    def add_destination(cls, name, trip_id):
        """
        Add a new destination to the database.

        :param name: The name of the destination.
        :param trip_id: The trip id of the destination.
        """
        new_destination = Destination(name=name, trip_id=trip_id)
        session.add(new_destination)
        session.commit()

    
