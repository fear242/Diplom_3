from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
import allure


class FeedPage(BasePage):

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

    @allure.step('Находим заголовок "Лента заказов"')
    def find_feed_title(self):
        element = self.find_element_with_wait(FeedPageLocators.FEED_PAGE_TITLE)
        return element.is_displayed()

    @allure.step('Получаем показания счётчика заказо за всё время')
    def get_alltime_counter_text(self):
        return self.get_text_from_element(FeedPageLocators.ALL_TIME_COUNTER)

    @allure.step('Получаем показания счётчика заказов за сегодня')
    def get_today_counter_text(self):
        return self.get_text_from_element(FeedPageLocators.TODAY_COUNTER)

    @allure.step('Получаем список заказов в работе')
    def get_in_progress_lists_text(self):
        return self.get_text_from_element(FeedPageLocators.IN_PROGRESS_LIST)
