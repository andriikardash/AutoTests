from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base import BaseView


class HomePage(BaseView):
    HTML_HEADER = (By.CSS_SELECTOR, 'header')
    DARK_LIGHT_TOGGLE = (By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/section/div')
    GLOBAL_BTN = (By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[2]/div/div/button')
    UKR_LANG_BTN = (By.XPATH, '//*[@class="location-selector__link" and @lang="uk"]')
    

      
    def get_background_color(self):
        html = self.wait_for(self.HTML_HEADER)
        return html.value_of_css_property('background-color')
    
    def click_on_dark_light_toggle(self):
        self.wait_for(self.DARK_LIGHT_TOGGLE).click()
        
    def go_to_ukr_page(self):
        self.wait_for(self.GLOBAL_BTN).click()
        self.accept_cookie_policy()
        self.wait_for(self.UKR_LANG_BTN).click()


    def check_search_results(self):
        self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[3]/div/button/span[1]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        time.sleep(1)
        search_field = self.driver.find_element(By.XPATH, '//*[@id="new_form_search"]').send_keys('ai')
        self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[3]/div/div/form/div[1]/button').click()
        search_actual = self.driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/section/div[2]/div[4]/section/h2').text
        search_expected = 'RESULTS FOR "AI"'
        assert search_expected in search_actual