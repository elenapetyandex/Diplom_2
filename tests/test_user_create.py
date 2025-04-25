
import allure

from api_methods import ApiMethods
import pytest

from data import Data


class TestUserCreate:

    @allure.title('Проверка получения кода ответа 200 и accessToken,refreshToken в теле ответа при создании пользователя с уникальными данными методом POST /api/auth/register.')
    def test_create_unique_user_get_status_200(self, get_create_user):
        response = get_create_user
        assert response.status_code == 200 and response.json()["accessToken"] and response.json()["refreshToken"] and response.json()["success"] is True and response.json()["user"]

    @allure.title('Проверка возвращения кода 403 при создании пользователя, который уже зарегистрирован методом POST /api/auth/register.')
    def test_create_user_when_user_registered_get_status_403(self, get_create_user):
        response_1 = get_create_user

        try:                                                  #добавила этот блок try, чтобы в случае ошибки первой регистрации, увидеть это
            body = {
                "email": response_1.json()["user"]["email"],
                "password": Data.user_password,
                "name": response_1.json()["user"]["name"]
            }
            result = ApiMethods.create_user(body)
            assert result.status_code == 403 and result.json()["success"] is False and result.json()["message"] == Data.message_user_exist

        except KeyError as e:
            print(f'Error of first registration {e}')


    @allure.title('Проверка возвращения кода 403 при не заполненных обязательных полях методом POST /api/auth/register.')
    @pytest.mark.parametrize('email,password,name', Data.data_without_required_field_user_create)
    def test_create_user_without_required_field_get_403(self,email, password, name):
        body = {
            "email": email,
            "password": password,
            "name": name
        }
        response = ApiMethods.create_user(body)
        assert response.status_code == 403 and response.json()["success"] is False and response.json()["message"] == Data.message_required_fields
