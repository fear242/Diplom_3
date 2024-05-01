from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_on_account_button(self):
        self.click_on_element(MainPageLocators.BUTTON_ACCOUNT)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_on_orders_feed_button(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDERS_FEED)

    @allure.step('Клик по ингредиенту')
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT)

    @allure.step('Находим модальное окно с описанием ингредиента')
    def find_ingredient_modal(self):
        self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL)

    @allure.step('Клик по кнопке, закрывающей модальное окно с описанием ингредиента')
    def close_ingredients_modal(self):
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_MODAL)

    @allure.step('Перетаскиваем булочку в заказ')
    def drag_ingredient_to_basket(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT, MainPageLocators.PLACE_FOR_BUN)

    @allure.step('Получаем информацию от счётчика ингредиента')
    def receive_ingredient_counter_text(self):
        self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Кликаем кнопку "Оформить заказ"')
    def click_on_order_button(self):
        self.click_on_element(MainPageLocators.BUTTON_MAKE_ORDER)
