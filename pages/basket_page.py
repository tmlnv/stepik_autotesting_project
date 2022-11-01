from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_no_items_in_basket(self):
        assert self.browser.find_element(*BasketPageLocators.CONTINUE_SHOPPING_BUTTON)

    def check_items_in_basket(self, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(BasketPageLocators.ORDER_TOTAL))
        except TimeoutException:
            return False

        return True

    def should_not_be_items_in_basket(self):
        assert not self.check_items_in_basket()

    def check_empty_basket_text(self):
        assert 'Your basket is empty' in self.browser.page_source
