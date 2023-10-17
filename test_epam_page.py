from statistics import harmonic_mean
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
    

def test_change_language_to_ukr(driver):
    ukr_url = 'https://careers.epam.ua/'
    home = HomePage()
    home.nav_to_epam_page()
    home.go_to_urk_page()
    url = home.get_current_url()
    assert ukr_url == url


def test_policies_list(driver):
    home = HomePage()
    home.nav_to_epam_page()
    home.check_policies_link_available()

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


# Test 9 does not work. Have no clue
"""
download_directory = "C:/Users/Andrii_Kardash/Downloads"
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_directory}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.epam.com/about')

download_file = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[5]/section/div[2]/div/div/div[1]/div/div[3]/div/a').click()
"""