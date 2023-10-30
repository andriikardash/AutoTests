from selenium.webdriver.common.by import By
from base import Base
from selenium.webdriver.support.ui import Select

class Display(Base):
    SHOES = (By.PARTIAL_LINK_TEXT, 'Apparel')
    DISPLAY_DROP_DOWN = (By.ID, 'products-pagesize')
    
    def nav_to_shoes_page(self):
        self.wait_for(self.SHOES).click()
        
    def select_display_option(self, option):
        drop_down = Select(self.wait_for(self.DISPLAY_DROP_DOWN))
        drop_down.select_by_index(option)
        
    def check_options_displayed(self, expected):
        products = self.driver.find_elements(By.XPATH, "//h2[contains(@class, 'product-title')]")
        num_of_elements = len(products)
        assert num_of_elements == expected