from selenium.webdriver.common.by import By
from base import Base

class Register(Base):
    REGISTRATION_BUTTON = (By.XPATH, '//a[@class="ico-register"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register-button')
    SUCCESSFULL_REGISTRATION = (By.CSS_SELECTOR, '.result')
    
    def nav_to_register(self):
        self.find(self.REGISTRATION_BUTTON).click()
        
    def click_confirm_register_button(self):
        self.find(self.REGISTER_BUTTON).click()
        
    def check_successfull_registration(self, expected_result):
        result = self.wait_for(self.SUCCESSFULL_REGISTRATION).text
        assert result == expected_result