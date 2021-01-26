import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('offer_num', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, offer_num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{str(offer_num)}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_item_in_basket_message()
    page.should_be_item_name_in_message()
    page.should_be_basket_cost_message()
    page.should_be_equal_item_and_basket_costs()
