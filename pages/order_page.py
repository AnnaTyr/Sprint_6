import allure
from pages.base_page import BasePage
from locators.order_page_locators import *


class OrderPage(BasePage):

    url = 'https://qa-scooter.praktikum-services.ru/order'

    @allure.step('Заполняем обязательные поля формы заказа на первой странице')
    def fill_in_order_required_fields_form_1(self, name: str, last_name: str, address: str, station: str, phone: str):
        self.find_element(OrderPageLocators.INPUT_NAME).send_keys(name)
        self.find_element(OrderPageLocators.INPUT_LAST_NAME).send_keys(last_name)
        self.find_element(OrderPageLocators.INPUT_ADDRESS).send_keys(address)
        self.find_element(OrderPageLocators.INPUT_STATION).send_keys(station)
        self.click([By.XPATH, f'//div[@class="select-search__select"]//*[text()="{station}"]'])
        self.find_element(OrderPageLocators.INPUT_PHONE).send_keys(phone)
        self.click(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполняем обязательные поля формы заказа на второй странице')
    def fill_in_order_required_fields_form_2(self, date: str, term: str):
        self.find_element(OrderPageLocators.INPUT_DATE).send_keys(date)
        self.click(OrderPageLocators.DATE_SELECTED)
        self.select_option_in_dropdown(OrderPageLocators.DROPDOWN_TERM, term)
        self.click(OrderPageLocators.BUTTON_ORDER)

    def select_option_in_dropdown(self, dropdown: list, option_text: str):
        self.click(dropdown)
        self.is_visible(OrderPageLocators.DROPDOWN_OPTION)
        options = self.find_elements(OrderPageLocators.DROPDOWN_OPTION)
        for option in options:
            if option.text == option_text:
                option.click()
                return
        raise InterruptedError(f'{option_text} нет в выпадающем списке')

    @allure.step('Подтверждаем заказ и проверяем успешное оформление')
    def confirm_order_and_check_modal(self):
        self.click(OrderPageLocators.BUTTON_YES)
        self.is_visible(OrderPageLocators.BUTTON_CHECK_STATUS)
        header = self.find_element(OrderPageLocators.MODAL_ORDER_HEADER)
        assert 'Заказ оформлен' in header.text
