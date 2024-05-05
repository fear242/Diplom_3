from selenium.common import ElementClickInterceptedException
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.login_account_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.feed_page_locators import FeedPageLocators
import allure


URL_login = 'https://stellarburgers.nomoreparties.site/login'


class FeedPage(BasePage):

    @allure.step('Входим в аккаунт')
    def login_into_account(self, registered_user):
        payload = registered_user
        self.open_url(URL_login)
        self.text_input_to_element(LoginPageLocators.INPUT_EMAIL, payload["email"])
        self.text_input_to_element(LoginPageLocators.INPUT_PASSWORD, payload["password"])
        self.click_on_element(LoginPageLocators.BUTTON_LOGIN)

    @allure.step('Создаём заказ')
    def make_order(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT, MainPageLocators.PLACE_FOR_BUN)
        self.click_on_element(MainPageLocators.BUTTON_MAKE_ORDER)
        self.press_esc()

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_on_account_button(self):
        try:
            self.click_on_element(BasePageLocators.BUTTON_ACCOUNT)
        except ElementClickInterceptedException:
            self.click_on_element(BasePageLocators.BUTTON_ACCOUNT)  # Без исключения драйвер прикидывается, что
                                                                    #  клику что-то мешает.

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_orders_history_button(self):
        self.click_on_element(LoginPageLocators.BUTTON_ORDERS_HISTORY)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(BasePageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Кликаем по заказу')
    def click_on_order(self):
        self.click_on_element(FeedPageLocators.ORDER)

    @allure.step('Находим модальное окно с информацией о заказе')
    def find_order_modal(self):
        element = self.find_element_with_wait(FeedPageLocators.ORDER_MODAL)
        return element.is_displayed()

    @allure.step('Получаем номер заказа')
    def get_orders_number(self):
        return self.get_text_from_element(FeedPageLocators.ORDER_NUMBER)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_on_orders_feed_button(self):
        try:
            self.click_on_element(BasePageLocators.BUTTON_ORDERS_FEED)
        except ElementClickInterceptedException:
            self.click_on_element(BasePageLocators.BUTTON_ORDERS_FEED)

    @allure.step('Получаем показания счётчика заказо за всё время')
    def get_alltime_counter_text(self):
        return self.get_text_from_element(FeedPageLocators.ALL_TIME_COUNTER)

    @allure.step('Получаем показания счётчика заказов за сегодня')
    def get_today_counter_text(self):
        return self.get_text_from_element(FeedPageLocators.TODAY_COUNTER)

    @allure.step('Получаем список заказов в работе')
    def get_in_progress_lists_text(self):
        return self.get_text_from_element(FeedPageLocators.IN_PROGRESS_LIST)
