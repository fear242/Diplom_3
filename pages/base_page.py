from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, link):
        self.driver.get(link)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def text_input_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def drag_and_drop_element(self, element_locator, destination_locator):
        element = self.find_element_with_wait(element_locator)
        destination = self.find_element_with_wait(destination_locator)
        action = ActionChains(self.driver)
        action.drag_and_drop(element, destination).perform()

    def press_esc(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()
