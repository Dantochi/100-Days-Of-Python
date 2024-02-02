from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import time

URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdXtdFc5CvkXg2VMudea5HwUUhOkrAzfVCbdFobi0Lk02b-lg/viewform"
response = requests.get(url=URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")
# print(soup.prettify())

# Getting the prices
price = [x.getText().strip("+/mo ").strip("+ 1 bd") for x in
         soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")]
print(len(price))

# Getting a list of links
links = [a["href"] for a in soup.find_all("a", class_="property-card-link")]
print(len(links))

# Getting the addresses
address = [x["alt"].replace("|", "") for x in soup.find_all("img", class_="Image-c11n-8-84-listing")]
print(len(address))

'''
Using Selenium for Google forms
'''
# Keep the browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
options = FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get(url=FORM)
x = 0
while x < 44:
    input_list = driver.find_elements(By.CSS_SELECTOR, value=".Xb9hP input")
    button = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")
    # another_response = driver.find_element(By.LINK_TEXT, value="Submit another response")
    # form_address.send_keys("Valley View Gardens")
    # Loop through the form address
    # print(button.text)


    def form_fill(x):
        input_list[0].send_keys(address[x])
        input_list[1].send_keys(price[x])
        input_list[2].send_keys(links[x])
        button.click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, value="Submit another response").click()
        time.sleep(3)


    form_fill(x)
    print(f"No.{x+1} response submitted...👍")
    x += 1

