import time
from turtle import title

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\google download\chromedriver_win32 (1)\chromedriver.exe")

driver.get ("https://www.facebook.com/login/")
time.sleep(5)
driver.maximize_window()
driver.find_element(By.NAME,'email').send_keys('abc@gmail.com')
driver.find_element(By.NAME,'pass').send_keys('12345')
driver.find_element(By.NAME,'login').click()
print(driver.title)
driver.back()
driver.forward()
time.sleep(5)
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
print(driver.title)
driver.close()
