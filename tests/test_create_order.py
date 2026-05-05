import requests
import pytest
import allure

class TestCreateOrder:

    @pytest.mark.parametrize('color_data', [
        ['BLACK', ''],
        ['GREY', ''],
        ['BLACK', 'GREY'],
        []  
    ])
    @allure.title('Создание заказа')
    def test_create_order_with_different_color_data_create_successfull(self, color_data):
        data_order = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color_data
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data = data_order) 

        r = response.json()

        if 'track' in r:
            track_order = r['track']
            print(f"Заказ успешно создан. track: {track_order}")
        else:
            print("track не найден в ответе")
        
        assert response.status_code == 201 
