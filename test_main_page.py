from .pages.main_page import MainPage
from .pages.locators import MainPageLocators, BasketPageLocators
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.click(MainPageLocators.BASKET_BUTTON)
    basket_page = BasketPage(browser, link)
    assert basket_page.check_no_items_in_basket(locator=BasketPageLocators.CONTINUE_SHOPPING_BUTTON)
    assert 'Your basket is empty' in browser.page_source
    assert not basket_page.check_items_in_basket(locator=BasketPageLocators.ORDER_TOTAL)
