# Implicit Wait
# es igual al time sleep
# es menos usado
# espera un tiempo para cargar un component
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\driver_chrome\chromedriver.exe')

    def test_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)  # dale pausa 5 segundos
        driver.get("http://www.google.com")

        # carga el elemento q o encuentra el elementos con el id q
        # Es para componentes dinamicos como Modal
        myDynamicElement = driver.find_element(By.NAME, 'q')


if __name__ == '__main__':
    unittest.main()
