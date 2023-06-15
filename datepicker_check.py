import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

"""Positive login testing"""

driver = webdriver.Firefox(
    executable_path='/Users/alekseykhnyrev/PycharmProjects/pythonSeleniumProject/selenium_project/geckodriver')
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
login_standard_user = 'standard_user'
password_all = "secret_sauce"

driver.maximize_window()

action = ActionChains(driver)
new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
new_date.clear()
new_date.send_keys("06/23/2023")
new_date.send_keys(Keys.RETURN)
time.sleep(4)

new_date.click()
date_tomorrow = driver.find_element(By.XPATH, '//div[@aria-label="Choose Thursday, June 15th, 2023"]')
date_tomorrow.click()

time.sleep(5)
driver.close()