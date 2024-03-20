from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from init import Base, session
from datetime import datetime


class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    description = Column(String)

    # Relationship with Destination (one-to-many)
    destinations = relationship("Destination", back_populates="trip")

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

    @classmethod
    def get_all_trips(cls):
        """
        Retrieve all trips from the database.

        :return: A list of Trip objects representing all trips.
        """
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, trip_id):
        """
        Find a trip by its ID.

        :param trip_id: The ID of the trip to find.
        :return: The Trip object if found, None otherwise.
        """
        return session.query(cls).filter_by(id=trip_id).first()
    
    @classmethod
    def find_by_name(cls, name):
        """
        Find a trip by its name.

        :param name: The name of the trip to find.
        :return: The Trip object if found, None otherwise.
        """
        return session.query(cls).filter_by(name=name).first()
    
    @staticmethod
    def delete_trip(trip_id):
        """
        Delete a trip from the database.

        :param trip_id: The ID of the trip to delete.
        """
        trip = session.query(Trip).get(trip_id)
        if trip:
            session.delete(trip)
            session.commit()

    def duration(self):
        """
        Calculate the duration of the trip in days.

        :return: The duration of the trip in days.
        """
        # Convert start_date and end_date to datetime objects
        start_date = datetime.strptime(self.start_date, "%Y-%m-%d")
        end_date = datetime.strptime(self.end_date, "%Y-%m-%d")

        # Calculate the difference between end_date and start_date
        duration = (end_date - start_date).days

        return duration


