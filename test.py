import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.epam.com')

"""
search_btn = driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[3]/div/button/span[1]').click()
search_field = driver.find_element(By.XPATH, '//*[@id="new_form_search"]').send_keys('ai')
time.sleep(3)
"""

inv = driver.find_element(By.LINK_TEXT, 'INVESTORS').click()
time.sleep(5)


print(first_name)




driver.quit()