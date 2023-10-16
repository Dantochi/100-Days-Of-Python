import requests
from datetime import datetime
from datetime import timedelta

tomorrow_time = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_month_time = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")

class FlightSearch:
    def __init__(self):
        self.kiwi_endpoint = "https://tequila-api.kiwi.com/locations/query"

    def get_code(self, city_name):
        KIWI_HEADERS = {
            # "Content-Type": "application/json",
            "apikey": "7dkRsFCeKx51x0lHtwTIgaoINiISf1uT",
            # "Content-Encoding": "gzip"
        }

        KIWI_PARAMETERS = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=self.kiwi_endpoint, headers=KIWI_HEADERS, params=KIWI_PARAMETERS)
        data = response.json()["locations"]
        city_code = data[0]["code"]
        return city_code

    def get_price(self, iatacode):
        FLIGHT_SEARCH_HEADER = {
            "apikey": "RA5XHq5Mn2r56SUiTf7hA23LUsJuQMSo",
            "Content-Type": "application/json",
            "Content-Encoding": "gzip"
        }
        FLIGHT_SEARCH_PARAMETERS = {
            "fly_from": "LON",
            "fly_to": iatacode,
            "date_from": tomorrow_time,
            "date_to": six_month_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        print(iatacode)
        flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        response = requests.get(url=flight_search_endpoint, params=FLIGHT_SEARCH_PARAMETERS,
                                headers=FLIGHT_SEARCH_HEADER)
        flight_data = response.json()
        return flight_data
        # flight_price = flight_data['data'][0]['price']
        # return f"£{flight_price}"

    #This class is responsible for talking to the Flight Search API.
    # FLIGHT_SEARCH_HEADER = {
    #     "apikey": "RA5XHq5Mn2r56SUiTf7hA23LUsJuQMSo",
    #     "Content-Type": "application/json",
    #     "Content-Encoding": "gzip"
    # }
    # FLIGHT_SEARCH_PARAMETERS = {
    #     "fly_from": "LON",
    #     "fly_to": "IST",
    #     "date_from": tomorrow_time,
    #     "date_to": six_month_time,
    #     "nights_in_dst_from": 7,
    #     "nights_in_dst_to": 28,
    #     "flight_type": "round",
    #     "one_for_city": 1,
    #     "max_stopovers": 0,
    #     "curr": "GBP"
    # }
    #
    # flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
    # response = requests.get(url=flight_search_endpoint, params=FLIGHT_SEARCH_PARAMETERS,
    #                         headers=FLIGHT_SEARCH_HEADER)
    # flight_data = response.json()
    # flight_price = flight_data['data'][0]['price']
    # print(flight_price)