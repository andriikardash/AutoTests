from home import HomePage
import time
from selenium.webdriver.common.by import By
import data

"""
def test_registration_new_user(driver):
    expected_result = 'Your registration completed'
    home = HomePage()
    home.go_to_main_page()
    home.nav_to_register()
    home.fill_in_first_name(data.firstname)
    home.fill_in_last_name(data.lastname)
    home.fill_in_email(data.new_user_email)
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
    
    
def test_computers_group(driver):
    home = HomePage()
    home.go_to_main_page()
    home.click_on_computers_group()
    desktops = home.get_desktops_subgroup()
    assert "Desktops" == desktops
    notebooks = home.get_notebooks_subgroup()
    assert "Notebooks" == notebooks
    accessories = home.get_accessories_subgroup()
    assert "Accessories" == accessories
    

    #need to think how to get correct data and sort it
def test_sorting_items(driver):
    home = HomePage()
    home.go_to_main_page()
    home.nav_to_books_page()
    initial_sort_items = home.get_products_titles()
    expected_sorting = sorted(initial_sort_items)
    home.sort_by_drop_down(1)
    actual_sorting = home.get_products_titles()
    assert expected_sorting == actual_sorting 
    
    
def test_display_per_page(driver):
    home = HomePage()
    home.go_to_main_page()
    home.nav_to_shoes_page()
    time.sleep(2)
    el = driver.find_elements(By.XPATH, '//h2[@class="product-title"]')
    count = len(el)
    assert 8 == count
    
    
def test_add_to_wishlist(driver):
    home = HomePage()
    expected = 'The product has been added to your wishlist'
    home.go_to_main_page()
    home.log_in_as_a_user()
    home.nav_to_gift_cards()
    home.fill_in_recipient_name(data.recipient_name)
    home.fill_in_recipient_email(data.recipient_email)
    home.click_on_add_wishlist_button()
    home.check_pop_up(expected)
    
def test_add_to_card(driver):
    home = HomePage()
    expected = 'The product has been added to your shopping cart'
    home.go_to_main_page()
    home.log_in_as_a_user()
    home.nav_to_gift_cards()
    home.fill_in_recipient_name(data.recipient_name)
    home.fill_in_recipient_email(data.recipient_email)
    home.click_on_add_to_card_button()
    home.check_pop_up(expected)
    
    """