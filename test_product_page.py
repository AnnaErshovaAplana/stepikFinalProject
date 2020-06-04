import pytest
from .pages.product_page import ProductPage
import time

# помечаем упавший тест xfail
#@pytest.mark.parametrize('offer_number', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
# прогоняем ссылки с параметром offer_number от 0 до 10 и помечаем ссылку 7 xfail
#@pytest.mark.parametrize('offer_number', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason="bugged link")) for i in range(10)])
#def test_guest_can_add_product_to_basket(browser, offer_number):
#    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)  # инициализируем Page Object,передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()
    page.should_be_product_title_in_cart()
    page.should_be_product_price_in_cart()
    time.sleep(5)


@pytest.mark.xfail(reason="message remains after adding product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)  # инициализируем Page Object,передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart() # Добавляем товар в корзину
    page.should_not_be_message_on_product_added_to_cart() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)  # инициализируем Page Object,передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_not_be_message_on_product_added_to_cart()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object,передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()  # Добавляем товар в корзину
    page.should_message_on_product_added_to_cart_disappear()    #Проверяем, что нет сообщения об успехе с помощью is_disappeared
