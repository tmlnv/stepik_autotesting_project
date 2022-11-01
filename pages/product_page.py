from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import ProductPageLocators, MainPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.click(ProductPageLocators.ADD_TO_BASKET_BUTTON)

    def should_be_message_about_adding(self):
        self.is_element_present(*ProductPageLocators.PRODUCT_NAME)
        self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text.split('has')[0][:-1]
        assert product_name == message

    def should_be_message_basket_total(self):
        self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL)
        self.is_element_present(*ProductPageLocators.PRODUCT_PRICE)
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == message_basket_total

    def should_not_be_success_message(self):
        assert self.is_not_element_present(), \
            "Success message is presented"

    def is_not_element_present(self, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(
                ProductPageLocators.SUCCESS_MESSAGE))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE))
        except TimeoutException:
            return False

        return True

    def should_be_disappeared(self):
        assert self.is_disappeared()

    def click_basket_button(self):
        self.click(MainPageLocators.BASKET_BUTTON)
