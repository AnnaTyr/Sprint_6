import allure
import pytest

from locators.home_page_locators import *

faq = {
    'question_1': {
        'question': 'Сколько это стоит? И как оплатить?',
        'answer': 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    },
    'question_2': {
        'question': 'Хочу сразу несколько самокатов! Так можно?',
        'answer': 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто '
                  'сделать несколько заказов — один за другим.'
    },
    'question_3': {
        'question': 'Как рассчитывается время аренды?',
        'answer': 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени '
                  'аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в '
                  '20:30, суточная аренда закончится 9 мая в 20:30.'
    },
    'question_4': {
        'question': 'Можно ли заказать самокат прямо на сегодня?',
        'answer': 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    },
    'question_5': {
        'question': 'Можно ли продлить заказ или вернуть самокат раньше?',
        'answer': 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    },
    'question_6': {
        'question': 'Вы привозите зарядку вместе с самокатом?',
        'answer': 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься'
                  ' без передышек и во сне. Зарядка не понадобится.'
    },
    'question_7': {
        'question': 'Можно ли отменить заказ?',
        'answer': 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    },
    'question_8': {
        'question': 'Я жизу за МКАДом, привезёте?',
        'answer': 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    },
}


class TestFaqSection:

    @pytest.mark.parametrize('question', [key for key in faq.keys()])
    @allure.title('Проверка наличия ответа на вопрос 1 в FAQ')
    def test_faq_item_1(self, home_page, question):
        section_header = faq[question]["question"]
        section_content = faq[question]["answer"]
        home_page.open_page(home_page.url)
        home_page.choose_section(locator=HomePageLocators.ACCORDION_FAQ[question]["heading"], section_header=section_header)
        home_page.check_section_content(locator=HomePageLocators.ACCORDION_FAQ[question]["text"], section_content=section_content)
