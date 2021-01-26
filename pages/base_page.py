from selenium.webdriver import Remote


class BasePage:

    def __init__(self, browser: Remote, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
