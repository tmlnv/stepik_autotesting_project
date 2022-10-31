from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
# from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators, MainPageLocators, BasketPageLocators
import pytest
import faker


@pytest.mark.parametrize('offer_num',
                         [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged')), *range(8, 10)])
def test_guest_can_add_to_basket(browser, offer_num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket(locator=ProductPageLocators.ADD_TO_BASKET_BUTTON)
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


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket(locator=ProductPageLocators.ADD_TO_BASKET_BUTTON)
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(locator=ProductPageLocators.SUCCESS_MESSAGE)


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(locator=ProductPageLocators.SUCCESS_MESSAGE)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket(locator=ProductPageLocators.ADD_TO_BASKET_BUTTON)

    assert page.is_disappeared(locator=ProductPageLocators.SUCCESS_MESSAGE)


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click(MainPageLocators.BASKET_BUTTON)
    basket_page = BasketPage(browser, link)
    assert basket_page.check_no_items_in_basket(locator=BasketPageLocators.CONTINUE_SHOPPING_BUTTON)
    assert 'Your basket is empty' in browser.page_source
    assert not basket_page.check_items_in_basket(locator=BasketPageLocators.ORDER_TOTAL)


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        f = faker.Faker()
        email = f.email()
        password = f.pystr()
        login_page = LoginPage(browser, url=link)
        login_page.open()
        login_page.register_new_user(email=email, password=password)
        assert browser.find_element(*BasketPageLocators.USER_ICON)

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(locator=ProductPageLocators.SUCCESS_MESSAGE)

    def test_user_can_add_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket(locator=ProductPageLocators.ADD_TO_BASKET_BUTTON)
        page.solve_quiz_and_get_code()
        product_name = page.should_be_message_about_adding(locator1=ProductPageLocators.PRODUCT_NAME,
                                                           locator2=ProductPageLocators.MESSAGE_ABOUT_ADDING)[0]
        message = page.should_be_message_about_adding(locator1=ProductPageLocators.PRODUCT_NAME,
                                                      locator2=ProductPageLocators.MESSAGE_ABOUT_ADDING)[1].split(
            'has')[0][:-1]
        assert product_name == message
        message_basket_total = page.should_be_message_basket_total(locator1=ProductPageLocators.MESSAGE_BASKET_TOTAL,
                                                                   locator2=ProductPageLocators.PRODUCT_PRICE)[0]
        product_price = page.should_be_message_basket_total(locator1=ProductPageLocators.MESSAGE_BASKET_TOTAL,
                                                            locator2=ProductPageLocators.PRODUCT_PRICE)[1]
        assert product_price == message_basket_total
