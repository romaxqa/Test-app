import pytest
from pages.counter_page import CounterPage
import allure

@allure.feature("Counter form")
@allure.story("Checking the operation of the counter with different values")
@pytest.mark.parametrize(
    "first_value, second_value",
    [
        ("6", "70"),        # 1–100
        ("404", "935"),     # 100–1000
        ("2527", "8510")    # 1000–10000
    ],
    ids=[
        "equivalence_1_100", # Test case — Passed
        "equivalence_100_1000", # Test case — Failed
        "equivalence_1000_10000" # Test case — Failed
    ]
)

def test_counter_form_equivalence_partitions(browser, user_registration, user_authentication, first_value, second_value):
    with allure.step("User Registration"):
        user_registration
    
    with allure.step("User authentication"):
        user_authentication

    counter_page = CounterPage(browser)
    counter_page.open()
    
    counter_page.fill_input_change(first_value)
    counter_page.increase_button()
    assert counter_page.counter_result() == first_value

    counter_page.decrease_button()
    assert counter_page.counter_result() == "0"

    counter_page.fill_input_change(second_value)
    counter_page.increase_button()
    assert counter_page.counter_result() == second_value

    counter_page.decrease_button()
    assert counter_page.counter_result() == "0"
    