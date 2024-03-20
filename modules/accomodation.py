from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from init import Base

class Accommodation(Base):
    __tablename__ = 'accommodations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    check_in_date = Column(String)
    check_out_date = Column(String)
    notes = Column(String)
    destination_id = Column(Integer, ForeignKey('destinations.id'))

    # Relationship with Destination (many-to-one)
    destination = relationship("Destination", back_populates="accommodations")

    def __repr__(self):
        return f"Accommodation(id={self.id}, name={self.name})"

