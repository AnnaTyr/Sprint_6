from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_NAME = [By.XPATH, '//input[contains(@placeholder, "Имя")]']
    INPUT_LAST_NAME = [By.XPATH, '//input[contains(@placeholder, "Фамилия")]']
    INPUT_ADDRESS = [By.XPATH, '//input[contains(@placeholder, "Адрес")]']
    INPUT_STATION = [By.XPATH, '//input[contains(@placeholder, "Станция")]']
    INPUT_PHONE = [By.XPATH, '//input[contains(@placeholder, "Телефон")]']
    BUTTON_NEXT = [By.XPATH, '//button[text()="Далее"]']
    INPUT_DATE = [By.XPATH, '//input[contains(@placeholder, "Когда")]']
    DATE_SELECTED = [By.XPATH, '//div[contains(@class, "react-datepicker__day--selected")]']
    DROPDOWN_TERM = [By.CLASS_NAME, 'Dropdown-root']
    DROPDOWN_OPTION = [By.XPATH, '//div[@class="Dropdown-option"]']
    BUTTON_ORDER = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']
    BUTTON_YES = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Да"]']
    MODAL_ORDER_HEADER = [By.XPATH, '//div[contains(@class, "Order_ModalHeader")]']
    BUTTON_CHECK_STATUS = [By.XPATH, '//button[text()="Посмотреть статус"]']




