from models.trip import Trip
from models.accommodation import Accommodation
from models.destination import Destination
from init import Base, engine
import ipdb


def debug():

    # Retrieve all trips
    all_trips = Trip.get_all_trips()
    print("All trips:")
    for trip in all_trips:
        print(trip)

    my_trip = Trip.add_trip(name="Trip to Paris", start_date="2024-04-01", end_date="2024-04-10", description="Exploring the beautiful city of Paris")

    # Retrieve all trips
    all_trips = Trip.get_all_trips()
    print("All trips:")
    for trip in all_trips:
        print(trip)

    search_trip = Trip.find_by_id(1)
    if search_trip:
        print("Trip found:", search_trip)
    else:
        print("Trip not found.")

    trip = Trip.find_by_name("Trip to Paris")
    if trip:
        print("Trip found:", trip)
    else:
        print("Trip not found.")

    Trip.delete_trip(5)

    # Retrieve all trips
    all_trips = Trip.get_all_trips()
    print("All trips:")
    for trip in all_trips:
        print(trip)

    trip = Trip.find_by_id(1)
    if trip:
        trip_duration = trip.duration()
        print(f"The duration of the trip {trip.name} is {trip_duration} days.")
    else:
        print("Trip not found.")

    trip = Trip.find_by_id(4)
    if trip:
        destinations = trip.get_destinations()
        for destination in destinations:
            print(destination)

    # Retrieve the trip object by its ID
    trip_to_update = Trip.find_by_id(4)
    if trip_to_update:
        new_name = "Updated Trip Name"
        new_start_date = "2024-03-01"
        new_end_date = "2024-03-10"
        new_description = "Updated trip description"
        Trip.update_trip(4, name=new_name, start_date=new_start_date, end_date=new_end_date, description=new_description)
        print("Trip updated successfully!")
    else:
        print("Trip with ID", 4, "not found.")





debug()
ipdb.set_trace()