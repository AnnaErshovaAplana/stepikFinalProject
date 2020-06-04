from selenium.webdriver.common.by import By
# Каждый класс будет соответствовать каждому классу PageObject


class MainPageLocators():
    # селектор — это пара: как искать и что искать.
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRODUCT_PAGE_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRODUCT_PAGE_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_ADDED_TITLE = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    PRODUCT_ADDED_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PRODUCT_ADD_TO_CARD_MESSAGE = (By.CSS_SELECTOR, '.alert-info .alertinner')
