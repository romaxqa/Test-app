import pytest
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
import allure

@allure.feature("Login form")
@allure.story("Checking login scripts")
@pytest.mark.parametrize(
    "login, password, expected_message, is_positive",
    [
        ("usertest", "1234", "Добро пожаловать", True),

        ("usertest_incorrect", "1234", "Пользователь с таким логином не существует", False),

        ("usertest", "1234_incorrect", "Неверный пароль", False),

        ("usertest_incorrect", "1234_incorrect", "Пользователь с таким логином не существует", False),
    ]   
)

def test_login_form(browser, login, password, expected_message, is_positive, user_registration):
    """
    + Проверка работы формы входа (табл. принятия решений, правило № 1)
    - Проверка работы формы входа (табл. принятия решений, правило № 2)
    - Проверка работы формы входа (табл. принятия решений, правило № 3)
    - Проверка работы формы входа (табл. принятия решений, правило № 4)
    """
    with allure.step("User registration"):
        user_registration
    
    login_page = LoginPage(browser)
    login_page.open()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.login_button()

    with allure.step("Checking the result"):
        if is_positive:
            message = login_page.get_success_message()
            login_page.exit_button()
        else:
            message = login_page.get_error_message()

        assert expected_message in message
        