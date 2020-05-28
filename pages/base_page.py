from selenium.common.exceptions import NoSuchElementException

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