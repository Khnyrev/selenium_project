import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

"""Data piker testing"""

driver = webdriver.Firefox(
    executable_path='/Users/alekseykhnyrev/PycharmProjects/pythonSeleniumProject/selenium_project/geckodriver')
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
now_date = datetime.datetime.utcnow()
driver.maximize_window()

future_date = now_date + datetime.timedelta(days=10)
formatted_future_date = future_date.strftime("%m/%d/%Y")  # get formatted date
print(formatted_future_date)

action = ActionChains(driver)
date_field = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
date_field.click()
date_field.clear()
date_field.send_keys(formatted_future_date)
date_field.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()