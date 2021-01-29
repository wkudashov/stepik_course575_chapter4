import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.firefox.options import Options as FOptions


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="chose the page language for testing")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="choose testing browser: chrome or firefox")
    parser.addoption('--head', action='store', default="on",
                     help="choose browser head mode: on or off (for head or headless)")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    visibility_mode = request.config.getoption("head")
    
    if browser_name == "chrome":
        c_options = COptions()
        if visibility_mode == 'off':
            c_options.add_argument("--headless")
        c_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        c_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=c_options)

    elif browser_name == "firefox":
        f_options = FOptions()
        if visibility_mode == 'off':
            f_options.headless = True
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=f_options, firefox_profile=profile)

    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")

    yield browser
    
    browser.quit()
