import requests
from data.urls import Urls
import allure
from helpers.helpers import generate_order_data


class BurgerMethods:

    @staticmethod
    @allure.step("Отправка POST-запроса на создание пользователя")
    def create_user(payload):
        return requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=payload)
    
    @staticmethod
    @allure.step("Отправка POST-запроса на авторизацию пользователя")
    def login_user(payload):
        return requests.post(Urls.BASE_URL + Urls.LOGIN_USER, json=payload)
    
    @staticmethod
    @allure.step("Отправка DELETE-запроса на удаление пользователя")
    def delete_user(accessToken):
        headers = {"Authorization": accessToken}
        return requests.delete(Urls.BASE_URL + Urls.DELETE_USER,headers=headers)
    
    @staticmethod
    @allure.step("Отправка POST-запроса на создание заказа")
    def create_order(payload=None,accessToken=None):
        if payload is None:
            payload = generate_order_data()
        headers = {}
        if accessToken:
            headers["Authorization"] = accessToken
        return requests.post(Urls.BASE_URL + Urls.ORDER, json=payload, headers=headers)
    