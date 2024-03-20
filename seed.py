from modules.trip import Trip
from modules.accomodation import Accommodation
from modules.destination import Destination
from init import Base, engine
from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Create an instance of Faker
fake = Faker()

try:
    Base.metadata.drop_all(engine)
    # Create the database tables
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")
except SQLAlchemyError as e:
    print("Error creating database tables:", e)

# Define function to generate fake data for trips, destinations, accommodations, activities, and transportation
def generate_seed_data():
    Base.metadata.bind = engine
    
    # Create session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    try:
        # Generate seed data for trips
        trips = []
        for _ in range(5):
            trip = Trip(
                name=fake.word(),
                start_date=fake.date(),
                end_date=fake.date(),
                description=fake.sentence()
            )
            trips.append(trip)
            session.add(trip)

        # Generate seed data for destinations, accommodations,
        destinations = [] 
        for _ in range(10):
            destination = Destination(
                name=fake.country() + " City",
                trip=fake.random_element(trips)
            )
            destinations.append(destination)
            session.add(destination)

            accommodation = Accommodation(
                name=fake.company(),
                price=fake.random_number(digits=3),
                notes=fake.sentence(),
                destination=fake.random_element(destinations)
            )
            session.add(accommodation)


        # Commit the changes
        session.commit()

        # Return the generated data
        return trips

    except Exception as e:
        # Rollback the transaction if an exception occurs
        session.rollback()
        raise e

    finally:
        # Close session
        session.close()

if __name__ == "__main__":

    # Generate seed data # Clear
    generate_seed_data()


