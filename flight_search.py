import requests


class FlightSearch:

    def __init__(self, API_KEY: str):
        self.API_KEY = API_KEY
        self.fly_search_endpoint = "https://api.tequila.kiwi.com/v2/search?"
        self.HEADER = {
            'accept': 'json',
            'apikey': API_KEY}

    def fly_searching(self, fly_from: str, fly_to: str,
                      date_from: str, date_to: str):

        search_parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to
        }

        response = requests.get(url=self.fly_search_endpoint, headers=self.HEADER,
                                params=search_parameters)

        return response.json()["data"][0]
