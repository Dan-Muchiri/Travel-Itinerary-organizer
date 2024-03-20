from modules.trip import Trip
from modules.accomodation import Accommodation
from modules.destination import Destination
from init import Base, engine
import ipdb


def debug():
  mytrip = Trip.add_trip(name="Trip to Paris", start_date="2024-04-01", end_date="2024-04-10", description="Exploring the beautiful city of Paris")

debug()
ipdb.set_trace()