from .base_page import BasePage

class MainPage(BasePage):
    def go_to_login_page(self):
   link = self.browser.find_elementBy.CSS_SELECTOR, "#login_link")
   link.click() 