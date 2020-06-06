import math
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException  # для метода получения кода для ответа на задание
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import BasketPageLocators



# Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы.
# В ней мы опишем вспомогательные методы для работы с драйвером.


class BasePage():
    # конструктор — метод, который вызывается, когда мы создаем объект.
    # Конструктор объявляется ключевым словом __init__.
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    # метод проверки наличия элемента, в котором будем перехватывать исключение
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    # метод для проверки того, что элемента еще нет на странице
    def is_element_not_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False


    # метод для проверки того, что элемент исчез со страницы
    def has_element_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout,1,TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


# реализуйте соответствующий метод для перехода в корзину
    def go_to_basket(self):
        basket_link = self.browser.find_element(*BasketPageLocators.CART_BUTTON)
        basket_link.click()


    # метод перехода на страницу логина
    def go_to_login_page(self):
        # проскроллим страницу вверх, чтобы повилась кнопка логина
        self.browser.execute_script("window.scrollTo(0,0);")
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        # пример. добавляем принятие всплывающих сообщений, чтобы тесты не ломались при переходе между страницами
        # alert = self.browser.switch_to.alert
        # alert.accept()


    # метод открывает нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)


    # метод проверки, что ссылка на логи имеется
    def should_be_login_link(self):
        #  * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    # метод для получени проверочного кода для заполнения ответа на сайте
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

