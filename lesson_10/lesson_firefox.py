from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

driver = webdriver.Firefox(service=Service(executable_path='./selenium/geckodriver'))
driver.get("http://itcareer.pythonanywhere.com")

# web_form = driver.find_element_by_class_name('form_group')
# print(web_form.get_attribute('innerHTML'))

name_field = driver.find_element_by_id('name')
name_field.send_keys('Inna')

surname_field = driver.find_element_by_id('surname')
surname_field.send_keys('Didnt')

email_field = driver.find_element_by_id('email')
email_field.send_keys('inn_did@gmail.com')

password_field = driver.find_element_by_id('password')
password_field.send_keys('12345qwert')

time.sleep(3)
driver.close()
