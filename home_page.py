from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HomePage:
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