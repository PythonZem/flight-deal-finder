import os
from dotenv import find_dotenv, load_dotenv
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

load_dotenv(find_dotenv())

FLY_KEY = os.getenv("FLIGHT_SEARCH_KEY")
TWILIO_KYE = os.getenv("TWILIO_KYE")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")

FlyData_SearchModule = FlightSearch(API_KEY=FLY_KEY)
sheety_data = DataManager()
target_cities_list = sheety_data.get_request()


def start_program():

    for target_city in target_cities_list:
        fly_fromCity = "Warsaw"
        fly_fromCode = "WAW"
        fly_toCode = target_city["iataCode"]
        fly_toCity = target_city["city"]
        target_price = target_city["lowestPrice"]

        s_data = FlyData_SearchModule.fly_searching(fly_from=fly_fromCode, fly_to=fly_toCode,
                                                    date_from="04/10/2023", date_to="04/03/2024")

        flyData = FlightData(fly_from=s_data["flyFrom"], fly_to=s_data["flyTo"], utc_departure=s_data["utc_departure"],
                             utc_arrival=s_data["utc_arrival"], price=s_data["price"])
        if float(flyData.price) <= target_price:
            text_sms = f"""Low price alert! Only €{flyData.price} to fly from {fly_fromCity}-{flyData.fly_from} to 
    {fly_toCity}-{fly_toCode}, from {flyData.utc_arrival} to {flyData.utc_departure}"""
            print(text_sms)
        # Sender_SMS = NotificationManager(KEY=TWILIO_KYE, TOKEN=TWILIO_TOKEN, text_sms=text_sms)
