from pages.base_page import BasePage
from locators.login_account_page_locators import LoginPageLocators
import allure


class LoginAccountPage(BasePage):

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_on_restore_pass_button(self):
        self.click_on_element(LoginPageLocators.BUTTON_RESTORE_PASS)

    @allure.step('Ввод электронного адреса пользователя')
    def enter_mail(self, mail):
        self.text_input_to_element(LoginPageLocators.INPUT_EMAIL, mail)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_on_restore_button(self):
        self.click_on_element(LoginPageLocators.BUTTON_RESTORE)

    @allure.step('Тык в глаз')
    def click_on_see_pass_button(self):
        self.click_on_element(LoginPageLocators.BUTTON_SEE_PASS)

    @allure.step('Проверяем, что поле ввода пароля активно')
    def find_is_password_input_active(self):
        self.find_element_with_wait(LoginPageLocators.ACTIVE_INPUT_PASSWORD)

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_orders_history_button(self):
        self.click_on_element(LoginPageLocators.BUTTON_ORDERS_HISTORY)

    @allure.step('Клик по кнопке "Выход"')
    def click_on_logout_button(self):
        self.click_on_element(LoginPageLocators.BUTTON_LOGOUT)
