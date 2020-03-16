from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from random import choice
import pytest
import time

@pytest.mark.solve_quiz
def test_order_product_w_ny_offer(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.order_product()
    page.solve_quiz_and_get_code()
    page.name_should_be_equal()
    page.price_should_be_equal()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="bugged_link")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])


def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.order_product()
    page.solve_quiz_and_get_code()
    page.name_should_be_equal()
    page.price_should_be_equal()

@pytest.mark.xfail(reason="Test should fail by design")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.order_product()
    page.should_not_be_success_message()

@pytest.mark.cant_see_success_message
def test_guest_cant_see_success_message(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Test should fail by design")
def test_message_disappeared_after_adding_product_to_basket(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.order_product()
    page.should_dissapear_success_message()

@pytest.mark.need_review_custom_scenarios
@pytest.mark.should_see_login_link
def test_guest_should_see_login_link_on_product_page(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
@pytest.mark.can_go_to_login_page
def test_guest_can_go_to_login_page_from_product_page(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
@pytest.mark.basket_is_empty
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, product_link):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_be_empty_message()   


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, product_link):
        page = ProductPage(browser, product_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = email = str(time.time()) + "@fakemail.org"
        def generate_pass(nletters:int,ndigits:int):
            '''Generates password with nletters and ndigids'''
            letters = [chr(i) for i in range(ord('a'),ord('z')+1)]
            digits = [str(i) for i in range (10)]
            return ''.join([choice(letters) for l in range(nletters)]) + \
            ''.join([choice(digits) for d in range(ndigits)])
        password = generate_pass(5,5)
        login_page.register_new_user(email,password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser, product_link):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, product_link):
        page = ProductPage(browser, product_link)
        page.open()
        page.order_product()
        page.name_should_be_equal()
        page.price_should_be_equal()