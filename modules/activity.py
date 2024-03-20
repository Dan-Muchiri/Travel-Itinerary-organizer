from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from init import Base

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String)
    time = Column(String)
    duration = Column(String)
    notes = Column(String)
    destination_id = Column(Integer, ForeignKey('destinations.id'))

    # Relationship with Destination (many-to-one)
    destination = relationship("Destination", back_populates="activities")

    def __repr__(self):
        return f"Activity(id={self.id}, name={self.name}, type={self.type})"

