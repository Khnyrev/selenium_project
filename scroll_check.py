import datetime
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

"""Positive login testing"""

driver = webdriver.Firefox(
    executable_path='/Users/alekseykhnyrev/PycharmProjects/pythonSeleniumProject/selenium_project/geckodriver')
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
login_standard_user = 'standard_user'
password_all = "secret_sauce"

driver.maximize_window()

action = ActionChains(driver)
double_click = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
action.double_click(double_click).perform()

right_click = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
action.context_click(right_click).perform()

# check_box = driver.find_element(By.XPATH, '//input[@id="tree-node-documents"]/following-sibling::span[@class="rct-checkbox"]')  # XPAth
# check_box.click()

time.sleep(5)
driver.close()