from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDER = By.XPATH, '//*[contains(@class, "listItem")]'
    ORDER_MODAL = By.XPATH, '//*[contains(@class, "Modal_orderBox_")]'
    ORDER_NUMBER = By.XPATH, '//*[@class="text text_type_digits-default"]'
    ALL_TIME_COUNTER = By.XPATH, '//*[text()="Выполнено за все время:"]/following::p'
    TODAY_COUNTER = By.XPATH, '//*[text()="Выполнено за сегодня:"]/following::p'
    IN_PROGRESS_LIST = By.XPATH, '//*[contains(@class, "orderListReady")]/child::li'
