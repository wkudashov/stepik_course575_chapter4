import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(e_c.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(e_c.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(e_c.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        try:
            WebDriverWait(self.browser, 5).until(e_c.alert_is_present())
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
        except TimeoutException:
            print("No first alert presented")
        # try:
        #     WebDriverWait(self.browser, 5).until(e_c.alert_is_present())
        #     alert = self.browser.switch_to.alert
        #     alert_text = alert.text.split()
        #     print(f"Your code: {alert_text[-1]}")
        #     alert.accept()
        # except TimeoutException:
        #     print("No second alert presented")
