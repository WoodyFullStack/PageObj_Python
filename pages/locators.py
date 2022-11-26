from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//div/span[@class = 'btn-group']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_EMPTINESS_MESSAGE = (By.XPATH, "//div[@class='content']/div[@id='content_inner']/p")
    ITEMS_IN_CART_MESSAGE = (By.XPATH, "//div[@class='content']/div[@id='content_inner']/div")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_PASS_INPUT = (By.ID, "id_registration-password1")
    REGISTER_PASS_AGAIN_INPUT = (By.ID, "id_registration-password2")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_BUTTON = (By.XPATH, '//form[@id="register_form"]/button')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_TO_ADD_DESCRIPTION = (By.XPATH, '//article/div[1]/div[2]/h1')
    ITEM_TO_ADD_PRICE = (By.XPATH, '//article/div[1]/div[2]/p[@class = "price_color"]')
    ADDED_ITEM_DESCRIPTION = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    ADDED_ITEM_PRICE = (By.XPATH, "//div[@id='messages']/div/div/p/strong")
