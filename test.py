import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import tempfile



#driver = webdriver.Chrome()


#driver.maximize_window()
#driver.get('https://www.epam.com/about')


download_directory = "C:\J"
expected_file = 'EPAM_Corporate_Overview_2023.pdf'
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_directory}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.epam.com/about')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[5]/section/div[2]/div/div/div[1]/div/div[3]/div/a').click()
time.sleep(3)
assert expected_file in os.listdir(download_directory)











driver.quit()