from selenium.common import NoSuchElementException

from .page import Page
from framework.locators import LOGIN_AND_PASSWORD_FIELDS, LOGIN_BUTTON, PERFORM_LOGIN_BUTTON, ADD_HUB_BUTTON


class LoginPage(Page):
    def fill_user_data(self, login: str, password: str) -> None:
        login_button = self.find_element(LOGIN_BUTTON)
        self.click_element(login_button)
        self.driver.implicitly_wait(5)
        login_field, password_field = self.find_element(LOGIN_AND_PASSWORD_FIELDS, multiple=True)
        self.fill_input_field(login_field, login)
        self.fill_input_field(password_field, password)
        perform_login_button = self.find_element(PERFORM_LOGIN_BUTTON)
        self.click_element(perform_login_button)

    def check_if_login_is_success(self):
        try:
            self.driver.implicitly_wait(7)
            return self.find_element(ADD_HUB_BUTTON).is_displayed()
        except NoSuchElementException:
            return False
