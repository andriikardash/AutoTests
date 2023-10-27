from selenium.webdriver.common.by import By
from base import BaseView


class HomePage(BaseView):
    HTML_HEADER = (By.CSS_SELECTOR, 'header')
    DARK_LIGHT_TOGGLE = (By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/section/div')
    GLOBAL_BTN = (By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[2]/div/div/button')
    UKR_LANG_BTN = (By.XPATH, '//*[@class="location-selector__link" and @lang="uk"]')

    def get_background_color(self):
        html = self.wait_for(self.HTML_HEADER)
        return html.value_of_css_property('background-color')
    
    def click_on_dark_light_toggle(self):
        self.wait_for(self.DARK_LIGHT_TOGGLE).click()
        
    def go_to_ukr_page(self):
        self.wait_for(self.GLOBAL_BTN).click()
        self.accept_cookie_policy()
        self.wait_for(self.UKR_LANG_BTN).click()
