import requests
import pytest
import allure

class TestListOfOrders:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_of_orders_correct_return_list_of_orders(self):

        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
    
        r = response.json()

        
        assert response.status_code == 200 and "orders" in r