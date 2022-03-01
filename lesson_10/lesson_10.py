# selenium
from selenium import webdriver

driver = webdriver.Firefox('/home/as/etc/selenium/geckodriver')
driver.get('http://google.com')
