from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BaseView(object):
    
    ACCEPT_COOKIE = (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
   

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        
    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def nav_to_epam_page(self):
        self.driver.get('https://www.epam.com/')
        
    def get_title(self):
        return self.driver.title
    
    def accept_cookie_policy(self):
        self.find(self.ACCEPT_COOKIE).click()
        
    def get_current_url(self):
        time.sleep(1)
        return self.driver.current_url
