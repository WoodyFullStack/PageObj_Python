from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "current url is not login page url"

        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form doesn't found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form doesn't found"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS_AGAIN_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
