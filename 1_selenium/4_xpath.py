import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\driver_chrome\chromedriver.exe')

    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get('http://www.google.com')
        time.sleep(3)
        buscar_por_xpath = driver.find_element(
            By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        time.sleep(3)
        buscar_por_xpath.send_keys('Selenium', Keys.ARROW_DOWN)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()


# XPATH
# Es una direccion para encontrar los elementos dentro de una pagina
# Es una estructura de objectos

# 1. XPATH RELATIVO
# se usa mas el xpath relativo, ya que el codigo va cambiando

# 2. XPATH ABSOLUTO
