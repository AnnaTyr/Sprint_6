import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_page(self, url: str):
        self.driver.get(url)

    @allure.step('Поиск элемента на странице')
    def find_element(self, locator: list) -> WebElement:
        try:
            element = self.driver.find_element(by=locator[0], value=locator[1])
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element
        except NoSuchElementException:
            raise NoSuchElementException(f"Элемент не найден на странице")

    @allure.step('Поиск элементов на странице')
    def find_elements(self, locator: list):
        try:
            return self.driver.find_elements(by=locator[0], value=locator[1])
        except NoSuchElementException:
            raise NoSuchElementException(f"Элемент не найден на странице")

    @allure.step('Проверяем, что элемент отображается на странице')
    def is_visible(self, locator: list, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    @allure.step('Клик на элемент на странице')
    def click(self, locator: list):
        element = self.find_element(locator)
        if self.is_clickable(locator):
            element.click()
        else:
            raise NoSuchElementException('Элемент не кликабелен')

    @allure.step('Проверяем, что элемент кликабельный')
    def is_clickable(self, locator: list, timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def url_to_be(self, url: str, timeout: int = 5):
        WebDriverWait(self.driver, timeout).until(ec.url_to_be(url))
