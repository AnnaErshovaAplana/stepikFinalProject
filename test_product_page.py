import pytest
from pages.base_page import BasePage
from .pages.product_page import ProductPage
import time


#@pytest.mark.parametrize('offer_number', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
# прогоняем ссылки с параметром offer_number от 0 до 10 и помечаем ссылку 7 xfail
@pytest.mark.parametrize('offer_number', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason="bugged link")) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    page = ProductPage(browser,link)  # инициализируем Page Object,передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()
    page.should_be_product_title_in_cart()
    page.should_be_product_price_in_cart()
    time.sleep(5)
