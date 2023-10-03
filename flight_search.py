import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

TEQUILA_KEY = os.getenv("FLIGHT_SEARCH_KEY")
class FlightSearch:

    def __init__(self):
        self.fly_search_endpoint = "https://api.tequila.kiwi.com/v2"
    #This class is responsible for talking to the Flight Search API.
    pass