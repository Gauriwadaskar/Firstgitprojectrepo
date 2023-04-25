import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("http://www.mitintech.com/auth")
time.sleep(3)
driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/nav/label[1]/i').click()

time.sleep(3)
driver.find_element(By.XPATH,'/html/body/nav/ul/li[3]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys('Bhagyashri@123')
driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('1234')
driver.find_element(By.XPATH,'//*[@id="mymodal"]/div/div/div[2]/form/div/input[3]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//input[@type="submit"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//select[@name="subject_id"]').click()
driver.find_element(By.XPATH,'//select[@name="bookseries"]').click()
driver.find_element(By.XPATH,'//select[@name="classid_id"]').send_keys('class1')
driver.find_element(By.XPATH,'//input[@value="Search"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//select[@id="chapter_id"]').send_keys('S-3_Chapter1')
driver.find_element(By.XPATH,'//input[@style="width:150px;"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div[2]/div/div/div[1]/div/a[2]').click()
driver.close()



