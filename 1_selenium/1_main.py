from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\driver_chrome\chromedriver.exe')
driver.get("https://www.python.org/")
driver.close()


# pip install selenium
# pip install opencv-python
# pip install html-testRunner ----> Para hacer reportes en html
# pip list
