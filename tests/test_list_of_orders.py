import requests
import pytest
import allure
from urls import Urls

class TestListOfOrders:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_of_orders_correct_return_list_of_orders(self):

        with allure.step("Отправляем запрос на получение списка заказов"):
            response = requests.get(Urls.url_create_order)
    
        r = response.json()

        assert response.status_code == 200 and "orders" in r