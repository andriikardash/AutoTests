from home import HomePage
from selenium.webdriver.common.by import By

REGISTRATION_BUTTON = (By.XPATH, '//a[@class="ico-register"]')

class Register(HomePage):
    def nav_to_register(self):
        self.find(self.REGISTRATION_BUTTON).click()