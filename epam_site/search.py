from base import BaseView
from selenium.webdriver.common.by import By
import time

class Search(BaseView):    
    SEARCH_BTN = (By.XPATH, "//*[contains(@class, 'search-icon') and contains(@class, 'dark-iconheader-search__search-icon')]")
    SEARCH_FIELD = (By.XPATH, '//*[@id="new_form_search"]')
    FIND_BTN = (By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[3]/div/div/form/div[1]/button')
    SEARCH_RESULT = (By.XPATH, '//*[@class="search-results__counter"]')
    
    def go_to_search_mode(self):
        self.wait_for(self.SEARCH_BTN).click()
        time.sleep(1)
        
    def fill_in_search(self, search):
        self.find(self.SEARCH_FIELD).send_keys(search)
        self.find(self.FIND_BTN).click()
        
    def check_search_result(self, result):
        actual = self.wait_for(self.SEARCH_RESULT).text.lower()
        assert result in actual