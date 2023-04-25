import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\google download\chromedriver_win32 (1)\chromedriver.exe")

driver.get("https://www.instagram.com/sem/campaign/emailsignup/?campaign_id=13530338610&extra_1=
driver.find_element(By.XPATH,').send_keys('gaikwad')
driver.find_element(By.XPATH,'//input[@name="Username"]').send_keys('gaurigaikwad')
driver.find_element(By.XPATH,'//input[@aria-label="Password"]').send_keys('abc@123')
driver.find_element(By.XPATH,'//input[@aria-label="Confirm"]').send_keys('abc@123')
driver.find_element(By.XPATH,'//*[@id="accountDetailsNext"]/div/button/div[3]').click()
time.sleep(5)
print(driver.title)
driver.close()