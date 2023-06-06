import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    executable_path='/Users/alekseykhnyrev/PycharmProjects/pythonSeleniumProject/selenium_project/geckodriver')
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
login_standard_user = 'standard_user55'
password_all = "secret_sauce"

driver.maximize_window()

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")  # XPAth
user_name.send_keys(login_standard_user)
print('Input Login')

password = driver.find_element(By.XPATH, "//input[@id='password']")  # css selector
password.send_keys(password_all)
print('Input Password')

button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print('Click Login button')

warning_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
value_warning_text = warning_text.text
assert value_warning_text == "Epic sadface: Username and password do not match any user in this service"
print("TEXT IS OKey !")

time.sleep(1)
driver.close()
