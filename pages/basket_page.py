from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_items_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_CART_MESSAGE), "Something was found in the Basket"

    def should_visible_message_of_empty_cart(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTINESS_MESSAGE),  "There is no message of empty cart, maybe it isn't empty"
