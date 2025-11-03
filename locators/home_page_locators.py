from selenium.webdriver.common.by import By


class HomePageLocators:
    ACCORDION_FAQ = {
        'question_1': {
            'heading': [By.ID, 'accordion__heading-0'],
            'text': [By.ID, 'accordion__panel-0']
        },
        'question_2': {
            'heading': [By.ID, 'accordion__heading-1'],
            'text': [By.ID, 'accordion__panel-1']
        },
        'question_3': {
            'heading': [By.ID, 'accordion__heading-2'],
            'text': [By.ID, 'accordion__panel-2']
        },
        'question_4': {
            'heading': [By.ID, 'accordion__heading-3'],
            'text': [By.ID, 'accordion__panel-3']
        },
        'question_5': {
            'heading': [By.ID, 'accordion__heading-4'],
            'text': [By.ID, 'accordion__panel-4']
        },
        'question_6': {
            'heading': [By.ID, 'accordion__heading-5'],
            'text': [By.ID, 'accordion__panel-5']
        },
        'question_7': {
            'heading': [By.ID, 'accordion__heading-6'],
            'text': [By.ID, 'accordion__panel-6']
        },
        'question_8': {
            'heading': [By.ID, 'accordion__heading-7'],
            'text': [By.ID, 'accordion__panel-7']
        },
    }
    BUTTON_ORDER_HEADER = [By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]']
    BUTTON_ORDER_FINISH = [By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']
    SAMOKAT_LOGO = [By.XPATH, '//a[contains(@class, "Header_LogoScooter")]']
    YANDEX_LOGO = [By.XPATH, '//a[contains(@class, "Header_LogoYandex")]']
