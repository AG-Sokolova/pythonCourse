from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=Service(executable_path='./selenium/geckodriver'))
driver.get("https://dd-node-api.herokuapp.com/")

name_filed = driver.find_element(By.NAME, 'name')
# name_filed.send_keys(names.)
print(names.get_first_name)

time.sleep(3)
driver.close()