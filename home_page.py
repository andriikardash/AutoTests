from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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
