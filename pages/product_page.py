from .base_page import BasePage
from .locators import ProductPageLocators
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as e_c
# from selenium.common.exceptions import TimeoutException


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
               "Add to basket button is not presented on Product"

    def should_be_item_in_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ITEM_ADDED), \
               "Item in basket message is not presented on Product"

    def should_not_be_item_in_basket_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ITEM_ADDED), \
               "Item in basket message is presented, but shouldn't on Product"

    def should_disappeared_item_in_basket_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ITEM_ADDED), \
               "Item in basket message is not disappeared on Product"

    def should_be_item_name_in_message(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        message_text = self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_ADDED).text
        print('ITEM->', item_name, 'MESSAGE ->', message_text)
        assert item_name == message_text, \
               "Item name is not presented in item_in_basket message on Product"

    def should_be_basket_cost_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_COST), \
               "Item in basket message is not presented on Product"

    def should_be_equal_item_and_basket_costs(self):
        item_cost = self.browser.find_element(*ProductPageLocators.ITEM_COST).text
        basket_cost = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_COST).text
        assert item_cost == basket_cost, \
            "Item cost is not equal to basket cost in message on Product"

    # def waiting_for_text(self):
    #     try:
    #         WebDriverWait(self.browser, 10).until(e_c.text_to_be_present_in_element(ProductPageLocators.MESSAGE_ITEM_ADDED, 'Coders at Work'))
    #     except TimeoutException:
    #         return False
    #     return True
