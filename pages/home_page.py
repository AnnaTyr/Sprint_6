import allure
from pages.base_page import BasePage
from pages.order_page import OrderPage
from time import sleep


class HomePage(BasePage):
    
    url = 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('Выбираем раздел')
    def choose_section(self, locator: list, section_header: str):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        assert self.find_element(locator).text == section_header

    @allure.step('Проверяем ответ в разделе')
    def check_section_content(self, locator: list, section_content: str):
        self.is_visible(locator)
        assert self.find_element(locator).text == section_content

    @allure.step('Переходим на страницу заказа')
    def go_to_order(self, button: list):
        self.click(button)
        self.url_to_be(OrderPage.url)

    @allure.step('Проверяем урл, по которому осуществился переход')
    def check_logo_go_to_url(self, logo: str):
        if logo == 'samokat':
            assert self.driver.current_url == self.url
        elif logo == 'yandex':
            window_handles_after = self.driver.window_handles
            assert len(window_handles_after) == 2, 'Новая вкладка не открылась'
            new_window_handle = window_handles_after[-1]
            self.driver.switch_to.window(new_window_handle)
            self.url_to_be('https://dzen.ru/?yredirect=true')
        else:
            raise ValueError('Передан некорректный логотип')
