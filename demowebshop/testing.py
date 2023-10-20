from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


home = webdriver.Chrome()
home.maximize_window()
ex = 'Your registration completed'
home.get("https://demowebshop.tricentis.com/")
time.sleep(3)
home.find_element(By.LINK_TEXT, 'Computers').click()
res = home.find_element(By.XPATH, "//a[@href='/computers']/following-sibling::ul[@class='sublist']").text
print(res)



home.quit()