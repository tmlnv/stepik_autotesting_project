from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

    def should_be_login_form(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        assert all((login_email, login_password, login_button)), "Could not find login form"

    def should_be_register_form(self):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        reg_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        reg_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        assert all((reg_email, reg_password1, reg_password2, reg_button)), "Could not find register form"

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        reg_email.clear()
        reg_email.send_keys(email)
        reg_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        reg_password1.clear()
        reg_password1.send_keys(password)
        reg_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        reg_password2.clear()
        reg_password2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_button.click()
