import pytest
from api_methods import ApiMethods
from data import Data


@pytest.fixture
def get_create_user():
    email = Data.user_email
    password = Data.user_password
    name = Data.user_name
    body = {
        "email": email,
        "password": password,
        "name": name
    }
    response = ApiMethods.create_user(body)

    yield response
    body_1 = {
        "email": email,
        "password": password
    }
    response_login = ApiMethods.login_user(body_1)
    if response_login.status_code == 200:
        token = response_login.json().get("accessToken")
        ApiMethods.delete_user(token)













@pytest.fixture
def get_access_token():
    email = Data.user_email
    password = Data.user_password
    name = Data.user_name
    body = {
        "email": email,
        "password": password,
        "name": name
    }
    ApiMethods.create_user(body)
    body_1 = {
        "email": email,
        "password": password
    }
    response_login = ApiMethods.login_user(body_1)
    token = response_login.json().get("accessToken")
    yield token
    ApiMethods.delete_user(token)



