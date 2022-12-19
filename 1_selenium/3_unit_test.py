import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\driver_chrome\chromedriver.exe')

    def test_buscar(self):
        driver = self.driver
        driver.get('https://www.google.com')
        # verifica que el title del pagina sea google
        self.assertIn('Google', driver.title)
        elemento = driver.find_element(By.NAME, 'q')
        elemento.send_keys('Selenium')
        elemento.send_keys(Keys.RETURN)  # ENTER
        time.sleep(5)

        assert "No se encontro el elemento" not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
