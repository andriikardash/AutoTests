from selenium import webdriver
from home_page import HomePage
from selenium.webdriver.common.by import By
from contact_page import ContactPage



def test_epam_title(driver):
    home = HomePage()
    home.nav_to_epam_page()
    TITLE = 'EPAM | Software Engineering & Product Development Services'
    assert home.get_title() == TITLE
    
def test_dark_light_mode(driver):
    home = HomePage()
    home.nav_to_epam_page()
    home.check_header_background_color()
    
def test_policies_list(driver):
    home = HomePage()
    home.nav_to_epam_page()
    home.check_policies_link_available()


def test_contact_required_fields(driver):  
    contact = ContactPage()    
    contact.nav_to_epam_contact_page()
    contact.is_contact_fields_required()


def test_company_logo(driver):
    epam_url = 'https://www.epam.com/'    
    about = ContactPage()
    about.nav_to_epam_about_page()
    about.click_epam_logo_button()
    url = about.get_current_url()
    assert epam_url == url
    