from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/apparel-shoes")
time.sleep(2)


el = driver.find_elements(By.XPATH, '//h2[@class="product-title"]')
count = len(el)
print(count)
assert 8 == count





driver.quit()