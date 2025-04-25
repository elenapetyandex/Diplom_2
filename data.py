import random
import string

from faker import Faker
class Data:
    fake = Faker()
    user_email = ''.join((random.choice(string.digits) for x in range(5))) + fake.email() # добавила строку, так как почта из библиотеки faker стала повторяться в БД
    user_password = fake.password()
    user_name = fake.name()

    data_without_required_field_user_create = [
        [None, None, None],
        [None, user_password, user_email],
        [user_email, user_password, None],
        [user_email, None, user_name]
    ]
    names_for_patch_user = ['George', 'Георгий']
    ingredients_id = [
        "61c0c5a71d1f82001bdaaa6d", # Флюоресцентная булка R2-D3
        "61c0c5a71d1f82001bdaaa6f", # Мясо бессмертных моллюсков Protostomia
        "61c0c5a71d1f82001bdaaa70", #  Говяжий метеорит (отбивная)
        "61c0c5a71d1f82001bdaaa71",  # Биокотлета из марсианской Магнолии
        "61c0c5a71d1f82001bdaaa72" , #"Соус Spicy-X"
        "61c0c5a71d1f82001bdaaa6e", # Филе Люминесцентного тетраодонтимформа
        "61c0c5a71d1f82001bdaaa73", # "Соус фирменный Space Sauce"
        "61c0c5a71d1f82001bdaaa74", # Соус традиционный галактический
        "61c0c5a71d1f82001bdaaa6c", # Краторная булка N-200i
        "61c0c5a71d1f82001bdaaa75", # Соус с шипами Антарианского плоскоходца
        "61c0c5a71d1f82001bdaaa76",  # Хрустящие минеральные кольца
        "61c0c5a71d1f82001bdaaa77", # "Плоды Фалленианского дерева"
        "61c0c5a71d1f82001bdaaa78", # "Кристаллы марсианских альфа-сахаридов"
        "61c0c5a71d1f82001bdaaa79", # Мини-салат Экзо-Плантаго
        "61c0c5a71d1f82001bdaaa7a" # Сыр с астероидной плесенью
    ]

    not_correct_ingredient_id = "61c0c5a71d1f82001bdccc6d"
    message_authorization_error = "You should be authorised"
    message_email_exist = "User with such email already exists"
    message_user_exist = 'User already exists'
    message_required_fields = "Email, password and name are required fields"
    message_login_data_uncorrect = "email or password are incorrect"

