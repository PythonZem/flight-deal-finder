import requests


class FlightSearch:

    def __init__(self, API_KEY: str):
        self.fly_search_endpoint = "https://api.tequila.kiwi.com/v2/search?"
        self.location_search_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.HEADER = {
            'apikey': API_KEY}

    def fly_searching(self, fly_from: str, fly_to: str,
                      date_from, date_to):
        search_parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(url=self.fly_search_endpoint, headers=self.HEADER,
                                params=search_parameters)

        return response.json()["data"][0]

    def IATA_Code_searching(self, location_name: str):
        search_parameters = {
            "term": location_name,
            "locale": "en-US",
        }
        response = requests.get(url=self.location_search_endpoint, headers=self.HEADER, params=search_parameters)
        return response.json()["locations"][0]["code"]
