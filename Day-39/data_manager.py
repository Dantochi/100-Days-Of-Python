import requests
from pprint import pprint


put_endpoint = "https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices"
get_endpoint = "https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices"
get_response = requests.get(url=get_endpoint)
get_data = get_response.json()["prices"]
# city_name = [value["city"] for value in get_data["prices"]]
print(get_data)
class DataManager:
    def __init__(self):
        self.put_endpoint = "https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices"
        self.get_endpoint = "https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices"
        self.get_response = requests.get(url=self.get_endpoint)
        self.get_data = self.get_response.json()["prices"]
        self.city_name = [value["city"] for value in self.get_data]
        self.put_response = requests.put(url="https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices/[Object ID]")

    def sheet_put(self, arr):
        for x in range(len(self.get_data) - 1):
            SHEET_PARAMETERS = {
                "price": {
                    "iata code": arr[x]
                }
            }

            sheet_input = f"https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/flightDeals/prices/{self.get_data[x]["id"]}"
            sheet_put = requests.put(url=sheet_input, json=SHEET_PARAMETERS)

    #This class is responsible for talking to the Google Sheet.
    pass