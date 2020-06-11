import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = str(self.browser.current_url) # current_url Gets the URL of the current page.
        assert current_url.find("login") != -1, "URL does not contain word 'login'"

    def should_not_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = str(self.browser.current_url) # current_url Gets the URL of the current page.
        assert current_url.find("login") == -1, "URL contains word 'login', user is not logged in"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"


    def register_new_user(self, email, password, ):  # принимает две строки и регистрирует пользователя.
        enter_email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        enter_email_field.send_keys(email)
        enter_password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        enter_password_field.send_keys(password)
        enter_password_repeat_field = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT_FIELD)
        enter_password_repeat_field.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
        time.sleep(10)

    def check_if_logged_in(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_SUCCESS_BOX), "Success box is not presented, user is not logged in"
        assert self.browser.find_element(*LoginPageLocators.LOG_OUT_BUTTON), "Log out button is not presented, user is not logged in"
