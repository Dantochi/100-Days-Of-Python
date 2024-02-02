import requests
from datetime import datetime

TOKEN = "dantochi"
USERNAME = "dantochi"
pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=pixela_endpoint, json=PIXELA_PARAMS)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"
graph_params = {
    "id": graph_id,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

HEADERS = {
    "X-USER-TOKEN": TOKEN
}
today = datetime(year=2023, month=10, day=9)
print(today)
# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=HEADERS)
# print(graph_response.text)
graph_value_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}
graph_update_params = {
    "quantity": "10",
}

# graph_value_response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}", json=graph_value_params,
#                                      headers=HEADERS)
# graph_pixel_update = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}",
#                                   json=graph_update_params,
#                                   headers=HEADERS)
graph_pixel_delete = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}", headers=HEADERS)
print(graph_pixel_delete.text)
# print(graph_pixel_update.text)
# print(graph_value_response.text)
