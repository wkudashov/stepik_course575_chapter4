import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


# @pytest.mark.parametrize('offer_num', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
# def test_guest_can_add_product_to_basket(browser, offer_num):
#     link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{str(offer_num)}'
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_basket_button()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_item_in_basket_message()
#     page.should_be_item_name_in_message()
#     page.should_be_basket_cost_message()
#     page.should_be_equal_item_and_basket_costs()


@pytest.mark.xfail(strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.should_not_be_item_in_basket_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_item_in_basket_message()


@pytest.mark.xfail(strict=True)
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.should_be_item_name_in_message()
    page.should_disappeared_item_in_basket_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
