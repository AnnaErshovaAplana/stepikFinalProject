from selenium.webdriver.common.by import By
# Каждый класс будет соответствовать каждому классу PageObject


class MainPageLocators():
    # селектор — это пара: как искать и что искать.
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")