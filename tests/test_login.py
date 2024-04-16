from src.pages.login_page import LoginPage
from src.utilitis.urls import Urls


class TestLogin():

    url = Urls.base_url

    def test_login(self, browser):

        page = LoginPage(browser, self.url)

        page.open()
        page.login()