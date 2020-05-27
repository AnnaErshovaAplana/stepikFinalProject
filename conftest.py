import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Сначала добавляем в файле conftest обработчик опции в функции pytest_addoption,
# затем напишем фикстуру, которая будет обрабатывать переданные в опции данные.
# теперь при запуске файла с тестами нужно будет прописывать параметр --language(зык интерфейса)
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help="Choose language")


# создаем фикстуру с областью действия в функциях
@pytest.fixture(scope="function")
# создаем функцию для использования браузера для переиспользования с указанием конкретного языка интерфейса
def browser(request):
    # создаем функцию для передачи различных языков интерфейса через командную строку,
    # а также для возможности открывать тесты в разных браузерах
    # получаем из командной строки параметры для запуска browser_name и language
    browser_name = request.config.getoption("browser_name")
    if request.config.getoption("language") is None:
        language = 'en'
    else:
        language = request.config.getoption("language")

    if browser_name == "chrome" or None:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
