# импорт базового класса BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By
# импорт класса с локаторами
from .login_page import LoginPage


class MainPage(BasePage):
    # заглужка класса
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
