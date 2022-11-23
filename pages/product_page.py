from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_item_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()

    def should_be_added_proper_item(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_TO_ADD_DESCRIPTION).text ==\
               self.browser.find_element(*ProductPageLocators.ADDED_ITEM_DESCRIPTION).text, "items names doesn't equal"

    def should_be_added_item_with_proper_price(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_TO_ADD_PRICE).text ==\
               self.browser.find_element(*ProductPageLocators.ADDED_ITEM_PRICE).text, "items price doesn't equal"
