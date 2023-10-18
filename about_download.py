from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class Download():
    def __init__(self):
        download_directory = "C:\J"
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": download_directory}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        
    def nav_to_epam_about_page(self):
        self.driver.get('https://www.epam.com/about')
        time.sleep(2)
        
    def download_the_file(self, expected_file):
        download_directory = "C:\J"
        self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[5]/section/div[2]/div/div/div[1]/div/div[3]/div/a').click()
        time.sleep(3)
        assert expected_file in os.listdir(download_directory)