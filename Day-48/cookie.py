from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
cookie_btn = driver.find_element(By.CSS_SELECTOR, value="#cookie")
timeout = time.time() + 60*5
print(type(timeout))