import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()


driver.maximize_window()
driver.get('https://www.epam.com')


driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[3]/div/button/span[1]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
time.sleep(1)
search_field = driver.find_element(By.XPATH, '//*[@id="new_form_search"]').send_keys('ai')
driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[3]/div/div/form/div[1]/button').click()
search_actual = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/section/div[2]/div[4]/section/h2').text
search_expected = 'RESULTS FOR "AI"'
assert search_expected in search_actual
time.sleep(3)











driver.quit()