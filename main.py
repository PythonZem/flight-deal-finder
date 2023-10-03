import os
from dotenv import find_dotenv, load_dotenv
from flight_search import FlightSearch
from flight_data import FlightData
import json

load_dotenv(find_dotenv())

data = FlightSearch(API_KEY=os.getenv("FLIGHT_SEARCH_KEY"))
d = data.fly_searching(fly_from="IST", fly_to="PAR", date_from="04/10/2023", date_to="04/03/2024")

f = FlightData(fly_from=d["flyFrom"], fly_to=d["flyTo"], utc_departure=d["utc_departure"],
               utc_arrival=d["utc_arrival"], price=d["price"])
print(f.price)
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.