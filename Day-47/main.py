import requests
import smtplib
from bs4 import BeautifulSoup
import lxml

HEADER = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
}

requests = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
                        headers=HEADER)
response = requests.text
soup = BeautifulSoup(response, "lxml")
price_whole = soup.find("span", class_="a-price-whole").getText()
price_fraction = soup.find("span", class_="a-price-fraction").getText()
product_name = soup.find(name="span", id="productTitle").getText()
product_price = f"{price_whole}{price_fraction}"
print(product_name)

email = "chiditochukwudaniel@gmail.com"
password = "ulbeiqbhmkednqqp"
if float(product_price) < 100.0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="chiditochukwudaniel@outlook.com", msg=f"Subject: Amazon Price Alert \n\n{product_name}is now ${product_price}. Now would be a good time to buy".encode("utf-8"))

