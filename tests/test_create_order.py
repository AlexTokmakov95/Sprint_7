import requests
import pytest
import allure
from urls import Urls

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
        
        with allure.step("Отправляем запрос на создание заказа"):
            response = requests.post(Urls.url_create_order, data = data_order) 

        r = response.json()
        
        assert response.status_code == 201 and "track" in r
