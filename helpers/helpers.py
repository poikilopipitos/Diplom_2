import random
import string
import allure


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

@allure.step("Генерация случайных данных для пользователя (email, пароль, имя)")
def generate_user_data():
    return {
'email': generate_random_string(10) + '@yandex.ru',
'password': generate_random_string(10),
'name': generate_random_string(10)}

def generate_order_data():
    return {"ingredients": ["61c0c5a71d1f82001bdaaa6c","61c0c5a71d1f82001bdaaa70","61c0c5a71d1f82001bdaaa72"]}