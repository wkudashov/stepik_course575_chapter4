import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
# from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class BasePage:

    # def __init__(self, browser, url, timeout=10):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    # def is_element_present(self, how, what):
    #     try:
    #         self.browser.find_element(how, what)
    #     except NoSuchElementException:
    #         return False
    #     return True

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 10).until(e_c.presence_of_element_located((how, what)))
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
