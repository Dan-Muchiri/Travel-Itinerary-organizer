from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from modules.trip import Trip
from modules.destination import Destination
from modules.activity import Activity
from modules.accomodation import Accommodation
from modules.transportation import Transportation
from init import Base

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
