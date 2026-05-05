import requests
import allure

class TestLoginCourier:
    @allure.title('Авторизация под курьером выдает id')
    def test_login_courier_correct_data_login_successfull(self, register_new_courier_and_return_login_password):
        login_password = register_new_courier_and_return_login_password

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data = login_password)

        r = response.json()

        if 'id' in r:
            id_courier = r['id']
            print(f"Курьер успешно авторизован. ID: {id_courier}")
        else:
            print("ID не найден в ответе")
        
        assert response.status_code == 200 

    @allure.title('Ошибка при авторизации если не зполнить логин или пароль')
    def test_login_courier_without_login_login_impossible(self, register_new_courier_and_return_login_password):
        login_password = { 
            "login": '',
            "password": register_new_courier_and_return_login_password['password']
        }   

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data = login_password)

        r = response.json()

        assert response.status_code == 400 and r['message'] == "Недостаточно данных для входа"

    @allure.title('Ошибка при авторизации если логин или пароль не корректные')
    def test_login_courier_incorrect_login_login_impossible(self, register_new_courier_and_return_login_password):
        login_password = { 
            "login": '357',
            "password": register_new_courier_and_return_login_password['password']
        }   

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data = login_password)

        r = response.json()

        assert response.status_code == 404 and r['message'] == "Учетная запись не найдена"


