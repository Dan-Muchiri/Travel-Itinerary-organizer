from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from trip import Base

class Transportation(Base):
    __tablename__ = 'transportations'

    id = Column(Integer, primary_key=True)
    mode = Column(String, nullable=False)
    departure_date = Column(String)
    arrival_date = Column(String)
    departure_location = Column(String)
    arrival_location = Column(String)
    notes = Column(String)
    trip_id = Column(Integer, ForeignKey('trips.id'))

    # Relationship with Trip (many-to-one)
    trip = relationship("Trip", back_populates="transportations")

    def __repr__(self):
        return f"Transportation(id={self.id}, mode={self.mode})"


