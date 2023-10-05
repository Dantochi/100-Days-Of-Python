import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json') # The url is the API endpoint or location from which our request is settled or sent
response.raise_for_status() # Helps to raise or specify the kind of error generated if the url or endpoint link is incorrect.

data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)
print(iss_position)