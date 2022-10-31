from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.base_page import BasePage


def test_add_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart(locator=ProductPageLocators.ADD_TO_CART_BUTTON)
    page.solve_quiz_and_get_code()
    product_name = page.should_be_message_about_adding(locator1=ProductPageLocators.PRODUCT_NAME,
                                                       locator2=ProductPageLocators.MESSAGE_ABOUT_ADDING)[0]
    message = page.should_be_message_about_adding(locator1=ProductPageLocators.PRODUCT_NAME,
                                                  locator2=ProductPageLocators.MESSAGE_ABOUT_ADDING)[1]
    assert product_name in message
    message_basket_total = page.should_be_message_basket_total(locator1=ProductPageLocators.MESSAGE_BASKET_TOTAL,
                                               locator2=ProductPageLocators.PRODUCT_PRICE)[0]
    product_price = page.should_be_message_basket_total(locator1=ProductPageLocators.MESSAGE_BASKET_TOTAL,
                                               locator2=ProductPageLocators.PRODUCT_PRICE)[1]
    assert product_price in message_basket_total
