import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time

#помечаем упавший тест xfail
#@pytest.mark.parametrize('offer_number', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
#прогоняем ссылки с параметром offer_number от 0 до 10 и помечаем ссылку 7 xfail
#@pytest.mark.parametrize('offer_number', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason="bugged link")) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, offer_number):
   link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)  # инициализируем Page Object,передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()
    page.should_be_product_title_in_cart()
    page.should_be_product_price_in_cart()
    time.sleep(5)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object,передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_not_be_message_on_product_added_to_cart()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.xfail(reason="message remains after adding product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)  # инициализируем Page Object,передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart() # Добавляем товар в корзину
    page.should_not_be_message_on_product_added_to_cart() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object,передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()  # Добавляем товар в корзину
    page.should_message_on_product_added_to_cart_disappear()    #Проверяем, что нет сообщения об успехе с помощью is_disappeared

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser,link)
    page.should_be_login_url()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Переходит в корзину по кнопке в шапке
    page.go_to_basket()
    page = BasketPage(browser, link)
    # Ожидаем, что в корзине нет товаров
    page.should_be_no_products_in_cart()
    # Ожидаем, что есть текст о том что корзина пуста
    page.should_be_empty_cart_message()


class TestUserAddToBasketFromProductPage():
    # фикстуру setup. В этой функции нужно:
    # открыть страницу регистрации
    # зарегистрировать нового пользователя
    # проверить, что пользователь залогинен
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
        login_page.open()
        login_page.register_new_user(email, password)
        current_url = str(browser.current_url)
        login_page_with_user = LoginPage(browser, current_url)
        login_page_with_user.check_if_logged_in()
        login_page_with_user.should_not_be_login_url()



    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  # инициализируем Page Object,передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_to_cart()
        page.should_be_product_title_in_cart()
        page.should_be_product_price_in_cart()
        time.sleep(5)


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  # инициализируем Page Object,передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_not_be_message_on_product_added_to_cart()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
