from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
cookie_btn = driver.find_element(By.CSS_SELECTOR, value="#cookie")
cursor_text = int(driver.find_element(By.CSS_SELECTOR, value="#buyCursor b").text.split()[2])
grandma_text = int(driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b").text.split()[2])
factory_text = int(driver.find_element(By.CSS_SELECTOR, value="#buyFactory b").text.split()[2])
mine_text = int(driver.find_element(By.CSS_SELECTOR, value="#buyMine b").text.split()[2].replace(',', ''))
shipment_text = int(driver.find_element(By.CSS_SELECTOR, value="#buyShipment b").text.split()[2].replace(',', ''))
alchemy_text = int(driver.find_element(By.CSS_SELECTOR, value="#buyAlchemy\ lab b").text.split()[3].replace(',', ''))
portal_text = int(driver.find_element(By.CSS_SELECTOR, value="#buyPortal b").text.split()[2].replace(',', ''))
time_machine_text = int(driver.find_element(By.CSS_SELECTOR, value="#buyTime\ machine b").text.split()[3].replace(',', ''))
cursor_btn = driver.find_element(By.ID, value="buyCursor")
grandma_btn = driver.find_element(By.ID, value="buyGrandma")
factory_btn = driver.find_element(By.ID, value="buyFactory")
mine_btn = driver.find_element(By.ID, value="buyMine")
shipment_btn = driver.find_element(By.ID, value="buyShipment")
alchemy_btn = driver.find_element(By.ID, value="buyAlchemy\ lab")
portal_btn = driver.find_element(By.ID, value="buyFactory")
time_machine_btn = driver.find_element(By.ID, value="buyTime\ machine")
timeout = time.time() + 60*5
start_time = time.time()
time_out = time.time() + 5
while True:
    cookie_btn.click()
    # test = 0
    if time.time() > time_out: # This is to confirm that the 5mins is not exceeded. The loop is to end after 5mins
        money_text = int(driver.find_element(By.CSS_SELECTOR, value="#money").text)
        # print(time.time() - start_time)
        # if (int(timeout) - int(time.time())) % 5 == 0:
        # if int(time.time() - start_time) == 5:
        # start_time = time.time()
        if money_text > time_machine_text:
            time_machine_btn.click()
        elif money_text > portal_text:
            portal_btn.click()
        elif money_text > alchemy_text:
            alchemy_btn.click()
        elif money_text > shipment_text:
            shipment_btn.click()
        elif money_text > mine_text:
            mine_btn.click()
        elif money_text > factory_text:
            factory_btn.click()
        elif money_text > grandma_text:
            grandma_btn.click()
        elif money_text > cursor_text:
            cursor_btn.click()
        else:
            print("passed")
        time_out = time.time() + 5
        # else:
        #     pass
        # print(money_text)


# driver.quit()