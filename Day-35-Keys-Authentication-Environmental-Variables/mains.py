import requests
from twilio.rest import Client
account_sid = 'ACe38d1d2aebedaa76be626de0c287b2ea'
auth_token = '4230728929c84124abc2b39549ad44a1'
api_key = "b37bae1c9bc63e0ae155c6ec3c5a7917"
PARAMETERS = {
    'lat': -22.913219,
    'lon': -47.055740,
    'appid': api_key,
}
response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=PARAMETERS)
data = response.json()
weather_data = data['weather'][0]['id']

will_rain = False

if weather_data > 500:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12565489058',
        to='+2349060630130',
        body="It's going to rain today bring an umbrella ☔"
    )
    print(message.sid)
else:
    print("weather is good today 👍")
print(response.status_code)
print(weather_data)
