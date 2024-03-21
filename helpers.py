import datetime
from models.trip import Trip
from models.destination import Destination


def exit_program():
    print("Goodbye!")
    exit()


def list_trips():
    all_trips = Trip.get_all_trips()
    print("All trips:")
    for trip in all_trips:
        print(trip)


def find_trip_by_name():
    name = input("Enter the trip's name: ")
    trips = Trip.find_by_name(name)
    if trips:
        print("Trips found:")
        for trip in trips:
          print(trip)
    else: 
        print(f'Trip "{name}" not found')


def find_trip_by_id():
    # Use a trailing underscore not to override the built-in id function
    id_ = input("Enter the trip's id: ")
    trip = Trip.find_by_id(id_)
    if trip:
        print("Trip found:", trip)
    else: 
        print(f'Trip "{id_}" not found')


def create_trip():
    while True:
        name = input("Enter the trip's name: ")
        start_date = input("Enter the Trip's start date in YYYY-MM-DD format: ")
        end_date = input("Enter the Trip's end date in YYYY-MM-DD format: ")
        description = input("Enter the trip's description: ")

        try:
            # Validate date format
            datetime.datetime.strptime(start_date, "%Y-%m-%d")
            datetime.datetime.strptime(end_date, "%Y-%m-%d")
            # Ensure end_date is after start_date
            if end_date <= start_date:
                raise ValueError("End date must be after start date")

            # If all validations pass, add the trip
            trip = Trip.add_trip(name, start_date, end_date, description)
            print(f'Success: "{name}" Trip created')
            break
        except ValueError as ve:
            print("Error creating trip: ", ve)


def update_trip():
    while True:
        id_ = input("Enter the trip's id: ")
        trip = Trip.find_by_id(id_)
        if not trip:
            print(f'Trip {id_} not found')
            return

        name = input("Enter the trip's new name: ")
        start_date = input("Enter the trip's new start date in YY-MM-DD format: ")
        end_date = input("Enter the trip's new end date in YY-MM-DD format: ")
        description = input("Enter the trip's new description: ")

        try:
            # Validate date format
            datetime.datetime.strptime(start_date, "%Y-%m-%d")
            datetime.datetime.strptime(end_date, "%Y-%m-%d")
            # Ensure end_date is after start_date
            if end_date <= start_date:
                raise ValueError("End date must be after start date")

            # If all validations pass, update the trip
            Trip.update_trip(id_, name=name, start_date=start_date, end_date=end_date, description=description)
            print(f'Successfully updated trip: {trip}')
            break
        except ValueError as ve:
            print("Error updating trip: ", ve)


def delete_trip():
    id_ = input("Enter the trip's id: ")
    trip = Trip.find_by_id(id_)
    if trip:
        trip_name = trip.name
        Trip.delete_trip(id_)
        print(f'Trip "{trip_name}" deleted')
    else:
        print(f'Trip "{id_}" not found')



def get_duration():
    id_ = input("Enter the trip's id: ")
    if trip := Trip.find_by_id(id_):
        trip_duration = trip.duration()
        print(f"The duration of the trip '{trip.name}' is {trip_duration} days.")
    else:
        print("Trip not found.")

def get_destinations():
    trip_id = input("Enter the trip's id: ")
    trip = Trip.find_by_id(trip_id)
    if trip:
        destinations = trip.get_destinations()
        if destinations:
            print(f"Destinations for Trip '{trip.name}':")
            for destination in destinations:
                print(f"Destination: {destination.name}, ID: {destination.id}")
        else:
            print(f"No destinations found for Trip '{trip.name}'.")
    else:
        print("Trip not found.")


def get_description():
    id_ = input("Enter the trip's id: ")
    if trip := Trip.find_by_id(id_):
        print(f"Trip Name: {trip.name}")
        print(f"Description: {trip.description}")
    else:
        print("Trip not found.")

def add_destination():
    name = input("Enter the destination's name: ")
    trip_id = input("Enter the trip's id: ")
    trip = Trip.find_by_id(trip_id)
    if trip:
        Destination.add_destination(name, trip_id)
        print(f"Destination '{name}' added to trip '{trip.name}' successfully.")
    else:
        print("No trip found with specified ID.")

