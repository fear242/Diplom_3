import allure
from pages.login_account_page import LoginAccountPage
from faker import Faker


fake = Faker(['ru_RU'])
URL = 'https://stellarburgers.nomoreparties.site/'
URL_forgot = 'https://stellarburgers.nomoreparties.site/forgot-password'


class TestLoginAccountPage:

    @allure.title('Тест: Авторизованный пользователь может сделать заказ')
    def test_authorised_user_can_make_order(self, driver, registered_user):
        l_a_page = LoginAccountPage(driver)
        l_a_page.login_into_account(registered_user)
        assert l_a_page.find_make_order_button() == True

    @allure.title('Тест: Переход на страницу аосстановления пароля по кнопке "Восстановить пароль"')
    def test_get_forgot_password_page_by_button(self, driver):
        l_a_page = LoginAccountPage(driver)
        l_a_page.open_login_page()
        l_a_page.click_on_restore_pass_button()
        assert l_a_page.find_restore_button() == True

    @allure.title('Тест: Ввод почты и клик "Восстановить" переводят на страницу создания пароля')
    def test_enter_mail_and_click_restore(self, driver):
        mail = fake.email()
        l_a_page = LoginAccountPage(driver)
        l_a_page.open_url(URL_forgot)
        l_a_page.enter_mail(mail)
        l_a_page.click_on_restore_button()
        assert l_a_page.find_code_from_mail_field() == True

    @allure.title('Тест: Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_make_pass_field_visible(self, driver):
        l_a_page = LoginAccountPage(driver)
        l_a_page.open_login_page()
        l_a_page.click_on_see_pass_button()
        assert l_a_page.find_is_password_input_active() == True

    @allure.title('Тест: Переход в раздел "История заказов')
    def test_get_order_history_page_by_button(self, driver, registered_user):
        l_a_page = LoginAccountPage(driver)
        l_a_page.login_into_account(registered_user)
        l_a_page.click_on_account_button()
        l_a_page.click_on_orders_history_button()
        assert l_a_page.find_history_order_block() == True

    @allure.title('Тест: Клик по кнопке "Выход" разлогинивает пользователя')
    def test_click_on_logout_button(self, driver, registered_user):
        l_a_page = LoginAccountPage(driver)
        l_a_page.login_into_account(registered_user)
        l_a_page.click_on_account_button()
        l_a_page.click_on_logout_button()
        assert l_a_page.find_enter_button() == True
