#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
sheet_data = DataManager()
cities = sheet_data.city_name
data = sheet_data.get_data
for x in data:
    city_code = FlightSearch(x)
    x["iataCode"] = city_code.city_code()
    sheet_update = sheet_data.city_code(x["id"], x["iataCode"])

print(sheet_update)
