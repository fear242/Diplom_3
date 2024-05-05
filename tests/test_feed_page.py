from pages.feed_page import FeedPage
import allure


class TestFeedPage:

    def test_see_modal_by_clicking_order(self, driver, registered_user):
        feed_page = FeedPage(driver)
        feed_page.login_into_account(registered_user)
        feed_page.make_order()
        feed_page.click_on_account_button()
        feed_page.click_on_orders_history_button()
        feed_page.click_on_order()
        assert feed_page.find_order_modal() == True

    def test_users_history_in_orders_feed(self, driver, registered_user):
        feed_page = FeedPage(driver)
        feed_page.login_into_account(registered_user)
        feed_page.make_order()
        feed_page.click_on_account_button()
        feed_page.click_on_orders_history_button()
        order_num = feed_page.get_orders_number()
        feed_page.click_on_orders_feed_button()
        order_feed = feed_page.get_orders_number()
        assert order_num in order_feed

    def test_all_time_counter_raise_by_order(self, driver, registered_user):
        feed_page = FeedPage(driver)
        feed_page.login_into_account(registered_user)
        feed_page.click_on_orders_feed_button()
        count_0 = int(feed_page.get_alltime_counter_text())
        feed_page.click_on_constructor_button()
        feed_page.make_order()
        feed_page.click_on_orders_feed_button()
        count_1 = int(feed_page.get_alltime_counter_text())
        assert count_1 > count_0

    def test_today_counter_raise_by_order(self, driver, registered_user):
        feed_page = FeedPage(driver)
        feed_page.login_into_account(registered_user)
        feed_page.click_on_orders_feed_button()
        count_0 = int(feed_page.get_today_counter_text())
        feed_page.click_on_constructor_button()
        feed_page.make_order()
        feed_page.click_on_orders_feed_button()
        count_1 = int(feed_page.get_today_counter_text())
        assert count_1 > count_0

    def test_order_appears_in_progress_list(self, driver, registered_user):
        feed_page = FeedPage(driver)
        feed_page.login_into_account(registered_user)
        feed_page.make_order()
        feed_page.click_on_account_button()
        feed_page.click_on_orders_history_button()
        order_num = str(feed_page.get_orders_number())
        feed_page.click_on_orders_feed_button()
        assert feed_page.get_in_progress_lists_text() in order_num
