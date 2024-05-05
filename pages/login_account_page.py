from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.login_account_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
import allure


URL_login = 'https://stellarburgers.nomoreparties.site/login'


class LoginAccountPage(BasePage):

    @allure.step('Входим в аккаунт')
    def login_into_account(self, registered_user):
        payload = registered_user
        self.open_url(URL_login)
        self.text_input_to_element(LoginPageLocators.INPUT_EMAIL, payload["email"])
        self.text_input_to_element(LoginPageLocators.INPUT_PASSWORD, payload["password"])
        self.click_on_element(LoginPageLocators.BUTTON_LOGIN)

    @allure.step('Переход на страницу логина')
    def open_login_page(self):
        self.open_url(URL_login)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_on_account_button(self):
        self.click_on_element(BasePageLocators.BUTTON_ACCOUNT)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_on_restore_pass_button(self):
        self.scroll_to_element(LoginPageLocators.BUTTON_RESTORE_PASS)
        self.click_on_element(LoginPageLocators.BUTTON_RESTORE_PASS)

    @allure.step('Ввод электронного адреса пользователя')
    def enter_mail(self, mail):
        self.text_input_to_element(LoginPageLocators.INPUT_EMAIL, mail)

    @allure.step('Находим кнопку "Войти"')
    def find_enter_button(self):
        element = self.find_element_with_wait(LoginPageLocators.BUTTON_LOGIN)
        return element.is_displayed()

    @allure.step('Находим кнопку "Восстановить"')
    def find_restore_button(self):
        element = self.find_element_with_wait(LoginPageLocators.BUTTON_RESTORE)
        return element.is_displayed()

    @allure.step('Находим поле для ввода кода из письма')
    def find_code_from_mail_field(self):
        element = self.find_element_with_wait(LoginPageLocators.INPUT_CODE)
        return element.is_displayed()

    @allure.step('Клик по кнопке "Восстановить"')
    def click_on_restore_button(self):
        self.click_on_element(LoginPageLocators.BUTTON_RESTORE)

    @allure.step('Тык в глаз')
    def click_on_see_pass_button(self):
        self.click_on_element(LoginPageLocators.BUTTON_SEE_PASS)

    @allure.step('Проверяем, что поле ввода пароля активно')
    def find_is_password_input_active(self):
        element = self.find_element_with_wait(LoginPageLocators.ACTIVE_INPUT_PASSWORD)
        return element.is_displayed()

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_orders_history_button(self):
        self.click_on_element(LoginPageLocators.BUTTON_ORDERS_HISTORY)

    @allure.step('Находим блок с историей заказов')
    def find_history_order_block(self):
        element = self.find_element_with_wait(LoginPageLocators.ACTIVE_BUTTON_ORDER_HISTORY)
        return element.is_displayed()

    @allure.step('Клик по кнопке "Выход"')
    def click_on_logout_button(self):
        self.click_on_element(LoginPageLocators.BUTTON_LOGOUT)

    @allure.step('Находим кнопку"Оформить заказ"')
    def find_make_order_button(self):
        element = self.find_element_with_wait(MainPageLocators.BUTTON_MAKE_ORDER)
        return element.is_displayed()
