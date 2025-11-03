import allure
import pytest
from locators.home_page_locators import *
from helpers.generate_test_data_create_order import get_test_data_required_fields


class TestOrder:

    @pytest.mark.parametrize('button', [HomePageLocators.BUTTON_ORDER_HEADER, HomePageLocators.BUTTON_ORDER_FINISH])
    @allure.title('Проверка успешного оформления заказа')
    def test_order_success_notification(self, home_page, order_page, button):
        name, last_name, address, station, phone, tomorrow_date, term = get_test_data_required_fields()
        home_page.open_page(home_page.url)
        home_page.go_to_order(button)
        order_page.fill_in_order_required_fields_form_1(name, last_name, address, station, phone)
        order_page.fill_in_order_required_fields_form_2(tomorrow_date, term)
        order_page.confirm_order_and_check_modal()
