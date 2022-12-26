from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'C:\driver_chrome\chromedriver.exe')
driver.get("https://google.com")
time.sleep(3)

element = driver.find_element(By.LINK_TEXT, 'Privacidad')

hover = ActionChains(driver).move_to_element(element)
hover.perform()
