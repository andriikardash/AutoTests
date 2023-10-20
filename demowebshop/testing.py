from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


home = webdriver.Chrome()
home.maximize_window()
ex = 'Your registration completed'
home.get("https://demowebshop.tricentis.com/registerresult/1")
time.sleep(3)
home.find_element(By.CLASS_NAME, 'ico-login').click()
time.sleep(3)



home.quit()