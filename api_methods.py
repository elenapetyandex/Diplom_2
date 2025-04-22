import allure
import requests
import urls


class ApiMethods:
    @staticmethod
    @allure.step('Создать пользователя')
    def create_user(body):
        return requests.post(urls.create_user_url, data=body)

    @staticmethod
    @allure.step('Логин пользователя')
    def login_user(body):
        return requests.post(urls.login_url, data=body)



    @staticmethod
    @allure.step('Удалить пользователя')
    def delete_user(access_token):
        return requests.delete(urls.delete_user, headers={'Authorization': access_token})

    @staticmethod
    @allure.step('Изменить данные пользователя')
    def patch_user(access_token, updated_data):
        return requests.patch(urls.patch_user, headers={'Authorization': access_token}, data=updated_data)

    @staticmethod
    @allure.step('Создать заказ')
    def create_order(access_token, order_data):
        return requests.post(urls.create_order, headers={'Authorization': access_token}, data=order_data)

    @staticmethod
    @allure.step('Получить заказ конкретного пользователя')
    def get_order_list(access_token):
        return requests.get(urls.create_order, headers={'Authorization': access_token})

