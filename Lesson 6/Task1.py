# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 17

# import random
# import os
# os.system('cls' if os.name == 'nt' else 'clear')
# def list_creation(num):
#     list = []
#     for i in range (0, num):
#         list.append(random.randint(1, 10))
#     return list 

# def comparison(list_1, list_2):
#     list = []
#     for num in list_1:
#         if num not in list_2:
#             list.append(num)
#     return list 

# n = int(input("Введите кол-во элементов массива n: "))
# m = int(input("Введите кол-во элементов массива m: "))
# list_1 = list_creation(n)
# list_2 = list_creation(m)
# print(list_1)
# print(list_2)
# list_3 = comparison(list_1, list_2)
# print(list_3)

def create_arr(st1):
    return [int(input(f"Введите {i+1} элемент: ")) for i in range(int(input(st1)))]


arr1 = create_arr("Число элементов массива 1: ")
arr2 = create_arr("Число элементов массива 2: ")

for el in arr1:
    if el not in arr2:
        print(el, end=" ")