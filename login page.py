import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#D:\google download\chromedriver_win32 (1)\chromedriver
driver=webdriver.Chrome(executable_path="D:\google download\chromedriver_win32 (1)\chromedriver.exe")
driver.get('https://www.instagram.com/accounts/login/')
driver.find_element(By.NAME,'email').send_keys('abc@gmail.com')
driver.find_element(By.NAME,'passward').send_keys('123')
driver.find_element(By.NAME,'login').click()
time.sleep(5)
print(driver.title)
