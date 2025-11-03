import allure
import pytest
from locators.home_page_locators import *


class TestNavigation:

    @pytest.mark.parametrize('logo_name, logo_locator', [('samokat', HomePageLocators.SAMOKAT_LOGO),
                                                         ('yandex', HomePageLocators.YANDEX_LOGO)])
    @allure.title('Проверка навигации по клику на логотипы')
    def test_navigation(self, order_page, home_page, logo_name, logo_locator):
        order_page.open_page(order_page.url)
        order_page.click(logo_locator)
        home_page.check_logo_go_to_url(logo_name)
