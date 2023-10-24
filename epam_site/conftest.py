from tkinter import BROWSE
from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    browser = 'chrome'
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    yield driver
    driver.quit()