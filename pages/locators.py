from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    TO_BASKET = (By.CSS_SELECTOR, 'div.basket-mini a')

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, '#messages div.alert-info strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1)')

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner .basket-title")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
