from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.links import Links
import allure

class LoginPage(BasePage):
    """
    Class for working with the login page.
    Contains methods for entering the username and password,
    submitting the login form and checking for error messages.
    """
    
    PAGE_URL = Links.LOGIN_PAGE
    
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Open login page")
    def open(self):
        super().open()

    @allure.step("Fill login field with: {login}")
    def fill_login(self, login):
        self.browser.find_element(By.NAME, "login").send_keys(login)

    @allure.step("Fill password field with: {password}")
    def fill_password(self, password):
        self.browser.find_element(By.NAME, "password").send_keys(password)

    @allure.step("Click on the login button")
    def login_button(self):
        login_button = self.browser.find_element(By.XPATH, value='//*[@id="app"]/div/main/div/div/div[1]/div/div/div[2]/button')
        login_button.click()

    @allure.step("Get success message after login")
    def get_success_message(self):
        wait = WebDriverWait(self.browser, 10)
        message = wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#app > div > main > div > div > div > div > div.v-card__title"
            ))
        )
        return message.text
    
    @allure.step("Get error message after login")
    def get_error_message(self):
        wait = WebDriverWait(self.browser, 10)
        message = wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__text"
            ))
        )
        return message.text
    
    @allure.step("Click on the exit button")
    def exit_button(self):
        exit_button = self.browser.find_element(By.CSS_SELECTOR, "#app > div > footer > div > button")
        exit_button.click()
        