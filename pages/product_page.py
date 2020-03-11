from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators

class ProductPage(BasePage):

    def order_product(self):
        link = self.browser.find_element(
            *ProductPageLocators.ORDER_BUTTON)
        link.click()

    def name_should_be_equal(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        alert_product_name = self.browser.find_element(
            *ProductPageLocators.ALERT_PRODUCT_NAME).text
        print(product_name,alert_product_name)
        assert product_name == alert_product_name,\
                'Product name is not equal to added product'
    
    def price_should_be_equal(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        alert_product_price = self.browser.find_element(
            *ProductPageLocators.ALERT_PRODUCT_PRICE).text
        print(product_price,alert_product_price)
        assert product_price == alert_product_price,\
                'Product prece is not equal to cart added price'
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not dissapeared, but should"