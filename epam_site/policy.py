from base import BaseView
from selenium.webdriver.common.by import By

class Policy(BaseView):
    POLICIES = (By.XPATH, '//*[@class="policies-links-wrapper"]')
    
    def check_policy_available(self, policy):
        current_policy = self.wait_for(self.POLICIES).text.lower()
        assert policy in current_policy