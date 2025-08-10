from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.links import Links
from selenium.webdriver.common.keys import Keys
import allure

class CounterPage(BasePage):
    """
    Class for interacting with the counter form.
    Provides methods for entering values, managing the buttons
    to increase/decrease the counter and getting the current value.
    """

    PAGE_URL = Links.COUNTER_PAGE

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    @allure.step("Open counter page")
    def open(self):
        super().open()

    @allure.step("Fill input change: {value}")
    def fill_input_change(self, value):
        input_change = self.browser.find_element(By.CSS_SELECTOR, "#input-89")
        input_change.click()
        input_change.send_keys(Keys.CONTROL + "a")
        input_change.send_keys(Keys.DELETE)
        input_change.send_keys(str(value))

    @allure.step("Click on the increase button")
    def increase_button(self):
        increase = self.browser.find_element(By.CSS_SELECTOR, "#app > div > main > div > div > div > div.v-card__text > button.ma-3.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--dark.v-size--default.green.darken-4")
        increase.click()

    @allure.step("Check the counter result")
    def counter_result(self):
        result = self.browser.find_element(By.CSS_SELECTOR, "span[data-v-905d94ce]")
        return result.text

    @allure.step("Click on the decrease button")
    def decrease_button(self):
        decrease = self.browser.find_element(By.CSS_SELECTOR,"#app > div > main > div > div > div > div.v-card__text > button.ma-3.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--dark.v-size--default.red.darken-4")
        decrease.click()
