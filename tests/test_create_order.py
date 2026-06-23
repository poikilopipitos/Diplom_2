from api_methods.burger_methods import BurgerMethods
import allure
from helpers.helpers import generate_order_data

@allure.epic("Работа с заказами")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа")
    def test_create_order_authorized_user(self,user_setup):
        token = user_setup["accessToken"]
        response = BurgerMethods.create_order(accessToken=token)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["order"]

    def test_create_order_without_authorization(self):
        response = BurgerMethods.create_order()
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["order"]

    def test_create_order_with_ingredients(self):
        payload = generate_order_data()
        response = BurgerMethods.create_order(payload)
        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["order"]
        
    def test_create_order_without_ingredients(self):
        payload = {"ingredients": []}
        response = BurgerMethods.create_order(payload)
        assert response.status_code == 400
        assert response.json()["success"] is False

    def test_create_order_with_invalid_ingredient_hash(self):
        payload = {"ingredients": ["123","321"]}
        response = BurgerMethods.create_order(payload)
        assert response.status_code == 500
        

