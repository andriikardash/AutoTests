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
    #POLICIES = (By.XPATH, '//*[@class="policies-links-wrapper"]')

      
    def get_background_color(self):
        html = self.wait_for(self.HTML_HEADER)
        return html.value_of_css_property('background-color')
    
    def click_on_dark_light_toggle(self):
        self.wait_for(self.DARK_LIGHT_TOGGLE).click()
        
    def go_to_ukr_page(self):
        self.wait_for(self.GLOBAL_BTN).click()
        self.accept_cookie_policy()
        self.wait_for(self.UKR_LANG_BTN).click()
        time.sleep(2)

    def check_region_location(self):
        canada = self.driver.find_element(By.XPATH, '//img[@alt="Canada"]')
        colombia = self.driver.find_element(By.XPATH, '//img[@alt="Colombia"]')
        d_Republic = self.driver.find_element(By.XPATH, '//img[@alt="Dominican Republic"]')
        mexico = self.driver.find_element(By.XPATH, '//img[@alt="Mexico"]')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        self.driver.find_element(By.XPATH, '//a[@data-item="1"]').click()
        armenia = self.driver.find_element(By.XPATH, '//img[@alt="Armenia"]')
        austria = self.driver.find_element(By.XPATH, '//img[@alt="Austria"]')
        belarus = self.driver.find_element(By.XPATH, '//img[@alt="Belarus"]')
        belgium = self.driver.find_element(By.XPATH, '//img[@alt="Belgium"]')
        self.driver.find_element(By.XPATH, '//a[@data-item="2"]').click()
        australia = self.driver.find_element(By.XPATH, '//img[@alt="Australia"]')
        china = self.driver.find_element(By.XPATH, '//img[@alt="China"]')
        hong_Kong = self.driver.find_element(By.XPATH, '//img[@alt="Hong Kong SAR"]')
        india = self.driver.find_element(By.XPATH, '//img[@alt="India"]')
        assert canada and colombia and d_Republic and mexico and armenia and austria and belarus and belgium and australia and china and hong_Kong and india


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