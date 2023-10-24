from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import data

class HomePage(object):
    
    REGISTRATION_BUTTON = (By.XPATH, '//a[@class="ico-register"]')
    FIRST_NAME = (By.CSS_SELECTOR, '#FirstName')
    LAST_NAME = (By.CSS_SELECTOR, '#LastName')
    EMAIL = (By.CSS_SELECTOR, '#Email')
    PASSWORD = (By.CSS_SELECTOR, '#Password')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#ConfirmPassword')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register-button')
    SUCCESSFULL_REGISTRATION = (By.CSS_SELECTOR, '.result')
    LOGIN_BUTTON = (By.CLASS_NAME, 'ico-login')
    SUBMIT_LOGIN_BUTTON = (By.XPATH, '//input[@type="submit" and @value="Log in"]')
    USER_ACCOUNT = (By.XPATH, '//a[@class="account"]')
    COMPUTERS = (By.LINK_TEXT, 'Computers')
    COMPUTERS_SUBGROUP = (By.XPATH, "//a[@href='/computers']/following-sibling::ul[@class='sublist']")
    DESKTOPS = (By.PARTIAL_LINK_TEXT, 'Desktops')
    NOTEBOOKS = (By.PARTIAL_LINK_TEXT, 'Notebooks')
    ACCESSORIES = (By.PARTIAL_LINK_TEXT, 'Accessories')
    BOOKS = (By.PARTIAL_LINK_TEXT, 'Books')
    SORT_BY = (By.CSS_SELECTOR, '#products-orderby')
    PRODUCTS_TITLE = (By.XPATH, '//h2[@class="product-title"]')
    APPAREL = (By.PARTIAL_LINK_TEXT, 'Apparel')
    GIFT_CARDS = (By.PARTIAL_LINK_TEXT, 'Gift')
    GIFT_CARD_25 = (By.PARTIAL_LINK_TEXT, '$25 Virtual')
    RECIPIENT_EMAIL = (By.CSS_SELECTOR, '#giftcard_2_RecipientEmail')
    RECIPIENT_NAME = (By.CSS_SELECTOR, '#giftcard_2_RecipientName')
    ADD_WISHLIST_BUTTON = (By.CSS_SELECTOR, '#add-to-wishlist-button-2')
    POP_UP = (By.XPATH, '//p[@class="content"]')
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button-2')
    SHOPPING_CART = (By.PARTIAL_LINK_TEXT, 'Shopping cart')
    REMOVE_CHECKBOX = (By.XPATH, '//*[@name="removefromcart"]')
    UPDATE_SHOPPING_CART = (By.NAME, 'updatecart')
    EMPTY_CART = (By.CLASS_NAME, 'page-body')
    POLICY_CHECKBOX = (By.ID, 'termsofservice')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    COUNTRY_CHECKBOX = (By.ID, 'BillingNewAddress_CountryId')
    CITY = (By.ID, 'BillingNewAddress_City')
    ADDRESS1 = (By.ID, 'BillingNewAddress_Address1')
    ZIP_CODE = (By.ID, 'BillingNewAddress_ZipPostalCode')
    PHONE_NUMBER = (By.ID, 'BillingNewAddress_PhoneNumber')
    CONTINUE_BUTTON_BILLING_ADDRESS = (By.CSS_SELECTOR, '.button-1.new-address-next-step-button')
    CONTINUE_BUTTON_PAYMENT_METHOD = (By.XPATH, "/html/body/div[5]/div[1]/div[4]/div/div/div[2]/ol/li[2]/div[2]/div/input")
    CONTINUE_BUTTON_PAYMENT_INFO = (By.CSS_SELECTOR, '.button-1.payment-info-next-step-button')
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, '.button-1.confirm-order-next-step-button')
    ORDER_COMPLETED = (By.CSS_SELECTOR, '.order-completed')


    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        
    def go_to_main_page(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        time.sleep(1)
        
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def nav_to_register(self):
        self.find(self.REGISTRATION_BUTTON).click()
        
    def fill_in_first_name(self, firstName):
        self.find(self.FIRST_NAME).send_keys(firstName)
        
    def fill_in_last_name(self, lastName):
        self.find(self.LAST_NAME).send_keys(lastName)

    def fill_in_email(self, email):
        self.find(self.EMAIL).send_keys(email)
        
    def fill_in_password(self, password):
        self.find(self.PASSWORD).send_keys(password)
        
    def fill_in_confirm_password(self, confirm_password):
        self.find(self.CONFIRM_PASSWORD).send_keys(confirm_password)
        
    def click_confirm_register_button(self):
        self.find(self.REGISTER_BUTTON).click()
        
    def check_successfull_registration(self, expected_result):
        result = self.wait_for(self.SUCCESSFULL_REGISTRATION).text
        assert result == expected_result
        

    def nav_to_login_page(self):
        self.wait_for(self.LOGIN_BUTTON).click()
        
    def confirm_login(self):
        self.find(self.SUBMIT_LOGIN_BUTTON).click()
        
    def check_user_account(self, user_email):
        result = self.wait_for(self.USER_ACCOUNT).text
        assert result == user_email
        
    def click_on_computers_group(self):
        self.wait_for(self.COMPUTERS).click()
        
        
    def get_desktops_subgroup(self):
        return self.wait_for(self.DESKTOPS).text
    
    def get_notebooks_subgroup(self):
        return self.wait_for(self.NOTEBOOKS).text

    def get_accessories_subgroup(self):
        return self.wait_for(self.ACCESSORIES).text
    
    def nav_to_books_page(self):
        self.wait_for(self.BOOKS).click()
        
    def sort_by_drop_down(self, sort_option):
        sorting = Select(self.wait_for(self.SORT_BY))
        sorting.select_by_index(sort_option)
        
    def get_products_titles(self):
        return self.wait_for(self.PRODUCTS_TITLE).text
    
    def nav_to_shoes_page(self):
        self.wait_for(self.APPAREL).click()
        
    def check_number_of_products_in_page(self):
        self.elements = self.driver.find_elements(self.PRODUCTS_TITLE)
        #self.num = len(self.elements)
        #assert 8 == self.num 
        return len(self.elements)
        

    def log_in_as_a_user(self):
        self.nav_to_login_page()
        self.fill_in_email(data.existed_user_email)
        self.fill_in_password(data.password)
        self.confirm_login()
        
    def nav_to_gift_cards(self):
        self.wait_for(self.GIFT_CARDS).click()
        self.wait_for(self.GIFT_CARD_25).click()
        

    def fill_in_recipient_name(self, name):
        self.find(self.RECIPIENT_NAME).send_keys(name)
        
    def fill_in_recipient_email(self, email):
        self.find(self.RECIPIENT_EMAIL).send_keys(email)
        
    def click_on_add_wishlist_button(self):
        self.wait_for(self.ADD_WISHLIST_BUTTON).click()
        
    def check_pop_up(self, expected):
        res = self.wait_for(self.POP_UP).text
        assert expected == res
        
    def click_on_add_to_card_button(self):
        self.wait_for(self.ADD_TO_CARD_BUTTON).click()
        
    def nav_to_shopping_cart(self):
        self.wait_for(self.SHOPPING_CART).click()
        
    def click_on_remove_checkbox(self):
        self.wait_for(self.REMOVE_CHECKBOX).click()
        
    def click_on_update_shopping_cart(self):
        self.find(self.UPDATE_SHOPPING_CART).click()

    def check_shopping_cart_is_empty(self, expected):
        res = self.wait_for(self.EMPTY_CART).text
        assert expected == res
        
    def click_on_policy_checkbox(self):
        self.wait_for(self.POLICY_CHECKBOX).click()
        
    def click_on_checkout_button(self):
        self.find(self.CHECKOUT_BUTTON).click()
        
    def select_country(self, option):
        country = Select(self.wait_for(self.COUNTRY_CHECKBOX))
        country.select_by_index(option)
        
    def fill_in_city(self, city):
        self.find(self.CITY).send_keys(city)
        
    def fill_in_address1(self, address1):
        self.find(self.ADDRESS1).send_keys(address1)
        
    def fill_in_zip(self, zip):
        self.find(self.ZIP_CODE).send_keys(zip)
        
    def fill_in_phone(self, phone):
        self.find(self.PHONE_NUMBER).send_keys(phone)
        
    def click_on_confirm_continue_billing_address_button(self):
        self.wait_for(self.CONTINUE_BUTTON_BILLING_ADDRESS).click()
        
    def click_on_confirm_continue_payment_method_button(self):
        self.wait_for(self.CONTINUE_BUTTON_PAYMENT_METHOD).click()
            
    def click_on_confirm_continue_payment_info_button(self):
        self.wait_for(self.CONTINUE_BUTTON_PAYMENT_INFO).click()
        
    def click_on_confirm_order_button(self):
        self.wait_for(self.CONFIRM_ORDER_BUTTON).click()
            
    def check_order_completed(self, expected):
        res = self.wait_for(self.ORDER_COMPLETED).text
        assert expected in res