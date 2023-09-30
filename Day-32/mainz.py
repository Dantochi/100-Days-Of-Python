import random
import smtplib

import datetime as dt
import random as rd

#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2000, day=4, month=8)
# print(date_of_birth)
now = dt.datetime.now()
current_day = now.weekday()
print(current_day)

with open(file="quotes.txt", mode='r') as quotes:
    bank = random.choice(quotes.readlines())

if current_day == 5:
    email = "chiditochukwudaniel@gmail.com"
    password = "ulbeiqbhmkednqqp "
    with smtplib.SMTP("smtp.gmail.com") as connection:  # Location of email provider's smtp server
        connection.starttls()  # Means transfer layer security, encrypts the sent message paradventure the imge is intercepted
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="chiditochukwudaniel@outlook.com",
                            msg=f"Subject: Saturday Motivation :) \n\n {bank}")

