from selenium import webdriver
from selenium.webdriver.common.by import By
from home_page import HomePage
from base import BaseView

class ContactPage(BaseView):    
    LOGO_BTN = (By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div/div/header/div/div/a[1]')
    FIRST_NAME = (By.NAME, 'user_first_name')
    LAST_NAME = (By.NAME, 'user_last_name')
    EMAIL = (By.NAME, 'user_email')
    PHONE = (By.NAME, 'user_phone')
    DROP_DOWN = (By.NAME, 'user_comment_how_hear_about')
    POLICY_CHECKBOX = (By.CLASS_NAME, 'checkbox-custom')
    
    def check_first_name_is_required(self):
        self.first_name = self.find(self.FIRST_NAME)
        self.is_first_name_required = 'required' in self.first_name.get_attribute("outerHTML")
        return self.is_first_name_required
    
    def check_last_name_is_required(self):
        self.last_name = self.find(self.LAST_NAME)
        self.is_last_name_required = 'required' in self.last_name.get_attribute("outerHTML")
        return self.is_last_name_required
    
    def check_email_is_required(self):
        self.email = self.find(self.EMAIL)
        self.is_email_required = 'required' in self.email.get_attribute("outerHTML")
        return self.is_email_required
    
    def check_phone_is_required(self):
        self.phone = self.find(self.PHONE)
        self.is_phone_required = 'required' in self.phone.get_attribute("outerHTML")
        return self.is_phone_required
    
    def check_drop_down_is_required(self):
        self.drop_down = self.find(self.DROP_DOWN)
        self.is_drop_down_required = 'required' in self.drop_down.get_attribute("outerHTML")
        return self.is_drop_down_required
    
    def check_policy_is_required(self):
        self.policies_checkbox = self.find(self.POLICY_CHECKBOX)
        self.is_policies_checkbox_required = 'required' in self.policies_checkbox.get_attribute("outerHTML")
        return self.is_policies_checkbox_required
 
    def nav_to_epam_contact_page(self):
        self.driver.get('https://www.epam.com/about/who-we-are/contact')
        
    def nav_to_epam_about_page(self):
        self.driver.get('https://www.epam.com/about')
        
    def click_epam_logo_button(self):
        self.wait_for(self.LOGO_BTN).click()
