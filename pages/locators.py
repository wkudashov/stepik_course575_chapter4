from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    ITEM_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    MESSAGE_ITEM_ADDED = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner strong")
    ITEM_COST = (By.CSS_SELECTOR, "#content_inner .price_color")
    MESSAGE_BASKET_COST = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner p:nth-child(1) strong")
