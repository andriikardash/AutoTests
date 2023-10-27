from selenium.webdriver.common.by import By
from base import Base
import time

class Wishlist(Base):
    GIFT_CARDS = (By.PARTIAL_LINK_TEXT, 'Gift')
    GIFT_CARD_25 = (By.PARTIAL_LINK_TEXT, '$25 Virtual')
    RECIPIENT_EMAIL = (By.CSS_SELECTOR, '#giftcard_2_RecipientEmail')
    RECIPIENT_NAME = (By.CSS_SELECTOR, '#giftcard_2_RecipientName')
    ADD_WISHLIST_BUTTON = (By.CSS_SELECTOR, '#add-to-wishlist-button-2')
    POP_UP = (By.XPATH, '//p[@class="content"]')
    ADD_TO_CARD_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button-2')
    SHOPPING_CART = (By.PARTIAL_LINK_TEXT, 'Shopping cart')
    REMOVE_CHECKBOX = (By.XPATH, '//*[@name="removefromcart"]')
    UPDATE_SHOPPING_CART = (By.NAME, 'updatecart')
    EMPTY_CART = (By.CLASS_NAME, 'page-body')
    POLICY_CHECKBOX = (By.ID, 'termsofservice')
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    CONTINUE_BUTTON_BILLING_ADDRESS = (By.CSS_SELECTOR, '.button-1.new-address-next-step-button')
    CONTINUE_BUTTON_PAYMENT_METHOD = (By.XPATH, "//input[@class='button-1 payment-method-next-step-button']")
    CONTINUE_BUTTON_PAYMENT_INFO = (By.CSS_SELECTOR, '.button-1.payment-info-next-step-button')
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, '.button-1.confirm-order-next-step-button')
    ORDER_COMPLETED = (By.CSS_SELECTOR, '.order-completed')

    def nav_to_gift_cards(self):
        self.wait_for(self.GIFT_CARDS).click()
        self.wait_for(self.GIFT_CARD_25).click()
        
    def fill_in_recipient_name(self, name):
        self.find(self.RECIPIENT_NAME).send_keys(name)
        
    def fill_in_recipient_email(self, email):
        self.find(self.RECIPIENT_EMAIL).send_keys(email)
        
    def click_on_add_wishlist_button(self):
        self.wait_for(self.ADD_WISHLIST_BUTTON).click()
        
    def check_pop_up(self, expected):
        res = self.wait_for(self.POP_UP).text
        assert expected == res
        
    def click_on_add_to_card_button(self):
        self.wait_for(self.ADD_TO_CARD_BUTTON).click()
        time.sleep(1)
        
    def nav_to_shopping_cart(self):
        time.sleep(1)
        self.wait_for(self.SHOPPING_CART).click()
        
    def click_on_remove_checkbox(self):
        self.wait_for(self.REMOVE_CHECKBOX).click()
        
    def click_on_update_shopping_cart(self):
        self.find(self.UPDATE_SHOPPING_CART).click()

    def check_shopping_cart_is_empty(self, expected):
        res = self.wait_for(self.EMPTY_CART).text
        assert expected == res
        
    def click_on_policy_checkbox(self):
        self.wait_for(self.POLICY_CHECKBOX).click()
        
    def click_on_checkout_button(self):
        self.find(self.CHECKOUT_BUTTON).click()
        
    def click_on_confirm_continue_billing_address_button(self):
        self.wait_for(self.CONTINUE_BUTTON_BILLING_ADDRESS).click()
        
    def click_on_confirm_continue_payment_method_button(self):
        time.sleep(1)
        self.wait_for(self.CONTINUE_BUTTON_PAYMENT_METHOD).click()
            
    def click_on_confirm_continue_payment_info_button(self):
        time.sleep(1)
        self.wait_for(self.CONTINUE_BUTTON_PAYMENT_INFO).click()
        
    def click_on_confirm_order_button(self):
        time.sleep(1)
        self.wait_for(self.CONFIRM_ORDER_BUTTON).click()
            
    def check_order_completed(self, expected):
        res = self.wait_for(self.ORDER_COMPLETED).text
        assert expected in res