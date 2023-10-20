from home import HomePage
import time
import data

"""
def test_registration_new_user(driver):
    expected_result = 'Your registration completed'
    home = HomePage()
    home.go_to_main_page()
    home.nav_to_register()
    home.fill_in_first_name("Andrii")
    home.fill_in_last_name("Test")
    home.fill_in_email("test+15@gmail.com")
    home.fill_in_password("Welcome1")
    home.fill_in_confirm_password("Welcome1")
    home.click_confirm_register_button()
    home.check_successfull_registration(expected_result)
"""

def test_user_login(driver):
    #user_email = 'test+10@gmail.com'
    home = HomePage()
    home.go_to_main_page()
    home.nav_to_login_page()
    home.fill_in_email(data.user_email)
    #home.fill_in_password("Welcome1")
    home.fill_in_password(data.password)
    home.confirm_login()
    home.check_user_account 