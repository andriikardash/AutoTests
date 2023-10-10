import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os



driver = webdriver.Chrome()


driver.maximize_window()
driver.get('https://www.epam.com')

"""
search_btn = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[3]/div/button/span[1]').click()
search_field = driver.find_element(By.XPATH, '//*[@id="new_form_search"]').send_keys('ai')
time.sleep(3)
"""

global_btn = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[2]/div/div/button').click()
ukr_language = driver.find_element(By.XPATH, '//a[@href="https://careers.epam.ua"]').click()
time.sleep(5)



driver.quit()