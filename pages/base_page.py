from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def text_input_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def drag_and_drop_element(self, element_locator, destination_locator):
        action = ActionChains(self.driver)
        action.drag_and_drop(element_locator, destination_locator)

    def find_element_by_text(self, text):
        self.driver.find_element_by_xpath(f'//*[contains(text(), {text}')
