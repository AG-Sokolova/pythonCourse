from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(service=Service(executable_path='./selenium/geckodriver'))
driver.get("http://itcareer.pythonanywhere.com")

# web_form = driver.find_element(By.CLASS_NAME, 'form-group')
# print(web_form.get_attribute('innerHTML'))

def field_entry(element, data):
    filed = driver.find_element(By.ID, element).send_keys(data)
    return filed


field_entry('name', 'Inna')
field_entry('surname', 'Didnt')
field_entry('email', 'inn_did@gmail.com')
field_entry('password', '12345qwert')

# success_massage = driver.find_element(By.TAG_NAME, 'strong')
# if 'Success' in success_massage.text:
#     print('Test success_massage - PASSED')
# else:
#     print('Test success_massage - FAILED')

time.sleep(3)
driver.close()
