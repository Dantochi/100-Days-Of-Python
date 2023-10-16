#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
sheet_data = DataManager()
cities = sheet_data.city_name
data = sheet_data.get_data
city_code = FlightSearch()
print(data)
for x in data:
    x["iataCode"] = city_code.get_code(x["city"])
    sheet_code_update = sheet_data.update_city_code(x["id"], x["iataCode"]) # I update the sheet with the IATA code using the id from the data array
    receive_flight_data = city_code.get_price(city_code.get_price(x["iataCode"])) # I receive the price of a flight from london to a location with the parameter x["iataCode"]
    # receive_flight_price = receive_flight_data[0]
    # sheet_price_update = sheet_data.receive_price(x["id"], receive_flight_price)
    # print(f"£{receive_flight_price}")
    data_list = [receive_flight_data.keys]
    print(data_list)





