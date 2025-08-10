from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10, poll_frequency=1)

    @allure.step("Open page")
    def open(self):
        self.browser.get(self.PAGE_URL)

    @allure.step("Check that page is opened")
    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))