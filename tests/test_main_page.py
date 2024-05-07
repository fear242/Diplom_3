import allure
import data
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_account_page import LoginAccountPage


class TestMainPage:

    @allure.title('Тест: Переход по кнопке "Конструктор"')
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(data.URL_login)
        main_page.find_burger_constructor_button()
        main_page.click_on_constructor_button()
        assert main_page.find_burger_constructor_title()

    @allure.title('Тест: Переход по кнопке "Лента заказов"')
    def test_orders_feed_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_orders_feed_button()
        feed_page = FeedPage(driver)
        assert feed_page.find_feed_title()

    @allure.title('Тест: Появляется окнос информацией по клику на ингредиент')
    def test_modal_after_clicking_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_ingredient()
        assert main_page.find_ingredient_modal()

    @allure.title('Тест: Закрывается модальное окно ингредиента по клику на "крестик"')
    def test_modal_closure_by_clicking_x(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_ingredient()
        main_page.close_ingredients_modal()
        assert main_page.find_is_ingredient_clickable()

    @allure.title('Тест: Перход на страницу логина по клику на "Личный кабинет"')
    def test_click_login_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_account_button()
        l_a_page = LoginAccountPage(driver)
        assert l_a_page.find_login_button()

    @allure.title('Тест: Добавление ингредиента в корзину изменяет его счётчик')
    def test_add_ingredient_check_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        counter_0 = int(main_page.receive_ingredient_counter_text())
        main_page.drag_ingredient_to_basket()
        counter_1 = int(main_page.receive_ingredient_counter_text())
        assert counter_1 > counter_0
