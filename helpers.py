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
    trip = Trip.find_by_name(name)
    if trip:
        print("Trip found:", trip)
    else: 
        print(f'Trip "{name}" not found')


def find_trip_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the trip's id: ")
    trip = Trip.find_by_id(id_)
    if trip:
        print("Trip found:", trip)
    else: 
        print(f'Trip "{id_}" not found')


def create_trip():
    name = input("Enter the trip's name: ")
    start_date = input("Enter the Trip's start_date in YY-MM-DD format: ")
    end_date = input("Enter the Trip's start_date in YY-MM-DD format: ")
    description = input("Enter the trip's description: ")
    try:
        trip = Trip.add_trip(name, start_date, end_date, description)
        print(f'Success: {trip}')
    except Exception as exc:
        print("Error creating trip: ", exc)


def update_trip():
    id_ = input("Enter the trip's id: ")
    if trip := Trip.find_by_id(id_):
        try:
            name = input("Enter the trip's new name: ")
            new_name = name
            start_date = input("Enter the trip's new start date in YY-MM-DD format: ")
            new_start_date = start_date
            end_date = input("Enter the trip's new end date in YY-MM-DD format: ")
            new_end_date = end_date
            description = input("Enter the trip's new description: ")
            new_description = description

            Trip.update_trip(id_, name=new_name, start_date=new_start_date, end_date=new_end_date, description=new_description)
            print(f'Success: {trip}')
        except Exception as exc:
            print("Error updating trip: ", exc)
    else:
        print(f'Trip {id_} not found')


def delete_trip():
    id_ = input("Enter the trip's id: ")
    if trip := Trip.find_by_id(id_):
        Trip.delete_trip(id_)
        print(f'Trip {id_} deleted')
    else:
        print(f'Trip {id_} not found')


