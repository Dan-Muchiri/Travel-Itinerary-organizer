from modules.trip import Trip
from modules.accomodation import Accommodation
from modules.destination import Destination
from init import Base, engine
import ipdb


def debug():

  # Retrieve all trips
  all_trips = Trip.get_all_trips()
  print("All trips:")
  for trip in all_trips:
      print(trip)

  mytrip = Trip.add_trip(name="Trip to Paris", start_date="2024-04-01", end_date="2024-04-10", description="Exploring the beautiful city of Paris")

  # Retrieve all trips
  all_trips = Trip.get_all_trips()
  print("All trips:")
  for trip in all_trips:
      print(trip)

debug()
ipdb.set_trace()