from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from trip import Base, Trip
from destination import Destination
from activity import Activity
from accomodation import Accommodation
from transportation import Transportation

# Define your database URL
db_url = "sqlite:///travel_organizer.db"


# Create the SQLAlchemy engine
engine = create_engine(db_url)

try:
    Base.metadata.drop_all(engine)
    # Create the database tables
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")
except SQLAlchemyError as e:
    print("Error creating database tables:", e)
