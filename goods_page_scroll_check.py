import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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

password = driver.find_element(By.XPATH, "//input[@id='password']")  # css selector
password.send_keys(password_all)
print('Input Password')

button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print('Click Login button')

# driver.execute_script("window.scrollTo(0, 500)")

action = ActionChains(driver)
white_t_short = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
action.move_to_element(white_t_short).perform()

now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = "screenshot" + now_date + '.png'
driver.save_screenshot(
    '/Users/alekseykhnyrev/PycharmProjects/pythonSeleniumProject/selenium_project/screenshots/screen' + name_screenshot)

time.sleep(1)
driver.close()
