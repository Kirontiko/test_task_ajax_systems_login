import pytest
import logging

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "login, password, expected",
    [
        pytest.param(
            "UserNotFound",
            "qa_automation_password",
            False,
            id="Login is incorrect",
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "wrong_mate",
            False,
            id="Password is incorrect",
        ),
        pytest.param(
            "you_are_not_even_close",
            "mate",
            False,
            id="All user data is incorrect"
        ),
    ],
)
def test_user_login_incorrect(user_login_fixture, login: str, password: str, expected: bool) -> None:
    page = user_login_fixture
    LOGGER.info(f"Start logging in test with login: {login} password: {password}")
    page.fill_user_data(login, password)
    assert page.check_if_login_is_success() == expected
    LOGGER.info(f"This data is not valid, login action failed")
    page.driver.reset()


@pytest.mark.parametrize(
    "login, password, expected",
    [
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            True,
            id="User data is correct",
        )
    ],
)
def test_user_login_correct(user_login_fixture, login: str, password: str, expected: bool) -> None:
    page = user_login_fixture
    LOGGER.info(f"Start logging in test with login: {login} password: {password}")
    page.fill_user_data(login, password)
    assert page.check_if_login_is_success() == expected
    LOGGER.info(f"This data is valid, login action success")
