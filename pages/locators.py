from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn[href*='basket']")
    USER_ICON = (By.CLASS_NAME, "icon-user")


class LoginPageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.NAME, "registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    ITEM_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    MESSAGE_ITEM_ADDED = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner strong")
    ITEM_COST = (By.CSS_SELECTOR, "#content_inner .price_color")
    MESSAGE_BASKET_COST = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner p:nth-child(1) strong")


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items .row")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
