from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="http://www.python.org/")
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")
# #To close a single tab and quit chrome is only one tab is currently opened
# driver.close()
# search = driver.find_element(By.NAME, value="q")
# print(search.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
# Using XPath... It never fails
# bug_link = driver.find_element(By.XPATH, value='/html/body/div/footer/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
dates_element = driver.find_elements(By.CSS_SELECTOR, value="li time")
date_list = [x.text.split("2023-")[1] for x in dates_element if dates_element.index(x) < 5]
# date = dates_element.split("T")[0]
event = driver.find_elements(By.CSS_SELECTOR, value="div.blog-widget div.shrubbery ul.menu li a")
event_list = [element.text for element in event]
# print(event_list)
# print(date_list)
latest_news = {x: {"time": date_list[x], "name": event_list[x]} for x in range(5)}


print(latest_news)
# To quit chrome entirely regardless of the amount of tabs opened
driver.quit()
