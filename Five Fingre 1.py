import time
from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("http://www.mitintech.com/admin/login/?next=/admin/")
time.sleep(5)
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="id_username"]').send_keys('Bhagyashri@123')
driver.find_element(By.XPATH,'//*[@id="id_password"]').send_keys('1234')
driver.find_element(By.XPATH,'//*[@id="login-form"]/div[3]/input').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="content-main"]/div[2]/table/tbody/tr[4]/th/a' ).click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[4]/td/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="id_name"]').send_keys('Marthi')
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="id_description"]').send_keys('My fav sub')
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="tblsubject_form"]/div/div/input[1]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[1]/td/a').click()
time.sleep(5)
gauri=Select(driver.find_element(By.NAME,'subject'))
gauri.select_by_index(19)
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="id_name"]').send_keys('Balbharti1')
time.sleep(5)
driver.find_element(By.NAME,'_save').click()
time.sleep(5)
driver.find_element(By,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[3]/td/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="id_name"]').send_keys('class1')
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="tblclass_form"]/div/div/input[1]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[2]/td/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="id_name"]').send_keys('shivaji')
time.sleep(5)
gauri=Select(driver.find_element(By.NAME,'subject'))
gauri.select_by_index(19)
time.sleep(5)
gauri=Select(driver.find_element(By.NAME,'Bookseries'))
gauri.select_by_index(75)










#driver.find_element(By.XPATH,'//*[@id="content"]/h1').click()
#time.sleep(5)
#driver.find_element(By.NAME,'worksheet1').send_keys("C:\\Users\\hp\\Desktop\\gauri data\\PANDIT BACHARAJ (1).pdf")
#time.sleep(5)



