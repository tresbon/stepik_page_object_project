from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # Инициализация класса
    page = MainPage(browser, link)   
    # Открыть
    page.open()             
    # Перейти на страницу логина
    page.go_to_login_page()          

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()