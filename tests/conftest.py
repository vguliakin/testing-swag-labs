import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
