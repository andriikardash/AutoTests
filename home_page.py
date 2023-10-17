from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
        

    def nav_to_epam_page(self):
        self.driver.get('https://www.epam.com/')
    
    def get_title(self):
        return self.driver.title
        
    def check_header_background_color(self):
        html = self.driver.find_element(By.CSS_SELECTOR, 'header')
        initial_color = html.value_of_css_property('background-color')
        dark_light_toggle = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/header/div/div/section/div/div").click()
        time.sleep(2)
        changed_color = html.value_of_css_property('background-color')
        assert initial_color != changed_color
        

    def check_policies_link_available(self):
        investors = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[3]/div[1]/footer/div/div/div[1]/div[2]/div/ul[1]/li[1]/a')
        open_source = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[3]/div[1]/footer/div/div/div[1]/div[2]/div/ul[1]/li[2]/a')
        privacy_policy = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[3]/div[1]/footer/div/div/div[1]/div[2]/div/ul[1]/li[3]/a')
        cookie_policy = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[3]/div[1]/footer/div/div/div[1]/div[2]/div/ul[2]/li[1]/a')
        applicant_privacy_notice = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[3]/div[1]/footer/div/div/div[1]/div[2]/div/ul[2]/li[2]/a')
        web_accessibility = self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[3]/div[1]/footer/div/div/div[1]/div[2]/div/ul[2]/li[3]/a')
        assert investors and open_source and privacy_policy and cookie_policy and applicant_privacy_notice and web_accessibility 

    def go_to_urk_page(self):
        
        self.driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[2]/div/div/button').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@class="location-selector__link" and @lang="uk"]').click()
        time.sleep(2)
        
    def get_current_url(self):
        self.new_url = self.driver.current_url
        return self.new_url

    def accept_coolie_policy(self):
        self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
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