import requests
from pprint import pprint


put_endpoint = "https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices"
get_endpoint = "https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices"
get_response = requests.get(url=get_endpoint)
get_data = get_response.json()["prices"]
# city_name = [value["city"] for value in get_data["prices"]]
# print(get_data)
class DataManager:
    def __init__(self):
        self.put_endpoint = "https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices"
        self.get_endpoint = "https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices"
        self.get_response = requests.get(url=self.get_endpoint)
        self.get_data = self.get_response.json()["prices"]
        self.city_name = [value["city"] for value in self.get_data]
        self.put_response = requests.put(url="https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices/[Object ID]")

    def update_city_code(self, id, code):
        sheet_parameters = {
            "price": {
                "iataCode": code
            }
        }
        sheet_endpoint = f"https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices/{id}"
        sheet_put = requests.put(url=sheet_endpoint, json=sheet_parameters)
        # print(sheet_put.text)

    def receive_price(self, id, price):
        sheet_parameters = {
            "price": {
                "lowestprice": price
            }
        }
        sheet_endpoint = f"https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices/{id}"
        sheet_edit = requests.put(url=sheet_endpoint, json=sheet_parameters)
        print(sheet_edit.text)

    #This class is responsible for talking to the Google Sheet.
