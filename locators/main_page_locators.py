from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_ACCOUNT = By.XPATH, '//*[@href="/account"]'
    BUTTON_CONSTRUCTOR = By.XPATH, '//*[text()="Конструктор"]'
    BUTTON_MAKE_ORDER = By.XPATH, '//*[text()="Оформить заказ"]'
    BUTTON_ORDERS_FEED = By.XPATH, '//*[text()="Лента Заказов"]'
    INGREDIENT = By.XPATH, '//*[contains(@class, "ingredient") and @draggable]'
    INGREDIENT_MODAL = By.XPATH, '//*[contains(@class, "contentBox")]'
    BUTTON_CLOSE_MODAL = By.XPATH, '//*[contains(@class, "modal__close") and @type="button"]'
    INGREDIENT_COUNTER = By.XPATH, '//p[contains(@class, "counter")]'
    PLACE_FOR_BUN = By.XPATH, '//*[text()="Перетяните булочку сюда (верх)"]'
