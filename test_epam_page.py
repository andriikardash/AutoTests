from selenium import webdriver
from home_page import HomePage



def test_epam_title(driver):
    home = HomePage()
    home.nav_to_epam_page()
    TITLE = 'EPAM | Software Engineering & Product Development Services'
    assert home.get_title() == TITLE
    
#def test_dark_light_mode(driver):
#    driver.get('https://www.epam.com/')