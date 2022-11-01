from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def click_on_basket(self):
        self.click(MainPageLocators.BASKET_BUTTON)
