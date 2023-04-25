import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\google download\chromedriver_win32 (1)\chromedriver.exe")

driver.get("https://www.facebook.com/campaign/landing.php?campaign_id=14884913640&extra_1=s%7Cc%7C589460569867%7Cb%7Cfacebook%20create%20new%20account%7C&placement=&creative=589460569867&keyword=facebook%20create%20new%20account&partner_id=googlesem&extra_2=campaignid%3D14884913640%26adgroupid%3D128696221432%26matchtype%3Db%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-298831213137%26loc_physical_ms%3D9302986%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=CjwKCAiA9NGfBhBvEiwAq5vSy2STOwdc3IT40-5WnsjJp4lKSZU2A54E988IlvnW9DPSYMCZiRW8BRoC8QEQAvD_BwE")
time.sleep(5)
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys('gauri')
driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys('gaikwad')
driver.find_element(By.XPATH,'//input[@name="reg_email__"]').send_keys('9359479594')
driver.find_element(By.XPATH,'//input[@name="reg_passwd__"]').send_keys('abc@123')
driver.find_element(By.XPATH,'//*[@id="day"]').send_keys('28')
driver.find_element(By.XPATH,'//*[@id="month"]').send_keys('mar')
driver.find_element(By.XPATH,'//*[@id="year"]').send_keys('1999')
driver.find_element(By.XPATH,'//input[@name="sex"]').click()
time.sleep(5)
driver.find_element(By.NAME,'websubmit').click()
time.sleep(10)
print(driver.title)
driver.close()


