from src.pages.main_page import MainPage
from src.locators.main_locators import MainLocators
from src.utilitis.urls import Urls


class TestMain:

    url = Urls.base_url

    def test_add_to_cart_from_catalog(self, browser):
        page = MainPage(browser, self.url)
        assert page.verify_add_to_cart_from_catalog()

    def test_redirect_to_product_page(self, browser):
        page = MainPage(browser, self.url)
        page.login()
        assert page.verify_redirect_to_product_page()
        assert page.is_product_url()

    def test_remove_product_from_catalog(self, browser):
        page = MainPage(browser, self.url)
        page.login()
        assert page.verify_remove_product_from_catalog()

    def test_add_to_cart_from_product(self, browser):
        page = MainPage(browser, self.url)
        page.login()
        assert page.verify_add_to_cart_from_product()

    def test_remove_product_from_product(self, browser):
        page = MainPage(browser, self.url)
        page.login()
        assert page.verify_remove_product_from_product()

