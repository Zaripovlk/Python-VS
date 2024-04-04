# # Дан массив, состоящий из целых чисел. Напишите
# # программу, которая в данном массиве определит
# # количество элементов, у которых два соседних и, при
# # этом, оба соседних элемента меньше данного. Сначала
# # вводится число N — количество элементов в массиве 
# # Далее записаны N чисел — элементы массива. Массив
# # состоит из целых чисел.
# # Ввод: Ввод:
# # 5            5
# # 1 2 3 4     5 1 5 1 5 1
# # Вывод:      Вывод:
# # 0            2

# import random
# def list_creation(num):
#     list = []
#     for i in range (0, num):
#         list.append(random.randint(1, 10))
#     return list 

# def element_comparison(list_1):
#     list = []
#     counter = 0
#     i = 0
#     while i < len(list_1):    
#         left_num = list_1[i-1]
#         middle_num = list_1[i]
#         right_num = list_1[i-len(list_1)+1]
#         i += 1
#         if left_num < middle_num > right_num:
#             counter += 1
#     return counter

# n = int(input("Введите кол-во элементов массива: "))
# list_1 = list_creation(n)
# print(list_1)
# counter = element_comparison(list_1)
# print(counter)

# Решение с рекурсией
import random


def create_arr(length):
    return [random.randint(0, 99) for _ in range(length)]


def count(arr):
    counter = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            counter += 1
    return counter


def recurs(arr):
    if len(arr) <= 2:
        return 0
    counter = 0
    if arr[1] > arr[0] and arr[1] > arr[2]:
        counter += 1
    return counter + recurs(arr[1:])


arr = create_arr(16)
print(arr)
print("С помощью рекурсии:", recurs(arr))
print("С помощью цикла:", count(arr))