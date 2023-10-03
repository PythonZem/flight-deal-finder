import os
from dotenv import find_dotenv, load_dotenv
from flight_search import FlightSearch

load_dotenv(find_dotenv())
FLIGHT_SEARCH_KEY = os.getenv("FLIGHT_SEARCH_KEY")


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.