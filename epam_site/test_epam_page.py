from search import Search
from region import Region
from home_page import HomePage
from contact import ContactPage
from download import Download
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

# Check that allow to switch location list by region
def test_location_region(driver):
    home = Region()
    home.nav_to_epam_page()
    home.check_americas_location_list()
    home.accept_cookie_policy()
    home.switch_to_emea_region()
    home.check_emea_location_list()
    home.switch_to_apac_region()
    home.check_apac_location_list()

# Check the search function
def test_search_func(driver):
    home = Search()
    home.nav_to_epam_page()
    home.go_to_search_mode()
    home.accept_cookie_policy() 
    home.fill_in_search('ai')
    home.check_search_result('ai')

# Check form's fields validation
def test_contact_required_fields(driver):  
    contact = ContactPage()    
    contact.nav_to_epam_contact_page()
    assert contact.check_first_name_is_required()
    assert contact.check_last_name_is_required()
    assert contact.check_email_is_required()
    assert contact.check_phone_is_required()
    assert contact.check_drop_down_is_required()
    assert contact.check_policy_is_required()
    
# Check that the Company logo on the header lead to the main page
def test_company_logo(driver):
    epam_url = 'https://www.epam.com/'    
    about = ContactPage()
    about.nav_to_epam_about_page()
    about.click_epam_logo_button()
    url = about.get_current_url()
    assert epam_url == url

# Check that allows to download report 
def test_download_file(driver):
    expected_file = 'EPAM_Corporate_Overview_Q3_october.pdf'
    dwnl = Download()
    dwnl.nav_to_epam_about_page()
    dwnl.download_the_file(expected_file)
