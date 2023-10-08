from selenium import webdriver

class HomePage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        

    def nav_to_epam_page(self):
        self.driver.get('https://www.epam.com/')
    
    def get_title(self):
        return self.driver.title
        
