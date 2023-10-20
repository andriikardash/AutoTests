from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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