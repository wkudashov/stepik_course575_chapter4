import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="chose the page language for testing")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="choose testing browser: chrome or firefox")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    
    if browser_name == "chrome":
        c_options = webdriver.chrome.options.Options()
        # c_options.add_argument("--headless")
        c_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        c_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        
    elif browser_name == "firefox":
        f_options = webdriver.firefox.options.Options()
        # f_options.headless = True
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=f_options, firefox_profile=profile)
    
    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")
    
    yield browser
    
    browser.quit()
