from selenium.webdriver.common.by import By


class MainPageLocators:

    BUTTON_ACCOUNT = By.XPATH, '//*[text()="Личный Кабинет"]'
    BUTTON_CONSTRUCTOR = By.XPATH, '//*[text()="Конструктор"]'
    BUTTON_ORDERS_FEED = By.XPATH, '//*[text()="Лента Заказов"]'
    BURGER_CONSTRUCTOR_TITLE = By.XPATH, '//*[text()="Соберите бургер"]'
    INGREDIENT = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d" and @draggable]'
    INGREDIENT_MODAL = By.XPATH, '//*[contains(@class, "contentBox")]'
    BUTTON_CLOSE_MODAL = By.XPATH, '//*[contains(@class, "modal__close") and @type="button"]'
    INGREDIENT_COUNTER = By.XPATH, '//p[contains(@class, "counter")]'
    PLACE_FOR_BUN = By.XPATH, '//section[contains(@class,"BurgerConstructor_basket")]'
    BUTTON_MAKE_ORDER = By.XPATH, '//*[text()="Оформить заказ"]'
