from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r'C:\driver_chrome\chromedriver.exe')
driver.get("https://www.w3schools.com/html/default.asp")
time.sleep(5)

content = driver.find_element(By.CSS_SELECTOR, 'a.w3-blue')
content.click()
