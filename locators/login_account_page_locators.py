from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following::input'
    INPUT_PASSWORD = By.XPATH, '//label[text()="Пароль"]/following::input'
    BUTTON_RESTORE_PASS = By.XPATH, '//*[text()="Восстановить пароль"]'
    INPUT_CODE = By.XPATH, '//*[text()="Введите код из письма"]'
    BUTTON_RESTORE = By.XPATH, '//*[text()="Восстановить"]'
    BUTTON_SEE_PASS = By.XPATH, '//*[@class="input__icon input__icon-action"]'
    ACTIVE_INPUT_PASSWORD = By.XPATH, '//*[contains (@class, "placeholder-focused") and text()="Пароль"]'
    BUTTON_ORDERS_HISTORY = By.XPATH, '//*[text()="История заказов"]'
    ACTIVE_BUTTON_ORDER_HISTORY = By.XPATH, '//*[contains(@class, "Account_link_active") and text()="История заказов"]'
    BUTTON_LOGOUT = By.XPATH, '//*[text()="Выход"]'
    BUTTON_LOGIN = By.XPATH, '//*[text()="Войти"]'
