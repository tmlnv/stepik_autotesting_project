from .base_page import BasePage


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
