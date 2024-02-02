import requests
from datetime import datetime
import smtplib

MY_LAT = 4.876340  # Your latitude
MY_LONG = 7.055450  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour



# If the ISS is close to my current position
def proximity():
    if MY_LAT % iss_latitude <= 5 and MY_LONG % iss_longitude <= 5:
        if sunset <= time_now:
            return True
        else:
            return False

if proximity():
    email = "chiditochukwudaniel@gmail.com"
    password = "ulbeiqbhmkednqqp "
    with smtplib.SMTP("smtp.gmail.com") as connection:  # Location of email provider's smtp server
        connection.starttls()  # Means transfer layer security, encrypts the sent message paradventure the imge is intercepted
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="chiditochukwudaniel@outlook.com",
                            msg="Subject: ISS Location :) \n\n Look up now man, you're gonna see a star but in reality it's a satellite")
else:
    pass
# and it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.
print(sunset)
print(time_now)
