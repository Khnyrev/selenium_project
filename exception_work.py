import datetime
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

"""Exception testing"""

driver = webdriver.Firefox(
    executable_path='/Users/alekseykhnyrev/PycharmProjects/pythonSeleniumProject/selenium_project/geckodriver')
base_url = 'https://demoqa.com/elements'
driver.get(base_url)
now_date = datetime.datetime.utcnow()
driver.maximize_window()

"""Переходим на https://demoqa.com/dynamic-properties - нужно для того что бы обойти проблему с долгой загрузко  перво   страницы"""

change_page = driver.find_element(By.XPATH, '//*[@id="item-8"]')
driver.execute_script("arguments[0].scrollIntoView();", change_page)
change_page.click()

try:
    visible_button = driver.find_element(By.XPATH, '//*[@id="visibleAfter"]')
    visible_button.click()
    print( 'visible button clicked')
except NoSuchElementException as exception:
    print("NoSuchElementException exception")
    time.sleep(7)
    visible_button = driver.find_element(By.XPATH, '//*[@id="visibleAfter"]')
    visible_button.click()
    print( 'visible button clicked')



time.sleep(5)
driver.close()