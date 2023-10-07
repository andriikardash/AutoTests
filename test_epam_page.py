from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_epam_title():
    driver.get('https://www.epam.com/')
    title = 'EPAM | Software Engineering & Product Development Services'
    page_title = driver.title
    assert page_title == title
    driver.quit()