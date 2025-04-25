import allure
import pytest
import random

from api_methods import ApiMethods
from data import Data


class TestGetUserOrder:
    @allure.title('Получение пустого списка заказа залогиненным пользователем без заказов')
    def test_get_order_logined_user_without_order_get_order_list(self, get_access_token):
        token = get_access_token
        response = ApiMethods.get_order_list(token)
        assert response.status_code == 200 and response.json()["success"] is True and len(response.json()["orders"]) == 0

    @allure.title('Получение списка заказа залогиненным пользователем с заказами')
    @pytest.mark.parametrize('count_orders', [1, 10, 49, 50])
    def test_get_order_logined_user_with_orders_get_order_list(self, get_access_token, count_orders):
        token = get_access_token
        for _ in range(count_orders):
            order_data = {
                "ingredients": []
            }
            order_data["ingredients"].append(random.choice(Data.ingredients_id))
            ApiMethods.create_order(token, order_data)

        response = ApiMethods.get_order_list(token)
        assert response.status_code == 200 and response.json()["success"] is True and len(response.json()["orders"]) == count_orders

    @allure.title('Получение кода 401  зарегистрированным незалогиненым пользователем')
    def test_get_order_registered_not_logined_user_get_401(self, get_create_user):
        response = get_create_user
        token = response.json()["accessToken"]
        response_1 = ApiMethods.get_order_list(token)
        assert response_1.status_code == 401 and response_1.json()["success"] is False and response_1.json()["message"] == Data.message_authorization_error

    @allure.title('Получение кода 401 при отсутсвии токена авторизации')
    def test_get_order_not_user_get_401(self):
        token = None
        response_1 = ApiMethods.get_order_list(token)
        assert response_1.status_code == 401 and response_1.json()["success"] is False and response_1.json()["message"] == Data.message_authorization_error



