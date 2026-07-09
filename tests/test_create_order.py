from api_methods.burger_methods import BurgerMethods
import allure
from helpers.helpers import generate_order_data

@allure.epic("Работа с заказами")
@allure.feature("Создание заказа")
class TestCreateOrder:


    @allure.title("Успешное создание заказа авторизованным пользователем")
    def test_create_order_authorized_user(self,user_setup):
        token = user_setup["accessToken"]
        response = BurgerMethods.create_order(accessToken=token)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["order"]

    @allure.title("Успешное создание заказа неавторизованным пользователем")
    def test_create_order_without_authorization(self):
        response = BurgerMethods.create_order()
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["order"]

    @allure.title("Успешное создание заказа с передачей списка ингредиентов")
    def test_create_order_with_ingredients(self):
        payload = generate_order_data()
        response = BurgerMethods.create_order(payload)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["order"]

    @allure.title("Ошибка создания заказа без ингредиентов (пустой список)")
    def test_create_order_without_ingredients(self):
        payload = {"ingredients": []}
        response = BurgerMethods.create_order(payload)
        assert response.status_code == 400
        assert response.json()["success"] is False
        
    @allure.title("Ошибка сервера (500) при передаче невалидного хеша ингредиента")
    def test_create_order_with_invalid_ingredient_hash(self):
        payload = {"ingredients": ["123","321"]}
        response = BurgerMethods.create_order(payload)
        assert response.status_code == 500
        

