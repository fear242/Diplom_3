from selenium.webdriver.common.by import By


class BasePageLocators:

    BUTTON_ACCOUNT = By.XPATH, '//*[text()="Личный Кабинет"]'
    BUTTON_CONSTRUCTOR = By.XPATH, '//*[text()="Конструктор"]'
    BUTTON_ORDERS_FEED = By.XPATH, '//*[text()="Лента Заказов"]'