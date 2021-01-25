import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="chose the page language for testing")


@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()

    # options.add_argument("--headless")
    # запуск браузера в режиме работы без отрисовки интерфейса

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

