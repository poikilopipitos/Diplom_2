from api_methods.burger_methods import BurgerMethods
import allure
from helpers.helpers import generate_user_data


@allure.epic("Регистрация и авторизация")
@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Успешная авторизация под существующим пользователем")
    def test_login_user_success(self,user_setup):
        payload = user_setup["payload"]
        response = BurgerMethods.login_user(payload)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["accessToken"]

    @allure.title("Ошибка авторизации при отправке неверного email")
    def test_login_user_with_invalid_login(self,user_setup):
        payload = user_setup["payload"]
        invalid_payload = {"email": payload['email'] + '123',"password": payload['password']}
        response = BurgerMethods.login_user(invalid_payload)
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()['message'] == "email or password are incorrect"
        
    @allure.title("Ошибка авторизации с неправильным паролем")
    def test_login_user_with_invalid_password(self,user_setup):
        payload = user_setup["payload"]
        invalid_payload = {"email": payload['email'],"password": payload['password'] + '123'}
        response = BurgerMethods.login_user(invalid_payload)
        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()['message'] == "email or password are incorrect"
