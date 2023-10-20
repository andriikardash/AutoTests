from home import HomePage
import time
import data


def test_registration_new_user(driver):
    expected_result = 'Your registration completed'
    home = HomePage()
    home.go_to_main_page()
    home.nav_to_register()
    home.fill_in_first_name(data.firstname)
    home.fill_in_last_name(data.lastname)
    home.fill_in_email(data.user_email)
    home.fill_in_password(data.password)
    home.fill_in_confirm_password(data.password)
    home.click_confirm_register_button()
    home.check_successfull_registration(expected_result)


def test_user_login(driver):
    home = HomePage()
    home.go_to_main_page()
    home.nav_to_login_page()
    home.fill_in_email(data.user_email)
    home.fill_in_password(data.password)
    home.confirm_login()
    home.check_user_account(data.user_email)