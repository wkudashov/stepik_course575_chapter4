from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url and self.is_element_present(*LoginPageLocators.LOGIN_LINK), \
               "Login link is not presented on Login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
               "Login form is not presented on Login"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), \
               "Registration form is not presented on Login"

    def register_new_user(self, email, password):
        reg_email = WebDriverWait(self.browser, 5).until(
            e_c.presence_of_element_located(LoginPageLocators.REGISTRATION_EMAIL)
        )
        reg_email.send_keys(email)
        reg_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        reg_password1.send_keys(password)
        reg_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        reg_password2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        reg_button.click()
