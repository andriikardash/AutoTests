from selenium.webdriver.common.by import By
from base import Base

class Login(Base):
    USER_ACCOUNT = (By.XPATH, '//a[@class="account"]')

    def nav_to_login_page(self):
        self.wait_for(self.LOGIN_BUTTON).click()
        
    def check_user_account(self, user_email):
        result = self.wait_for(self.USER_ACCOUNT).text
        assert result == user_email
        
