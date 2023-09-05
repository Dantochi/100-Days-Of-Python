# with open(file="weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv # Helps display CSV files in a nicer format than that above

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        temperature.append(row[1])
        print(row)
    print(temperature)