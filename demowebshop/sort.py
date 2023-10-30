from selenium.webdriver.common.by import By
from base import Base
import time
from selenium.webdriver.support.ui import Select

class Sort(Base):
    BOOKS = (By.PARTIAL_LINK_TEXT, 'Books')
    SORT_BY_DROP_DOWN = (By.ID, 'products-orderby')
    
    def nav_to_books_page(self):
        self.wait_for(self.BOOKS).click()
        
    def select_sorting_option(self, sort_option):
        drop_down = Select(self.wait_for(self.SORT_BY_DROP_DOWN))
        drop_down.select_by_index(sort_option)
        
    def check_sorting_A_Z(self):
        products = self.driver.find_elements(By.XPATH, "//h2[contains(@class, 'product-title')]")
        text = [element.text for element in products]
        is_sorted = all(text[i] <= text[i+1] for i in range(len(text) -1))
        assert is_sorted, "Elements are not sorted A-Z"

    def check_sorting_Z_A(self):
        products = self.driver.find_elements(By.XPATH, "//h2[contains(@class, 'product-title')]")
        text = [element.text for element in products]
        sorting = sorted(text, reverse = True)
        is_sorted = sorting
        assert is_sorted, "Elemenets are not sorted Z-A"