"""
Задача №1. Написать программу для копирования массива.
"""
from copy import deepcopy


def copy_mas(array: list) -> list:  # Функция возвращает копию входящего массива
    new_arr = deepcopy(array)
    return new_arr


def test_copy_mas():  # Функция для тестовых данных
    list_1 = [1, 5.0, 'hello', -8, 'Geek']
    new_list = copy_mas(list_1)
    if list_1 == new_list:
        print('TEST №1 - TRUE')
    else:
        print('TEST №1 - FALSE')

    list_2 = ['1,3,4', True, 12, 90.9, 56, -9, 13, 59, -92.8, 'HI', [], 'world', 9.7]
    list_new = copy_mas(list_2)
    if list_2 == list_new:
        print('--------------')
        print('TEST №2 - TRUE')
        print('--------------')
    else:
        print('--------------')
        print('TEST №2 - FALSE')
        print('--------------')

    list_3 = []
    list_new_3 = copy_mas(list_3)
    if list_3 == list_new_3:
        print('--------------')
        print('TEST №3 - TRUE')
        print('--------------')
    else:
        print('--------------')
        print('TEST №3 - FALSE')
        print('--------------')


test_copy_mas()
