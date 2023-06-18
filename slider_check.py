import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

"""Data piker testing"""

driver = webdriver.Firefox(
    executable_path='/Users/alekseykhnyrev/PycharmProjects/pythonSeleniumProject/selenium_project/geckodriver')
base_url = 'https://www.schoolsw3.com/howto/howto_js_rangeslider.php'
driver.get(base_url)
now_date = datetime.datetime.utcnow()
driver.maximize_window()

action = ActionChains(driver)
round_slider = driver.find_element(By.XPATH, '//*[@id="id1"]')
action.click_and_hold(round_slider).move_by_offset(120, 0).release().perform()

time.sleep(5)
driver.close()