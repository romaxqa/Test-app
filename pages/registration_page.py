from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.links import Links
import allure

class RegistrationPage(BasePage):
    """
    Class for working with the user registration page:
    contains methods for filling in fields, 
    submitting the form and checking error messages.
    """
    
    PAGE_URL = Links.REGISTRATION_PAGE
    
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Open registration page")
    def open(self):
        super().open()

    @allure.step("Fill login field with: {login}")
    def fill_login(self, login):
        self.browser.find_element(By.XPATH, value='//*[@id="input-31"]').send_keys(login)

    @allure.step("Fill password field with: {password}")
    def fill_password(self, password):
        self.browser.find_element(By.XPATH, value='//*[@id="input-35"]').send_keys(password)

    @allure.step("Fill confirm password with: {password}")
    def fill_confirm_password(self, password):
        self.browser.find_element(By.XPATH, value='//*[@id="input-39"]').send_keys(password)

    @allure.step("Click on the register button")
    def submit(self):
        reg_button = self.browser.find_element(By.XPATH, value='//*[@id="app"]/div/main/div/div/div[1]/div/div/div[2]/button')
        reg_button.click()

    @allure.step("Get success message after registration")
    def get_success_message(self):
        wait = WebDriverWait(self.browser, 10)
        message = wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text"
            ))
        )
        return message.text
    
    @allure.step("Get error message after registration")
    def get_error_message(self):
        wait = WebDriverWait(self.browser, 10)
        message = wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text"
            ))
        )
        return message.text