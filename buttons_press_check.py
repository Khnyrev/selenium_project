import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

"""Positive login testing"""

driver = webdriver.Firefox(
    executable_path='/Users/alekseykhnyrev/PycharmProjects/pythonSeleniumProject/selenium_project/geckodriver')
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
login_standard_user = 'standard_user'
password_all = "secret_sauce"

driver.maximize_window()

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")  # XPAth
user_name.send_keys(login_standard_user)
print('Input Login')
time.sleep(1)
# user_name.send_keys(Keys.BACKSPACE)

password = driver.find_element(By.XPATH, "//input[@id='password']")  # css selector
password.send_keys(password_all)
print('Input Password')
password.send_keys(Keys.RETURN)

filter = driver.find_element(By.XPATH, '//select[@class="product_sort_container"]')
filter.click()
print("Click FILTER")
time.sleep(5)

point = driver.find_element(By.XPATH, "//option[@value='za']")
time.sleep(1)
point.click()
print("Click on point")

time.sleep(10)
driver.close()
