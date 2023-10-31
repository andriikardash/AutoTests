from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='chrome')

@pytest.fixture
def platform(request):
    plat = request.config.getoption('platform').lower()
    if plat not in ['chrome', 'firefox']:
        raise ValueError('value must be chrome or firefox')
    return plat

@pytest.fixture
def driver(platform):
    driver = webdriver.Chrome() if platform == 'chrome' else webdriver.Firefox()
    yield driver
    driver.quit()
