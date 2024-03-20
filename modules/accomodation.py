from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from init import Base

class Accommodation(Base):
    __tablename__ = 'accommodations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    notes = Column(String)
    destination_id = Column(Integer, ForeignKey('destinations.id'))

    # Relationship with Destination (many-to-one)
    destination = relationship("Destination", back_populates="accommodations")

    def __repr__(self):
        return f"Accommodation(id={self.id}, name={self.name})"

