import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""Smoke testing with two goods """

"""General settings"""
driver = webdriver.Firefox(
    executable_path='/Users/alekseykhnyrev/PycharmProjects/pythonSeleniumProject/selenium_project/geckodriver')
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
login_standard_user = 'standard_user'
password_all = "secret_sauce"

driver.maximize_window()

"""Login operation"""
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")  # XPAth
user_name.send_keys(login_standard_user)
print('Input Login')

password = driver.find_element(By.XPATH, "//input[@id='password']")  # css selector
password.send_keys(password_all)
print('Input Password')

button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print('Click Login button')

"""Set variables for 1st product"""
product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
name_product_1 = product_1.text  # product #1 name saved in to variable
print(name_product_1)

price_value_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
price_product_1 = price_value_product_1.text[1::]  # product #1 price value, saved in to variable
print(price_product_1)

select_product_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click()  # product #1 added to cart
print("Product_1 added to the cart")
print("-----")


"""Set variables for 2nd product"""
product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
name_product_2 = product_2.text  # product #2 name saved in to variable
print(name_product_2)

price_value_product_2 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
price_product_2 = price_value_product_2.text[1::]  # product #2 price value, saved in the variable
print(price_product_2)

select_product_2 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
select_product_2.click()
print('Product_2 added to the cart')
print("-----\n")

print('----------')
cart_icon = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
cart_icon.click()
print('Click on cart icon and going to the cart page')
print('----------\n')

"""Cart check"""

"""Check cart value for product #1"""
value_overview_name_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
cart_name_product_1 = value_overview_name_product_1.text
assert name_product_1 == cart_name_product_1, print("cart_name_product_1 ERROR")  # Name check
print('success name_product_1 == cart_name_product_1')

value_cart_price_product_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
cart_price_product_1 = value_cart_price_product_1.text[1::]  # Price check
assert price_product_1 == cart_price_product_1, print('cart_price_product_1 ERROR')
print('success price_product_1 == cart_price_product_1')
print("-----")

"""Check cart value for product #2"""
value_overview_name_product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
cart_name_product_2 = value_overview_name_product_2.text
assert name_product_2 == cart_name_product_2, print("cart_name_product_2 ERROR")  # Name check
print('success name_product_2 == cart_name_product_2')

value_cart_price_product_2 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
cart_price_product_2 = value_cart_price_product_2.text[1::]  # Price check
assert price_product_2 == cart_price_product_2, print('cart_price_product_2 ERROR')
print('success price_product_2 == cart_price_product_2')
print('----------\n')

checkout_button = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout_button.click()
print('Click on "checkout button" and going to the INFO page')
print('----------\n')

"""INFO page"""
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
print('click continue button and go to the Overview page')
print('----------\n')

"""Overview page check"""
"""Check Overview value for product #1"""
value_overview_name_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
overview_name_product_1 = value_overview_name_product_1.text
assert name_product_1 == overview_name_product_1, print("overview_name_product_1 ERROR")  # Name check
print('success name_product_1 == overview_name_product_1')

value_overview_price_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
overview_price_product_1 = value_overview_price_product_1.text[1::]  # Price check
assert price_product_1 == overview_price_product_1, print('overview_price_product_1 ERROR')
print('success price_product_1 == overview_price_product_1')
print("-----")
"""Check Overview value for product #2"""
value_overview_name_product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
overview_name_product_2 = value_overview_name_product_2.text
assert name_product_2 == overview_name_product_2, print("overview_name_product_2 ERROR")  # Name check
print('success name_product_2 == overview_name_product_2')

value_overview_price_product_2 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
overview_price_product_2 = value_overview_price_product_2.text[1::]  # Price check
assert price_product_2 == overview_price_product_2, print('overview_price_product_2 ERROR')
print('success price_product_2 == overview_price_product_2')
print('----------\n')

"""Price Total check"""
value_item_total = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]')
item_total = value_item_total.text[13::]
print("item_total = " + item_total)
# print(float(price_product_1) + float(price_product_2))
assert float(price_product_1) + float(price_product_2) == float(item_total), print("Prices not equal! ERROR")
print("success sum price_product_1 and price_product_2 are equal item_total")


time.sleep(3)
driver.close()
print("Test successful")
