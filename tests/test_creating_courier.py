import requests
import allure
from urls import Urls


class TestCreatingCourier:
    @allure.title('Создание курьера')
    def test_create_courier_correct_data_create_successfull(self, register_new_courier):

        courier = register_new_courier 
        with allure.step("Отправляем запрос на создание курьера"):
            response = requests.post(Urls.url_create_courier, data = courier)

        r = response.json()
        
        assert response.status_code == 201 and r['ok'] is True


    @allure.title('Нельзя создать двух одинаковых курьеров с одинаковыми логинами')
    def test_create_courier_duplicate_data_creation_impossible(self, register_new_courier):

        courier = register_new_courier 
        
        with allure.step("Отправляем запрос на создание курьера"):
            response = requests.post(Urls.url_create_courier, data = courier)
        with allure.step("Отправляем повторный запрос на создание курьера с такими же данными"):
            response = requests.post(Urls.url_create_courier, data = courier)

        r = response.json()

        assert response.status_code == 409 and r['message'] == "Этот логин уже используется"


    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login_creation_impossible(self, register_new_courier_without_login):

        courier = register_new_courier_without_login 
        with allure.step("Отправляем запрос на создание курьера"):
            response = requests.post(Urls.url_create_courier, data = courier)

        r = response.json()

        assert response.status_code == 400 and r['message'] == "Недостаточно данных для создания учетной записи"  

    @allure.title('Нельзя создать курьера без пороля')
    def test_create_courier_without_password_creation_impossible(self, register_new_courier_without_password):

        courier = register_new_courier_without_password 
        with allure.step("Отправляем запрос на создание курьера"):
            response = requests.post(Urls.url_create_courier, data = courier)

        r = response.json()

        assert response.status_code == 400 and r['message'] == "Недостаточно данных для создания учетной записи"    