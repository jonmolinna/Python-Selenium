from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'C:\driver_chrome\chromedriver.exe')
driver.get('https://www.gmail.com')

# user = driver.find_element('id', 'identifierId')
user = driver.find_element(By.ID, 'identifierId')
user.send_keys('jake.dallase96@gmail.com')
user.send_keys(Keys.ENTER)
time.sleep(3)

password = driver.find_element(By.NAME, "Passwd")
password.send_keys('dosdnowindfiuneiuninnjn')
password.send_keys(Keys.ENTER)
