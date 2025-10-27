from selenium.webdriver.common.by import By


class HomePageLocators:
    ACCORDION_ITEM_HEADING_1 = [By.ID, 'accordion__heading-0']
    ACCORDION_ITEM_TEXT_1 = [By.ID, 'accordion__panel-0']
    ACCORDION_ITEM_HEADING_2 = [By.ID, 'accordion__heading-1']
    ACCORDION_ITEM_TEXT_2 = [By.ID, 'accordion__panel-1']
    ACCORDION_ITEM_HEADING_3 = [By.ID, 'accordion__heading-2']
    ACCORDION_ITEM_TEXT_3 = [By.ID, 'accordion__panel-2']
    ACCORDION_ITEM_HEADING_4 = [By.ID, 'accordion__heading-3']
    ACCORDION_ITEM_TEXT_4 = [By.ID, 'accordion__panel-3']
    ACCORDION_ITEM_HEADING_5 = [By.ID, 'accordion__heading-4']
    ACCORDION_ITEM_TEXT_5 = [By.ID, 'accordion__panel-4']
    ACCORDION_ITEM_HEADING_6 = [By.ID, 'accordion__heading-5']
    ACCORDION_ITEM_TEXT_6 = [By.ID, 'accordion__panel-5']
    ACCORDION_ITEM_HEADING_7 = [By.ID, 'accordion__heading-6']
    ACCORDION_ITEM_TEXT_7 = [By.ID, 'accordion__panel-6']
    ACCORDION_ITEM_HEADING_8 = [By.ID, 'accordion__heading-7']
    ACCORDION_ITEM_TEXT_8 = [By.ID, 'accordion__panel-7']
    BUTTON_ORDER_HEADER = [By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]']
    BUTTON_ORDER_FINISH = [By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']
    SAMOKAT_LOGO = [By.XPATH, '//a[contains(@class, "Header_LogoScooter")]']
    YANDEX_LOGO = [By.XPATH, '//a[contains(@class, "Header_LogoYandex")]']
