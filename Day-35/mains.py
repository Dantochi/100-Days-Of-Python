import requests
from twilio.rest import Client
api_key = "b37bae1c9bc63e0ae155c6ec3c5a7917"
PARAMETERS = {
    'lat': 6.524379,
    'lon': 3.379206,
    'appid': api_key,
}
response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=PARAMETERS)
data = response.json()
weather_data = data['weather'][0]['id']

will_rain = False

if weather_data > 500:
    print("Bring an umbrella ☔")
else:
    print("weather is good today 👍")
print(response.status_code)
print(weather_data)
