from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_TO_ADD_DESCRIPTION = (By.XPATH, '//article/div[1]/div[2]/h1')
    ITEM_TO_ADD_PRICE = (By.XPATH, '//article/div[1]/div[2]/p[@class = "price_color"]')
    ADDED_ITEM_DESCRIPTION = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    ADDED_ITEM_PRICE = (By.XPATH, "//div[@id='messages']/div/div/p/strong")
