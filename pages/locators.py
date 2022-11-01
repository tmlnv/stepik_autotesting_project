from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, '[href="/en-gb/basket/"]')


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[name='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, '[href="/en-gb/"]')
    ORDER_TOTAL = (By.CLASS_NAME, 'total')
