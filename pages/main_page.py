# импорт базового класса BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By
# импорт класса с локаторами
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # пример. добавляем принятие всплывающих сообщений, чтобы тесты не ломались при переходе между страницами
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_be_login_link(self):
        #  * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
