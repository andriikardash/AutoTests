from email.policy import Policy
from turtle import down
from selenium import webdriver
from home_page import HomePage
from selenium.webdriver.common.by import By
from contact_page import ContactPage
from about_download import Download
import time
from policy import Policy


# Check the title is correct
def test_epam_title(driver):
    home = HomePage()
    home.nav_to_epam_page()
    TITLE = 'EPAM | Software Engineering & Product Development Services'
    assert home.get_title() == TITLE
  
# Check the ability to switch Light / Dark mode
def test_dark_light_mode(driver):
    home = HomePage()
    home.nav_to_epam_page()
    initial_color = home.get_background_color()
    home.click_on_dark_light_toggle()
    current_color = home.get_background_color()
    assert initial_color != current_color
 
# Check that allow to change language to UA. 
# Please note, there is no ukr language. It just redirects you to another page
def test_change_language_to_ukr(driver):
    ukr_url = 'https://careers.epam.ua/'
    home = HomePage()
    home.nav_to_epam_page()
    home.go_to_ukr_page()
    url = home.get_current_url()
    assert ukr_url == url
    
# Check the policies list
def test_policy_available(driver):
    home = Policy()
    home.nav_to_epam_page()
    home.check_policy_available('investors')
    home.check_policy_available('open source')
    home.check_policy_available('privacy policy')
    home.check_policy_available('cookie policy')
    home.check_policy_available('applicant privacy notice')
    home.check_policy_available('web accessibility')
 
def test_location_region(driver):
    home = HomePage()
    home.nav_to_epam_page()
    home.check_region_location()

def test_search_func(driver):
    home = HomePage()
    home.nav_to_epam_page()
    home.check_search_results()

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

def test_download_file(driver):
    expected_file = 'EPAM_Corporate_Overview_Q3_october.pdf'
    dwnl = Download()
    dwnl.nav_to_epam_about_page()
    dwnl.download_the_file(expected_file)
   