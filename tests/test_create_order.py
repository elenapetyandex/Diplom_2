import allure
import pytest

from api_methods import ApiMethods
from data import Data


class TestCreateOrder:
    data = [
        [Data.ingredients_id[0]],
        [Data.ingredients_id[0], Data.ingredients_id[1]],
        [Data.ingredients_id[4], Data.ingredients_id[6], Data.ingredients_id[7], Data.ingredients_id[10], Data.ingredients_id[13]]
    ]
    @allure.title('Получение кода 200 при создании заказа с корректным id ингредиентов методом POST /api/orders')
    @pytest.mark.parametrize('ingredient_list', data)
    def test_create_order_with_correct_ingredients_by_logined_user_get_200(self, get_access_token, ingredient_list):
        token = get_access_token
        order_data = {
            "ingredients": []
        }
        for ingredient in ingredient_list:
            order_data["ingredients"].append(ingredient)
        response = ApiMethods.create_order(token, order_data)
        assert response.status_code == 200 and response.json()["order"]["number"] and response.json()["success"] is True

    @allure.title('Получение кода 400 при создании заказа залогиненым пользователем без ингредиентов методом POST /api/orders')
    def test_create_order_without_ingredients_by_logined_user_get_400(self, get_access_token):
        token = get_access_token
        order_data = {
            "ingredients": []
        }
        response = ApiMethods.create_order(token, order_data)
        assert response.status_code == 400

    @allure.title('Получение кода 500 при создании заказа залогиненым пользователем с некорректным id ингредиентов методом POST /api/orders')
    def test_create_order_with_uncorrect_ingredient_by_logined_user_get_500(self, get_access_token):
        token = get_access_token
        order_data = {
            "ingredients": []
        }

        order_data["ingredients"].append(Data.not_correct_ingredient_id)
        response = ApiMethods.create_order(token, order_data)
        assert response.status_code == 500

    @allure.title('Получение кода 400 при создании заказа зарегистрированным незалогиненым пользователем методом POST /api/orders')
    def test_create_order_with_correct_ingredients_by_registrated_unlogined_user_not_created(self, get_create_user):
        response = get_create_user
        token = response.json()["accessToken"]
        order_data = {
            "ingredients": [Data.ingredients_id[0], Data.ingredients_id[1]]
        }
        response = ApiMethods.create_order(token, order_data)
        assert not response.status_code == 200

    @allure.title('Получение кода 400 при создании заказа без передачи параметра авторизации  методом POST /api/orders')
    def test_create_order_with_correct_ingredients_by_not_registrated_user_not_created(self):
        token = None
        order_data = {
            "ingredients": [Data.ingredients_id[0], Data.ingredients_id[1]]
        }
        response = ApiMethods.create_order(token, order_data)
        assert not response.status_code == 200