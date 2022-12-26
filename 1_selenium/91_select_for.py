import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\driver_chrome\chromedriver.exe')

    def test_usando_select(self):
        driver = self.driver
        driver.get('https://www.w3schools.com/howto/howto_custom_select.asp')
        time.sleep(3)

        select = driver.find_element(
            By.XPATH, "//*[@id='main']/div[3]/div[1]/select")

        options = select.find_elements(By.TAG_NAME, 'option')
        time.sleep(3)

        for option in options:
            print("Los valores son: %s" % option.get_attribute("value"))
            option.click()
            time.sleep(1)

        seleccionar = Select(driver.find_element(
            By.XPATH, "//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
