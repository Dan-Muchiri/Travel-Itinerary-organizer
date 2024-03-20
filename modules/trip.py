from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from init import Base, session

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

    @classmethod
    def add_trip(cls, name, start_date, end_date, description):
        """
        Add a new trip to the database.

        :param name: The name of the trip.
        :param start_date: The start date of the trip.
        :param end_date: The end date of the trip.
        :param description: The description of the trip.
        """
        new_trip = Trip(name=name, start_date=start_date, end_date=end_date, description=description)
        session.add(new_trip)
        session.commit()
