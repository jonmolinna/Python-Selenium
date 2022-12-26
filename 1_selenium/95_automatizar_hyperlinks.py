from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r'C:\driver_chrome\chromedriver.exe')
driver.get('http://www.w3schools.com/')
time.sleep(3)

encontrar_link = driver.find_element(By.LINK_TEXT, 'Learn PHP')
encontrar_link.click()
