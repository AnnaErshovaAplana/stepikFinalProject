from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_products_in_cart(self):
        assert self.is_element_not_present(*BasketPageLocators.CART_PRODUCT_SUM), 'basket is not empty'


    def should_be_empty_cart_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE), "No message on empty cart"
