import requests
import allure
from urls import Urls

class TestLoginCourier:
    @allure.title('Авторизация под курьером выдает id')
    def test_login_courier_correct_data_login_successfull(self, register_new_courier_and_return_login_password):
        login_password = register_new_courier_and_return_login_password

        with allure.step("Отправляем запрос на логин курьера"):
            response = requests.post(Urls.url_login_courier, data = login_password)

        r = response.json()

        assert response.status_code == 200 and "id" in r 

    @allure.title('Ошибка при авторизации если не зполнить логин или пароль')
    def test_login_courier_without_login_login_impossible(self, register_new_courier_and_return_login_password):
        login_password = { 
            "login": '',
            "password": register_new_courier_and_return_login_password['password']
        }   

        with allure.step("Отправляем запрос на логин курьера"):
            response = requests.post(Urls.url_login_courier, data = login_password)

        r = response.json()

        assert response.status_code == 400 and r['message'] == "Недостаточно данных для входа"

    @allure.title('Ошибка при авторизации если логин или пароль не корректные')
    def test_login_courier_incorrect_login_login_impossible(self, register_new_courier_and_return_login_password):
        login_password = { 
            "login": '357',
            "password": register_new_courier_and_return_login_password['password']
        }   

        with allure.step("Отправляем запрос на логин курьера"):
            response = requests.post(Urls.url_login_courier, data = login_password)

        r = response.json()

        assert response.status_code == 404 and r['message'] == "Учетная запись не найдена"


