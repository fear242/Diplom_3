from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following::input'
    INPUT_PASSWORD = By.XPATH, '//label[text()="Пароль"]/following::input'
    BUTTON_RESTORE_PASS = By.XPATH, '//*[text()="Восстановить пароль"]'
    BUTTON_SEE_PASS = By.XPATH, '//*[@class="input__icon input__icon-action"]'
    BUTTON_ORDERS_HISTORY = By.XPATH, '//*[text()="История заказов"]'
    BUTTON_LOGOUT = By.XPATH, '//*[text()="Выход"]'
