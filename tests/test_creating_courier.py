import requests
import allure


class TestCreatingCourier:
    @allure.title('Создание курьера')
    def test_create_courier_correct_data_create_successfull(self, register_new_courier):

        courier = register_new_courier 
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data = courier)

        r = response.json()
        
        assert response.status_code == 201 and r['ok'] is True


    @allure.title('Нельзя создать двух одинаковых курьеров с одинаковыми логинами')
    def test_create_courier_duplicate_data_creation_impossible(self, register_new_courier):

        courier = register_new_courier 
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data = courier)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data = courier)

        r = response.json()

        assert response.status_code == 409 and r['message'] == "Этот логин уже используется"


    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login_creation_impossible(self, register_new_courier_without_login):

        courier = register_new_courier_without_login 
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data = courier)

        r = response.json()

        assert response.status_code == 400 and r['message'] == "Недостаточно данных для создания учетной записи"    