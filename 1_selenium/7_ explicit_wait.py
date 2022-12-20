import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\driver_chrome\chromedriver.exe')

    def test_explicit_wait(self):
        driver = self.driver
        driver.get("http://www.google.com")

        # Explicit Wait
        # Cargar un componente
        # Debe esperar hasta que cargue el componente, evite usar time
        try:
            # carga al elemento el google hasta 10 veces hasta encontrar el element q
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'q')))

        finally:
            driver.quit()


if __name__ == '__main__':
    unittest.main()
