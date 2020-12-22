from selenium import webdriver
import time

chrome_driver_path = "/home/rgoshen/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

five_min = time.time() + 60 * 1     # 5 minutes

cookie = driver.find_element_by_id('cookie')

while True:
    cookie.click()

    if time.time() > five_min:
        break
