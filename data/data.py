import random


class PersonData:
    user_name = 'Сергей'
    login = 'sergei_egorushkin20343@yandex.ru'
    password = 't123123T!'


class ValidData:
    user_name = 'Test test'
    login = f"Test_test{random.randint(10, 999)}@yandex.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"
