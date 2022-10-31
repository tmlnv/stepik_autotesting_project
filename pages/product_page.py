from .base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def add_to_cart(self, locator):
        self.click(locator)

    def should_be_message_about_adding(self, locator1, locator2):
        if self.is_element_present(*locator1) and self.is_element_present(*locator2):
            product_name = self.browser.find_element(*locator1).text
            message = self.browser.find_element(*locator2).text
            return product_name, message
        return 'No elements'

    def should_be_message_basket_total(self, locator1, locator2):
        if self.is_element_present(*locator1) and self.is_element_present(*locator2):
            message_basket_total = self.browser.find_element(*locator1).text
            product_price = self.browser.find_element(*locator2).text
            return message_basket_total, product_price
        return "No message"

    def should_not_be_success_message(self, locator):
        assert not self.is_element_present(*locator), \
            "Success message is presented"

    def is_not_element_present(self,locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True
