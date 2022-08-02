"""
Задача №2 с элементами математики. Написать программу для операции "произведение массивов".
Сама операция определяется так, как будто элементы массива - это коэффициенты полинома.
Соответственно, произведение массивов - должно дать новый массив, коэффициенты которого соответствуют нужному полиному.
"""
import numpy as np


def prod_array(list_1: list, list_2: list):
    new_list = np.zeros(len(list_1) + len(list_2) - 1, dtype=int)
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            new_list[i + j] += list_1[i] * list_2[j]
    return new_list.tolist()


def test_prod_array():  # Функция для тестовых данных
    list_1 = [1, 2, 3, 4]
    list_2 = [0]
    new_list1 = prod_array(list_1, list_2)
    if new_list1 == [0, 0, 0, 0]:
        print('TEST №1 - TRUE')
    else:
        print('TEST №1 - FALSE')

    list_1 = [-1, 1]
    list_2 = [2, 1]
    new_list2 = prod_array(list_1, list_2)
    if new_list2 == [-2, 1, 1]:
        print('TEST №2 - TRUE')
    else:
        print('TEST №2 - FALSE')


test_prod_array()
