class FlightData:

    def __init__(self, fly_from: str, fly_to: str, utc_departure: str, utc_arrival: str, price: str):
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.utc_departure = f"{utc_departure[:10]} {utc_departure[11:19]}"
        self.utc_arrival = f"{utc_arrival[:10]} {utc_arrival[11:19]}"
        self.price = price
