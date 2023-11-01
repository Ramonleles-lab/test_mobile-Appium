from appium import webdriver
from appium.options.android import UiAutomator2Options
from typing import Any, Dict  
from Environments import*
from Elements import*
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = (Elements_variable.desired_cap)
appium_server_ulr = (ulr)
options = UiAutomator2Options()
options.load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server_ulr, options=options)  

sleep(15)

#START_TEST

el1 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.login_email)
el1.send_keys(Elements_variable.login_email_value)
el2 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.login_password)
el2.send_keys(Elements_variable.login_password_value)
el3 = driver.find_element(by=AppiumBy.CLASS_NAME, value=Elements_variable.Button_login)
el3.click()

sleep(10)

#select_produt_multiple
el4 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.select_product1)
el4.click()
sleep(5)
el5 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.add_product1)
el5.click()
el6 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.Button_return_navigate)
el6.click()
sleep(5)
el7 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.select_product2)
el7.click()
sleep(5)
el8 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.add_product2)
el8.click()
el9 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.add_button_cart2)
el9.click()
sleep(5)
#checkout
el7 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.button_paymant)
el7.click()
sleep(5)
el8 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.button_pay_now)
el8.click()
sleep(5)
el9 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.button_ok)
el9.click()
sleep(5)


#END_TEST

driver.quit()