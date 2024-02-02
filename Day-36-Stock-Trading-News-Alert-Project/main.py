import requests
import datetime as dt
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
TODAY_DATE = dt.datetime.now().date()
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "JCU9FG6CGMQ22J4L"
NEWS_API_KEY = "e2827e28c3814580a5552f92d799f2d0"
account_sid = 'ACe38d1d2aebedaa76be626de0c287b2ea'
auth_token = '01c5ead679a3d02c0a3858feda9fb7ca'
STOCK_PARAMETER = {
    'function': "TIME_SERIES_DAILY",
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}
NEWS_PARAMETERS = {
    'q': COMPANY_NAME,
    'from': "2023-10-07",
    'to': TODAY_DATE,
    'sortBy': "publishedAt",
    'apiKey': "e2827e28c3814580a5552f92d799f2d0",
    'language': "en"
}
news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERS)
stock_response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMETER)
news_data = news_response.json()
stock_data = stock_response.json()
# print(news_data)
# print(stock_data)
# print(TODAY_DATE)
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_price_data = [value for (key, value) in stock_data.items()]
yesterday_stock_price = float(stock_price_data[1]['2023-10-09']['4. close'])
print(yesterday_stock_price)
# TODO 2. - Get the day before yesterday's closing stock price
day_before_stock_price = float(stock_price_data[1]['2023-10-06']['4. close'])
# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
stock_price_difference = abs(yesterday_stock_price - day_before_stock_price)
# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
average = (yesterday_stock_price + day_before_stock_price) / 2
percentage_difference = round((stock_price_difference / average) * 100, 3)
print(percentage_difference)
# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
news_info = news_data['articles']
articles_slice = news_info[2:5]
print(articles_slice)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
keys_to_get = ['title', 'description']
articles_data = []
for news in range(3):
    articles_data.append(f"{articles_slice[news]['title']}, {articles_slice[news]['description']}")
print(articles_data)
# TODO 9. - Send each article as a separate message via Twilio.
if percentage_difference > 0:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12565489058',
        to='+2349060630130',
        body=f"{STOCK_NAME}: 🔺{percentage_difference} \n\nHeadline: {articles_data[0]}  \n\n Brief: {articles_data[1]}"
    )


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
