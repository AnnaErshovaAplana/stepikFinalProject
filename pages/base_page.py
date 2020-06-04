import math
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException  # для метода получения кода для ответа на задание
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Для начала сделаем базовую страницу, от которой будут унаследованы все остальные классы.
# В ней мы опишем вспомогательные методы для работы с драйвером.


class BasePage():
    # конструктор — метод, который вызывается, когда мы создаем объект.
    # Конструктор объявляется ключевым словом __init__.
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # реализуем метод проверки наличия элемента, в котором будем перехватывать исключение
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    # Теперь добавим еще один метод open.
    # Он должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)


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
