import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

TEQUILA_KEY = os.getenv("FLIGHT_SEARCH_KEY")


class FlightSearch:

    def __init__(self):
        self.fly_search_endpoint = "https://api.tequila.kiwi.com/v2/search?"
        self.HEADER = {'apikey': TEQUILA_KEY}

    def fly_searching(self, fly_from: str, date_from: str, date_to: str):

        search_parameters = {
            "fly_from": fly_from,
            "date_from": date_from,
            "date_to": date_to
        }

        response = requests.get(url=self.fly_search_endpoint, headers=self.HEADER,
                                json=search_parameters)
        print(response.status_code)
        print(response.text)


fly_search = FlightSearch()
fly_search.fly_searching(fly_from="FRA", date_from="04/10/2023", date_to="06/10/2023")