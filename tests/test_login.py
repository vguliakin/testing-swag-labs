from src.pages.login_page import LoginPage
from src.utilitis.urls import Urls
from src.locators.login_locators import LoginLocators
from src.data.auth_data import AuthData


class TestLogin():
    url = Urls()

    def test_login_with_valid_credentials(self, browser):
        page = LoginPage(browser, self.url.base_url)

        page.open()
        page.login()

        assert page.get_current_url() == self.url.main_page_url
        assert page.verify_login_success()

    def test_login_with_empty_username(self, browser):
        page = LoginPage(browser, self.url.base_url)

        page.open()

        assert page.verify_login_with_empty_username()

    def test_login_with_empty_password(self, browser):
        page = LoginPage(browser, self.url.base_url)

        page.open()

        assert page.verify_login_with_empty_password()

    def test_login_with_wrong_credentials(self, browser):
        page = LoginPage(browser, self.url.base_url)

        page.open()

        assert page.verify_login_with_wrong_credentials()
