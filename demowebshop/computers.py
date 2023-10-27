from selenium.webdriver.common.by import By
from base import Base

class Computers(Base):
    COMPUTERS = (By.LINK_TEXT, 'Computers')
    DESKTOPS = (By.PARTIAL_LINK_TEXT, 'Desktops')
    NOTEBOOKS = (By.PARTIAL_LINK_TEXT, 'Notebooks')
    ACCESSORIES = (By.PARTIAL_LINK_TEXT, 'Accessories')

    def click_on_computers_group(self):
        self.wait_for(self.COMPUTERS).click()
        
    def get_desktops_subgroup(self):
        return self.wait_for(self.DESKTOPS).text
    
    def get_notebooks_subgroup(self):
        return self.find(self.NOTEBOOKS).text

    def get_accessories_subgroup(self):
        return self.find(self.ACCESSORIES).text