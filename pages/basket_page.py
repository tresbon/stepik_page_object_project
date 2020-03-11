from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_EMPTY), \
                'Basket is not empty but should'

    def should_be_empty_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_MESSAGE),\
            "Empty message is not present"