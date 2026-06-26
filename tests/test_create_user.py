from helpers.helpers import generate_user_data
from api_methods.burger_methods import BurgerMethods
import allure

@allure.epic("Регистрация и авторизация")
@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Успешное создание уникального пользователя")
    def test_create_unique_user_success(self,user_cleaner_api):
        payload = generate_user_data()
        response = BurgerMethods.create_user(payload)
        data = response.json()
        user_cleaner_api.append(data.get("accessToken"))
        assert data.get("success") is True
        assert data.get("refreshToken") and data.get("accessToken") 
        
    #@allure.title("Ошибка при регистрации пользователя с уже существующим email")
    #def test_create_user_duplicate_email(self,user_cleaner_api):
    #    payload = generate_user_data()
    #    response_1 = BurgerMethods.create_user(payload)
    #    user_cleaner_api.append(response_1.json().get("accessToken"))
    #    response_2 = BurgerMethods.create_user(payload)
    #    assert response_1.status_code == 200 
    #    assert response_2.status_code == 403
    #    assert response_2.json()["success"] is False
    #    assert response_2.json()["message"] == "User already exists"



    @allure.title("Ошибка при регистрации пользователя с уже существующим email")
    def test_create_user_duplicate_email(self,registered_user):
        response = BurgerMethods.create_user(registered_user)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"


    @allure.title("Ошибка создания уникального пользователя, без указания email")
    def test_create_user_without_email(self):
        payload = generate_user_data()
        payload.pop('email')
        response = BurgerMethods.create_user(payload)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"
   
    @allure.title("Ошибка создания уникального пользователя, без указания пароля")
    def test_create_user_without_password(self):
        payload = generate_user_data()
        payload.pop('password')
        response = BurgerMethods.create_user(payload)
        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"