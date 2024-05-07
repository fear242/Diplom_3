import allure
from pages.feed_page import FeedPage
from pages.login_account_page import LoginAccountPage
from pages.main_page import MainPage


class TestFeedPage:

    @allure.title('Тест: Всплывает окно с деталями заказа по клику на заказ')
    def test_see_modal_by_clicking_order(self, driver, registered_user):
        payload = registered_user
        l_a_page = LoginAccountPage(driver)
        l_a_page.login_into_account(payload)
        main_page = MainPage(driver)
        main_page.make_order()
        main_page.click_on_account_button()
        l_a_page.click_on_orders_history_button()
        feed_page = FeedPage(driver)
        feed_page.click_on_order()
        assert feed_page.find_order_modal()

    @allure.title('Тест: Заказ из Истории заказов пользователя виден в Ленте заказов')
    def test_users_history_in_orders_feed(self, driver, registered_user):
        payload = registered_user
        l_a_page = LoginAccountPage(driver)
        l_a_page.login_into_account(payload)
        main_page = MainPage(driver)
        main_page.make_order()
        main_page.click_on_account_button()
        l_a_page.click_on_orders_history_button()
        feed_page = FeedPage(driver)
        order_num = feed_page.get_orders_number()
        main_page.click_on_orders_feed_button()
        order_feed = feed_page.get_orders_number()
        assert order_num in order_feed

    @allure.title('Тест: При добавлении заказа счётчик "Выполнено за всё время" увеличивается')
    def test_all_time_counter_raise_by_order(self, driver, registered_user):
        payload = registered_user
        l_a_page = LoginAccountPage(driver)
        l_a_page.login_into_account(payload)
        main_page = MainPage(driver)
        main_page.click_on_orders_feed_button()
        feed_page = FeedPage(driver)
        count_0 = int(feed_page.get_alltime_counter_text())
        main_page.click_on_constructor_button()
        main_page.make_order()
        main_page.click_on_orders_feed_button()
        count_1 = int(feed_page.get_alltime_counter_text())
        assert count_1 > count_0

    @allure.title('Тест: При добавлении заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_counter_raise_by_order(self, driver, registered_user):
        payload = registered_user
        l_a_page = LoginAccountPage(driver)
        l_a_page.login_into_account(payload)
        main_page = MainPage(driver)
        main_page.click_on_orders_feed_button()
        feed_page = FeedPage(driver)
        count_0 = int(feed_page.get_today_counter_text())
        main_page.click_on_constructor_button()
        main_page.make_order()
        main_page.click_on_orders_feed_button()
        count_1 = int(feed_page.get_today_counter_text())
        assert count_1 > count_0

    @allure.title('Тест: При создании, заказ появляется в блоке "В работе"')
    def test_order_appears_in_progress_list(self, driver, registered_user):
        payload = registered_user
        l_a_page = LoginAccountPage(driver)
        l_a_page.login_into_account(payload)
        main_page = MainPage(driver)
        main_page.make_order()
        main_page.click_on_account_button()
        l_a_page.click_on_orders_history_button()
        feed_page = FeedPage(driver)
        order_num = str(feed_page.get_orders_number())
        main_page.click_on_orders_feed_button()
        assert feed_page.get_in_progress_lists_text() in order_num
