import os
from dotenv import find_dotenv, load_dotenv
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager

load_dotenv(find_dotenv())

data = FlightSearch(API_KEY=os.getenv("FLIGHT_SEARCH_KEY"))
sheety_data = DataManager()
target_cities_list = sheety_data.get_request()

for target_city in target_cities_list:

    fly_to = target_city["iataCode"]
    target_price = target_city["lowestPrice"]

    s_data = data.fly_searching(fly_from="WAW", fly_to=fly_to, date_from="04/10/2023", date_to="04/03/2024")

    flyData = FlightData(fly_from=s_data["flyFrom"], fly_to=s_data["flyTo"], utc_departure=s_data["utc_departure"],
                         utc_arrival=s_data["utc_arrival"], price=s_data["price"])
    if int(flyData.price) <= target_price:
        print(f"let`s go to {target_city['city']}. Only pay {flyData.price}")




#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.