from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest


@pytest.mark.parametrize('offer_num',
                         [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged')), *range(8, 10)])
def test_add_to_cart(browser, offer_num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart(locator=ProductPageLocators.ADD_TO_CART_BUTTON)
    page.solve_quiz_and_get_code()
    product_name = page.should_be_message_about_adding(locator1=ProductPageLocators.PRODUCT_NAME,
                                                       locator2=ProductPageLocators.MESSAGE_ABOUT_ADDING)[0]
    message = page.should_be_message_about_adding(locator1=ProductPageLocators.PRODUCT_NAME,
                                                  locator2=ProductPageLocators.MESSAGE_ABOUT_ADDING)[1].split('has')[0][:-1]
    assert product_name == message
    message_basket_total = page.should_be_message_basket_total(locator1=ProductPageLocators.MESSAGE_BASKET_TOTAL,
                                                               locator2=ProductPageLocators.PRODUCT_PRICE)[0]
    product_price = page.should_be_message_basket_total(locator1=ProductPageLocators.MESSAGE_BASKET_TOTAL,
                                                        locator2=ProductPageLocators.PRODUCT_PRICE)[1]
    assert product_price == message_basket_total
