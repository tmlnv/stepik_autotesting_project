from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.TAG_NAME, 'login-username')
    LOGIN_PASSWORD = (By.TAG_NAME, 'login-password')
    LOGIN_BUTTON = (By.TAG_NAME, 'login_submit')
    REGISTER_EMAIL = (By.TAG_NAME, 'registration-username')
    REGISTER_PASSWORD1 = (By.TAG_NAME, 'registration-password1')
    REGISTER_PASSWORD2 = (By.TAG_NAME, 'registration-password2')
    REGISTER_BUTTON = (By.TAG_NAME, 'registration_submit')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
