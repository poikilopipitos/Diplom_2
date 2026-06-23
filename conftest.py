import pytest
import allure
from api_methods.burger_methods import BurgerMethods
from helpers.helpers import generate_user_data 


@pytest.fixture
def user_setup():
    with allure.step("Фикстура SETUP: Создание и авторизация пользователя перед тестом"):
        payload = generate_user_data()
        create_responce = BurgerMethods.create_user(payload)
        assert create_responce.status_code == 200
        login_response = BurgerMethods.login_user({
        "email": payload["email"],
        "password": payload["password"]})
        user_token = login_response.json().get("accessToken")
        yield {"payload": payload, "accessToken": user_token}
        if user_token:
            with allure.step(f"Фикстура TEARDOWN: пользователя с Token {user_token}"):
                BurgerMethods.delete_user(user_token)


@pytest.fixture
def user_cleaner_api():
    tokens = []
    yield tokens
    for token in tokens:
        if token:
            with allure.step("Фикстура TEARDOWN: Удаление созданного в тесте пользователя"):
                BurgerMethods.delete_user(token)


