from base import BaseView
from selenium.webdriver.common.by import By

class Region(BaseView):    
    LOCATION_LIST = (By.XPATH, '//*[@class="tabs-23__ul-wrapper"]')
    CANADA = (By.XPATH, '//img[@alt="Canada"]')
    COLOMBIA = (By.XPATH, '//img[@alt="Colombia"]')
    D_REPUBLIC = (By.XPATH, '//img[@alt="Dominican Republic"]')
    MEXICO = (By.XPATH, '//img[@alt="Mexico"]')
    EMEA = (By.XPATH, '//a[@data-item="1"]')
    ARMENIA = (By.XPATH, '//img[@alt="Armenia"]')
    AUSTRIA = (By.XPATH, '//img[@alt="Austria"]')
    BELARUS = (By.XPATH, '//img[@alt="Belarus"]')
    BELGIUM = (By.XPATH, '//img[@alt="Belgium"]')
    APAC = (By.XPATH, '//a[@data-item="2"]')
    AUSTRALIA =  (By.XPATH, '//img[@alt="Australia"]')
    CHINA = (By.XPATH, '//img[@alt="China"]')
    HONG_KONG = (By.XPATH, '//img[@alt="Hong Kong SAR"]')
    INDIA = (By.XPATH, '//img[@alt="India"]')
    
    def check_americas_location_list(self):
        canada = self.wait_for(self.CANADA)
        colombia = self.find(self.COLOMBIA)
        d_republic = self.find(self.D_REPUBLIC)
        mexico = self.find(self.MEXICO)
        assert canada and colombia and d_republic and mexico
        
    def switch_to_emea_region(self):
        self.find(self.EMEA).click()
        
    def check_emea_location_list(self):
        armenia = self.wait_for(self.ARMENIA)
        austria = self.find(self.AUSTRIA)
        belarus = self.find(self.BELARUS)
        belgium = self.find(self.BELGIUM)
        assert armenia and austria and belarus and belgium
        
    def switch_to_apac_region(self):
        self.find(self.APAC).click()
        
    def check_apac_location_list(self):
        australia = self.wait_for(self.AUSTRALIA)
        china = self.find(self.CHINA)
        hong_Kong = self.find(self.HONG_KONG)
        india = self.find(self.INDIA)
        assert australia and china and hong_Kong and india