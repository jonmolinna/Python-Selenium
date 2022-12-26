import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=r'C:\driver_chrome\chromedriver.exe')

    def test_radio_button(self):
        driver = self.driver
        driver.get(
            "https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
        time.sleep(5)

        radio_btn_2 = driver.find_element(
            By.XPATH, "//*[@id='main']/div[3]/div[1]/input[4]")
        radio_btn_2.click()
        time.sleep(3)

        radio_btn_1 = driver.find_element(
            By.XPATH, "//*[@id='main']/div[3]/div[1]/input[3]")
        radio_btn_1.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
