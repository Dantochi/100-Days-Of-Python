import requests
from datetime import datetime
from datetime import timedelta
FLIGHT_SEARCH_HEADER = {
    "apikey": "RA5XHq5Mn2r56SUiTf7hA23LUsJuQMSo",
    "Content-Type": "application/json",
    "Content-Encoding": "gzip"
}

tomorrow_time = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_month_time = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
seven_days_time = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%y")
thirty_days_time = (datetime.now() + timedelta(days=30)).strftime("%d/%m/%y")

FLIGHT_SEARCH_PARAMETERS = {
    "fly_from": "LON",
    "fly_to": "FRA",
    "date_from": tomorrow_time,
    "date_to": six_month_time,
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 28,
    "flight_type": "round",
    "one_for_city": 1,
    "max_stopovers": 0,
    "curr": "GBP"
}

flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
response = requests.get(url=flight_search_endpoint, params=FLIGHT_SEARCH_PARAMETERS, headers=FLIGHT_SEARCH_HEADER)
flight_price = response.json()['data'][0]['price']
print(flight_price)

class FlightData:
    def __init__(self, price, airport_code, departure_city):
        self.price = ""
        self.departure_airport_code = ""
        self.departure_city = ""
    #This class is responsible for structuring the flight data.
    pass