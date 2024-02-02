from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
# no_of_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a").text
# print(no_of_articles)

# So it turns out that selenium has an easy way of locating anchor tags or link texts, it is just typing the text enclosed by the anchor tag
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# In order to enter some query into a search box...here's how
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# Another website
driver.get("http://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element(By.NAME, value="fName")
l_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
signup_btn = driver.find_element(By.CSS_SELECTOR, value=".btn")
f_name.send_keys("Tochukwu")
l_name.send_keys("Chidi")
email.send_keys("chiditochukwudaniel@gmail.com")
signup_btn.click()

# driver.quit()
