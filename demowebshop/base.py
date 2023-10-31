from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import data

class Base(object):
    FIRST_NAME = (By.CSS_SELECTOR, '#FirstName')
    LAST_NAME = (By.CSS_SELECTOR, '#LastName')
    EMAIL = (By.CSS_SELECTOR, '#Email')
    PASSWORD = (By.CSS_SELECTOR, '#Password')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#ConfirmPassword')
    LOGIN_BUTTON = (By.CLASS_NAME, 'ico-login')
    SUBMIT_LOGIN_BUTTON = (By.XPATH, '//input[@type="submit" and @value="Log in"]')
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        
    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def go_to_main_page(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        time.sleep(1)
        
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
        
    def log_in_as_a_user(self):
        self.nav_to_login_page()
        self.fill_in_email(data.existed_user_email)
        self.fill_in_password(data.password)
        self.confirm_login()
        
    def nav_to_login_page(self):
        self.wait_for(self.LOGIN_BUTTON).click()
        
    def confirm_login(self):
        self.find(self.SUBMIT_LOGIN_BUTTON).click()