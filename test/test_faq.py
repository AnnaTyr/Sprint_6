import allure

from locators.home_page_locators import *


class TestFaqSection:

    @allure.title('Проверка наличия ответа на вопрос 1 в FAQ')
    def test_faq_item_1(self, home_page):
        section_header = 'Сколько это стоит? И как оплатить?'
        section_content = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        home_page.open_page(home_page.url)
        home_page.choose_section(locator=HomePageLocators.ACCORDION_ITEM_HEADING_1, section_header=section_header)
        home_page.check_section_content(locator=HomePageLocators.ACCORDION_ITEM_TEXT_1, section_content=section_content)

    @allure.title('Проверка наличия ответа на вопрос 2 в FAQ')
    def test_faq_item_2(self, home_page):
        section_header = 'Хочу сразу несколько самокатов! Так можно?'
        section_content = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете ' \
                          'просто сделать несколько заказов — один за другим.'
        home_page.open_page(home_page.url)
        home_page.choose_section(locator=HomePageLocators.ACCORDION_ITEM_HEADING_2, section_header=section_header)
        home_page.check_section_content(locator=HomePageLocators.ACCORDION_ITEM_TEXT_2, section_content=section_content)

    @allure.title('Проверка наличия ответа на вопрос 3 в FAQ')
    def test_faq_item_3(self, home_page):
        section_header = 'Как рассчитывается время аренды?'
        section_content = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт ' \
                          'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли ' \
                          'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        home_page.open_page(home_page.url)
        home_page.choose_section(locator=HomePageLocators.ACCORDION_ITEM_HEADING_3, section_header=section_header)
        home_page.check_section_content(locator=HomePageLocators.ACCORDION_ITEM_TEXT_3, section_content=section_content)

    @allure.title('Проверка наличия ответа на вопрос 4 в FAQ')
    def test_faq_item_4(self, home_page):
        section_header = 'Можно ли заказать самокат прямо на сегодня?'
        section_content = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        home_page.open_page(home_page.url)
        home_page.choose_section(locator=HomePageLocators.ACCORDION_ITEM_HEADING_4, section_header=section_header)
        home_page.check_section_content(locator=HomePageLocators.ACCORDION_ITEM_TEXT_4, section_content=section_content)

    @allure.title('Проверка наличия ответа на вопрос 5 в FAQ')
    def test_faq_item_5(self, home_page):
        section_header = 'Можно ли продлить заказ или вернуть самокат раньше?'
        section_content = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому ' \
                          'номеру 1010.'
        home_page.open_page(home_page.url)
        home_page.choose_section(locator=HomePageLocators.ACCORDION_ITEM_HEADING_5, section_header=section_header)
        home_page.check_section_content(locator=HomePageLocators.ACCORDION_ITEM_TEXT_5, section_content=section_content)

    @allure.title('Проверка наличия ответа на вопрос 6 в FAQ')
    def test_faq_item_6(self, home_page):
        section_header = 'Вы привозите зарядку вместе с самокатом?'
        section_content = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете ' \
                          'кататься без передышек и во сне. Зарядка не понадобится.'
        home_page.open_page(home_page.url)
        home_page.choose_section(locator=HomePageLocators.ACCORDION_ITEM_HEADING_6, section_header=section_header)
        home_page.check_section_content(locator=HomePageLocators.ACCORDION_ITEM_TEXT_6, section_content=section_content)

    @allure.title('Проверка наличия ответа на вопрос 7 в FAQ')
    def test_faq_item_7(self, home_page):
        section_header = 'Можно ли отменить заказ?'
        section_content = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все ' \
                          'же свои.'
        home_page.open_page(home_page.url)
        home_page.choose_section(locator=HomePageLocators.ACCORDION_ITEM_HEADING_7, section_header=section_header)
        home_page.check_section_content(locator=HomePageLocators.ACCORDION_ITEM_TEXT_7, section_content=section_content)

    @allure.title('Проверка наличия ответа на вопрос 8 в FAQ')
    def test_faq_item_8(self, home_page):
        section_header = 'Я жизу за МКАДом, привезёте?'
        section_content = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        home_page.open_page(home_page.url)
        home_page.choose_section(locator=HomePageLocators.ACCORDION_ITEM_HEADING_8, section_header=section_header)
        home_page.check_section_content(locator=HomePageLocators.ACCORDION_ITEM_TEXT_8, section_content=section_content)
