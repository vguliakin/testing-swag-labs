import pytest

from src.data.data_test import DataTest
from src.locators.cart_locators import CartLocators
from src.locators.login_locators import LoginLocators
from src.locators.main_locators import MainLocators
from src.pages.cart_page import CartPage
from src.utilitis.urls import Urls


class TestCart:

    url = Urls.cart_page_url

    def test_complete_order(self, browser):
        page = CartPage(browser, self.url)
        page.add_item_to_cart()
        assert page.verify_complete_order()

    @pytest.mark.parametrize("test_data", DataTest.info_data)
    def test_ordering_with_wrong_data(self, browser, test_data):
        page = CartPage(browser, self.url)
        assert page.verify_ordering_with_wrong_data(test_data)

