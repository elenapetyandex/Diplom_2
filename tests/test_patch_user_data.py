from os import access

import allure
import pytest

from api_methods import ApiMethods
from data import Data


class TestPatchUserData:
    @allure.title('Получение кода 200 при изменении имени залогиненого пользователя с корректно заполненными данными.')
    @pytest.mark.parametrize('name', Data.names_for_patch_user )
    def test_patch_logined_user_name_with_required_data_correct_get_200(self, get_access_token, name):
        access_token = get_access_token
        updated_data = {"name": name}
        response = ApiMethods.patch_user(access_token, updated_data)

        assert response.status_code == 200 and response.json()["success"] is True and response.json()["user"]["name"] == name

    @allure.title('Получение кода 200 при изменении почты залогиненого пользователя с корректно заполненными данными.')
    @pytest.mark.parametrize('email', [Data.user_email])
    def test_patch_logined_user_email_with_required_data_correct_get_200(self, get_access_token, email):
        access_token = get_access_token
        updated_data = {"email": email}
        response = ApiMethods.patch_user(access_token, updated_data)

        assert response.status_code == 200 and response.json()["success"] is True and response.json()["user"]["email"] == email

    @allure.title('Получение кода 200 при изменении имени и почты залогиненого пользователя.')
    @pytest.mark.parametrize('email, name', [[Data.user_email, Data.user_name]])
    def test_patch_logined_user_email_and_name_required_data_correct_get_200(self, get_access_token, email, name):
        access_token = get_access_token
        updated_data = {"email": email, "name": name}
        response = ApiMethods.patch_user(access_token, updated_data)

        assert response.status_code == 200 and response.json()["success"] is True and response.json()["user"]["email"] == email and response.json()["user"]["name"] == name

    @allure.title('Получение кода 403 при изменении почты залогиненого пользователя на зарегистрированную почту.')
    def test_patch_logined_email_to_registered_email_get_403(self, get_create_user, get_access_token):
        response = get_create_user
        email = response.json()["user"]["email"]
        access_token = get_access_token
        updated_data = {"email": email}
        response = ApiMethods.patch_user(access_token, updated_data)
        assert response.status_code == 403 and response.json()["success"] is False and response.json()["message"] == "User with such email already exists"

    @allure.title('Получение кода 401 при изменении имени незалогиненого зарегистрированного пользователя.')
    def test_path_name_not_logined_user_get_401(self, get_create_user):
        response = get_create_user
        access_token = response.json()["accessToken"]
        updated_data = {"name": Data.user_name}
        response_1 = ApiMethods.patch_user(access_token, updated_data)
        assert response_1.status_code == 401 and response_1.json()["success"] is False and response_1.json()["message"] == "You should be authorised"

    @allure.title('Получение кода 401 при изменении почты незалогиненого зарегистрированного пользователя.')
    def test_path_name_not_logined_user_get_401(self, get_create_user):
        response = get_create_user
        access_token = response.json()["accessToken"]
        updated_data = {"email": Data.user_email}
        response_1 = ApiMethods.patch_user(access_token, updated_data)
        assert response_1.status_code == 401 and response_1.json()["success"] is False and response_1.json()["message"] == "You should be authorised"

    @allure.title('Получение кода 401 при изменении почты незалогиненого незарегистрированного пользователя')
    def test_path_name_with_no_registered_user_get_401(self):
        access_token = None
        updated_data = {"email": Data.user_email}
        response = ApiMethods.patch_user(access_token, updated_data)
        assert response.status_code == 401 and response.json()["success"] is False and response.json()["message"] == "You should be authorised"

    @allure.title('Получение кода 401 при изменении имени незалогиненого незарегистрированного пользователя')
    def test_path_name_with_no_registered_user_get_401(self):
        access_token = None
        updated_data = {"name": Data.user_name}
        response = ApiMethods.patch_user(access_token, updated_data)
        assert response.status_code == 401 and response.json()["success"] is False and response.json()["message"] == "You should be authorised"



