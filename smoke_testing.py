import datetime
import time
from selenium import webdriver
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

"""INFO Product #1"""
product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click()
print("Select_product_1")

cart =driver.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')
cart.click()
print("Enter cart")

"""INFO Cart #1"""
cart_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_cart_product_1 == value_product_1
print("INFO Cart #1 successful")

cart_price_product_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_product_1 = cart_price_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print(" successful")

checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()
print("Click on checkouy")

"""Enter User INFO"""
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys("Alex")
print("enter first_name")

last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys("Murphy")
print("enter last_name")

zip_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
zip_code.send_keys("12345")
print("enter zip_code")

continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')
continue_button.click()

"""INFO FINISH #1"""
finish_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_finish_product_1 == value_product_1
print("INFO FINISH #1 successful")

finish_price_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_finish_price_product_1 = finish_price_product_1.text
print(value_finish_price_product_1)
assert value_cart_price_product_1 == value_finish_price_product_1
print(" successful")

time.sleep(4)
driver.close()