import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

TEQUILA_KEY = os.getenv("FLIGHT_SEARCH_KEY")
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass