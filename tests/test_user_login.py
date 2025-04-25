import allure
import pytest

from api_methods import ApiMethods
from data import Data


class TestUserLogin:
    email = None
    password = None
    name = None

    @classmethod
    def setup_class(cls):
        cls.email = Data.user_email
        cls.password = Data.user_password
        cls.name = Data.user_name

    def test_created_user_registrated_login_get_200(self):
        body = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }
        response = ApiMethods.create_user(body)
        body_1 = {
            "email": self.email,
            "password": self.password
        }
        response_login = ApiMethods.login_user(body_1)

        assert response_login.status_code == 200 and response_login.json()["success"] is True and response_login.json()["accessToken"] and response_login.json()["refreshToken"]

    def test_user_not_registrated_login_get_401(self):
        body_1 = {
            "email": self.email,
            "password": self.password
        }
        response_login = ApiMethods.login_user(body_1)
        assert response_login.status_code == 401 and response_login.json()["success"] is False and response_login.json()["message"] == Data.message_login_data_uncorrect

    @allure.title('Получение кода 401 при логине зарегистрированного пользователя с пустым полем email.')
    def test_user_registrated_with_empty_email_field_login_get_401(self):
        body = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }
        response = ApiMethods.create_user(body)
        body_1 = {
            "email": None,
            "password": self.password
        }
        response_login = ApiMethods.login_user(body_1)

        assert response_login.status_code == 401 and response_login.json()["success"] is False and response_login.json()["message"] == Data.message_login_data_uncorrect

    @allure.title('Получение кода 401 при логине зарегистрированного пользователя с пустым полем password.')
    def test_user_registrated_with_empty_password_field_login_get_401(self):
        body = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }
        response = ApiMethods.create_user(body)
        body_1 = {
            "email": self.email,
            "password": None
        }
        response_login = ApiMethods.login_user(body_1)

        assert response_login.status_code == 401 and response_login.json()["success"] is False and response_login.json()["message"] == Data.message_login_data_uncorrect

    @allure.title('Получение кода 401 при логине зарегистрированного пользователя с пустыми полями.')
    def test_user_registrated_with_empty_required_fields_login_get_401(self):
        body = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }
        response = ApiMethods.create_user(body)
        body_1 = {
            "email": None,
            "password": None
        }
        response_login = ApiMethods.login_user(body_1)

        assert response_login.status_code == 401 and response_login.json()["success"] is False and response_login.json()["message"] == Data.message_login_data_uncorrect

    @allure.title('Получение кода 200 при логине зарегистрированного пользователя после изменения почты.')
    def test_user_login_after_patch_email_get_200(self):
        body = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }
        ApiMethods.create_user(body)
        body_1 = {
            "email": self.email,
            "password": self.password
        }
        response_login = ApiMethods.login_user(body_1)
        token = response_login.json()["accessToken"]
        new_email = {"email": Data.user_email}
        response_patch = ApiMethods.patch_user(token, new_email)
        body_2 = {
            "email": new_email["email"],
            "password": self.password
        }
        response_login_2 = ApiMethods.login_user(body_2)
        assert  response_login_2.status_code == 200 and response_login.json()["success"] is True and response_login.json()["accessToken"] and response_login.json()["refreshToken"]


    @classmethod
    def teardown_class(cls):
        body_1 = {
            "email": cls.email,
            "password": cls.password
        }
        response_login = ApiMethods.login_user(body_1)
        if response_login.status_code == 200:
            token = response_login.json()["accessToken"]
            ApiMethods.delete_user(token)


