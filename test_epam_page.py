from selenium import webdriver
from selenium.webdriver.common.by import By



def test_epam_title(driver):
    driver.get('https://www.epam.com/')
    title = 'EPAM | Software Engineering & Product Development Services'
    page_title = driver.title
    assert page_title == title
    driver.quit()