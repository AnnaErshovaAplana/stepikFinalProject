from pages.base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        # получаем результат математического выражения в консоль и отправляем его во всплыв окне
        BasePage.solve_quiz_and_get_code(self)
        self.browser.implicitly_wait(5)


    def should_be_product_title_in_cart(self):
        product_title_on_page_text = self.browser.find_element(*ProductPageLocators.PRODUCT_PRODUCT_PAGE_TITLE).text
        product_title_in_cart_text = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TITLE).text
        #  Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        assert product_title_on_page_text == product_title_in_cart_text


    def should_be_product_price_in_cart(self):
        product_price_on_page_text = self.browser.find_element(*ProductPageLocators.PRODUCT_PRODUCT_PAGE_PRICE).text
        product_price_in_cart_text = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_PRICE).text
        #  Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара
        assert product_price_on_page_text == product_price_in_cart_text
