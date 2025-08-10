import pytest
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.counter_page import CounterPage
from config.links import Links
import allure

@allure.feature("Registration form")
@allure.story("Checking registration scripts")
@pytest.mark.parametrize(
    "login, password, confirm_password, expected_message, is_positive",
    [
        ("usertest", "1234", "1234", "Теперь вы можете войти в систему, используя свой логин и пароль", True),

        ("usertest", "1234", "12345", "Пароль и подтверждение пароля не совпадают", False),
    ]
)

def test_registration_form(browser, login, password, confirm_password, expected_message, is_positive):
    """
    + проверка работы формы регистрации
    - проверка работы формы регистрации
    """
    
    registration_page = RegistrationPage(browser)
    registration_page.open()
    registration_page.fill_login(login)
    registration_page.fill_password(password)
    registration_page.fill_confirm_password(confirm_password)
    registration_page.submit()

    with allure.step("Checking the result"):
        if is_positive:
            message = registration_page.get_success_message()
        else:
            message = registration_page.get_error_message()

        assert expected_message == message
        