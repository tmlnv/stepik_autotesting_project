from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class BasketPage(BasePage):

    def check_no_items_in_basket(self, locator):
        return self.browser.find_element(*locator)

    def check_items_in_basket(self, locator, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False

        return True
