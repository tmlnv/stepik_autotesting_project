from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    # def test_guest_can_go_to_login_page(self):
    #     link = "http://selenium1py.pythonanywhere.com"
    #     page = MainPage(self.browser, link)
    #     page.open()
    #     login_page = page.go_to_login_page()
    #     login_page.should_be_login_page()

    def test_guest_can_go_to_login_page(self):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(self.browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(self.browser, self.browser.current_url)
        login_page.should_be_login_page()
