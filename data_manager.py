import requests


class DataManager:
    def __init__(self):
        self.sheety_get_endpoint = "https://api.sheety.co/d5b0a8d3337206a8da7f7f5fd8862fd3/flightDeals/prices"

    def get_request(self):
        response = requests.get(url=self.sheety_get_endpoint)
        return response.json()["prices"]

    def put_IATACode(self, IATA_code: str, RowID: int):
        url = f"{self.sheety_get_endpoint}/{RowID}"
        params = {"price": {
            'iataCode': IATA_code}
        }
        response = requests.put(url=url, json=params)
        print(response.status_code)



