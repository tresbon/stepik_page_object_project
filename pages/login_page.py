from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.current_url

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM),\
            "Login link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM),\
            "Login link is not presented"
    
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        pass1_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        pass1_input.send_keys(password)
        pass2_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        pass2_input.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()