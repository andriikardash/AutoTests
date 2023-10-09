import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.epam.com/about')

"""
search_btn = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[3]/div/button/span[1]').click()
search_field = driver.find_element(By.XPATH, '//*[@id="new_form_search"]').send_keys('ai')
time.sleep(3)
"""

epam_url = 'https://www.epam.com/'
logo_btn = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div/div/header/div/div/a[1]').click()
new_url = driver.current_url
assert epam_url == new_url







driver.quit()