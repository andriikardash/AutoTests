from selenium import webdriver
from selenium.webdriver.common.by import By
from home_page import HomePage

class ContactPage(HomePage):
       
    def is_contact_fields_required(self):
        self.first_name = self.driver.find_element(By.NAME, 'user_first_name')
        self.is_first_name_required = 'required' in self.first_name.get_attribute("outerHTML")
        self.last_name = self.driver.find_element(By.NAME, 'user_last_name')
        self.email = self.driver.find_element(By.NAME, 'user_email')
        self.phone = self.driver.find_element(By.NAME, 'user_phone')
        self.drop_down = self.driver.find_element(By.NAME, 'user_comment_how_hear_about')
        self.policies_checkbox = self.driver.find_element(By.CLASS_NAME, 'checkbox-custom')
        self.is_last_name_required = 'required' in self.last_name.get_attribute("outerHTML")
        self.is_email_required = 'required' in self.email.get_attribute("outerHTML")
        self.is_phone_required = 'required' in self.phone.get_attribute("outerHTML")
        self.is_drop_down_required = 'required' in self.drop_down.get_attribute("outerHTML")
        self.is_policies_checkbox_required = 'required' in self.policies_checkbox.get_attribute("outerHTML")
        assert self.is_first_name_required and self.is_last_name_required
        

    def nav_to_epam_contact_page(self):
        self.driver.get('https://www.epam.com/about/who-we-are/contact')
        
    def nav_to_epam_about_page(self):
        self.driver.get('https://www.epam.com/about')
        
    def click_epam_logo_button(self):
        self.logo_btn = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div/div/header/div/div/a[1]').click()
        
    def get_current_url(self):
        self.new_url = self.driver.current_url
        return self.new_url