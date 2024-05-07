from selenium.webdriver.common.by import By


class FeedPageLocators:

    FEED_PAGE_TITLE = By.XPATH, '//*[text()="Лента заказов"]'
    BUTTON_CLOSE_MODAL = By.XPATH, '//*[contains(@class, "modal__close") and @type="button"]'
    MODAL_ORDER_NUMBER = By.XPATH, '//h2[contains(@class, "modal__title")]'
    ORDER = By.XPATH, '//div[contains(@class, "OrderHistory")]//child::a'
    ORDER_MODAL = By.XPATH, '//section[contains(@class, "modal_opened")]'
    ORDER_NUMBER = By.XPATH, '//*[@class="text text_type_digits-default"]'
    ALL_TIME_COUNTER = By.XPATH, '//*[text()="Выполнено за все время:"]/following::p'
    TODAY_COUNTER = By.XPATH, '//*[text()="Выполнено за сегодня:"]/following::p'
    IN_PROGRESS_LIST = By.XPATH, '//*[contains(@class, "orderListReady")]/child::li[@class="text text_type_digits-default mb-2"]'
