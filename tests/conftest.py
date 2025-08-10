"""
Configuration test
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def browser():
    """
    Main fixture
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def user_registration(browser):
    registration_page = RegistrationPage(browser)
    registration_page.open()
    registration_page.fill_login("usertest")
    registration_page.fill_password("1234")
    registration_page.fill_confirm_password("1234")
    registration_page.submit()
    
    message = registration_page.get_success_message()
    assert "Теперь вы можете войти в систему, используя свой логин и пароль" in message
    yield

@pytest.fixture(scope="function")
def user_authentication(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.fill_login("usertest")
    login_page.fill_password("1234")
    login_page.login_button()
    assert "Добро пожаловать" in login_page.get_success_message()
    yield
