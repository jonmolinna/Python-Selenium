# Verifica si el elementos ya cargo en la pagina y si esta disponible

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'C:\driver_chrome\chromedriver.exe')
driver.get('https://www.google.com')

displayElement = driver.find_element(By.NAME, 'btnI')

# Verificando si el boton ya cargo en la pantalla -> return true o false
print(displayElement.is_displayed())

# Verifica si el boton esta habilitado
print(displayElement.is_enabled())
