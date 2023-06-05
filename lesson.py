import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path = '/Users/alekseykhnyrev/PycharmProjects/pythonSeleniumProject/selenium_project/geckodriver')
driver.get('https://www.saucedemo.com')
driver.maximize_window()
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys('standard_user')
time.sleep(5)
driver.close()