import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.epam.com/')


html = driver.find_element(By.CSS_SELECTOR, 'header')
initial_color = html.value_of_css_property('background-color')
toggle = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/header/div/div/section/div/div").click()
time.sleep(2)
changed_color = html.value_of_css_property('background-color')
assert initial_color != changed_color


driver.quit()