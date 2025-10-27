import allure
import pytest
from faker import Faker
from datetime import date, timedelta
import random
from locators.home_page_locators import *


class TestOrder:

    @pytest.mark.parametrize('button', [HomePageLocators.BUTTON_ORDER_HEADER, HomePageLocators.BUTTON_ORDER_FINISH])
    @allure.title('Проверка успешного оформления заказа')
    def test_order_success_notification(self, home_page, order_page, button):
        fake = Faker('ru_RU')
        name = fake.first_name()
        last_name = fake.last_name()
        address = fake.city()
        station = 'Черкизовская'
        phone = fake.msisdn()
        tommorrow = date.today() + timedelta(days=1)
        tommorrow_date = tommorrow.strftime("%d/%m/%Y")
        term = random.choice(['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток'])
        home_page.open_page(home_page.url)
        home_page.go_to_order(button)
        order_page.fill_in_order_required_fields_form_1(name, last_name, address, station, phone)
        order_page.fill_in_order_required_fields_form_2(tommorrow_date, term)
        order_page.confirm_order_and_check_modal()
