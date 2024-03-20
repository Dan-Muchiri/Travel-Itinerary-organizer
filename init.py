from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

# Define your database URL
db_url = "sqlite:///travel_organizer.db"


# Create the SQLAlchemy engine
engine = create_engine(db_url)

Base = declarative_base()

Base.metadata.bind = engine
    
# Create session
DBSession = sessionmaker(bind=engine)
session = DBSession()


