import requests


class FlightSearch:

    def __init__(self, API_KEY: str):
        self.fly_search_endpoint = "https://api.tequila.kiwi.com/v2/search?"
        self.location_search_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.HEADER = {
            'apikey': API_KEY}
        self.is_result = None

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

        if response.json()["_results"] > 0:
            self.is_result = True
            print(response.json()["data"][0])
            return response.json()["data"][0]
        else:
            self.is_result = False

    def IATA_Code_searching(self, location_name: str):
        search_parameters = {
            "term": location_name,
            "locale": "en-US",
        }
        response = requests.get(url=self.location_search_endpoint, headers=self.HEADER, params=search_parameters)
        return response.json()["locations"][0]["code"]
