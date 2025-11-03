import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.order_page import OrderPage


@pytest.fixture(scope='function')
def create_driver():
    driver = webdriver.Firefox()
    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def home_page(create_driver):
    """
    Открывает главную страницу
    """
    page = HomePage(create_driver)
    return page


@pytest.fixture(scope='function')
def order_page(create_driver):
    """
    Открывает страницу заказа
    """
    page = OrderPage(create_driver)
    return page
