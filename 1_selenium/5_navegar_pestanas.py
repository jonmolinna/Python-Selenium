import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\driver_chrome\chromedriver.exe')

    def test_cambiar_pestana(self):
        driver = self.driver
        driver.get('http://www.google.com')
        time.sleep(3)
        driver.execute_script("window.open('');")  # pestaña 1
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])  # pestaña 2
        driver.get("http://stackoverflow.com")
        time.sleep(3)
        # regresa a pestaña 0
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
