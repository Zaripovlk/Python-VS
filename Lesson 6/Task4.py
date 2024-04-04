# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:        Вывод:
# 1 2 3 2 3      2

# import random
# def list_creation(num):
#     list = []
#     for i in range (0, num):
#         list.append(random.randint(1, 10))
#     return list 

# def element_comparison(list_1):
#     list = []
#     counter = 0
#     # 1 2 3 2 3
#     for i in range(len(list_1)):
#         for j in range(i+1, len(list_1)):
#             if list_1[i] == list_1[j]:
#                 counter += 1
#     return counter 

# n = int(input("Введите кол-во элементов массива: "))
# list_1 = list_creation(n)
# print(list_1)
# counter = element_comparison(list_1)
# print(counter)


def count(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                count += 1
    return count

def recursive(numbers):
    if len(numbers) <= 1:
        return 0
    first_num = numbers[0]
    rest_nums = numbers[1:]
    count = 0
    for i in rest_nums:
        if first_num == i:
            count += 1
    return count + recursive(rest_nums)

arr = [1, 2, 3, 2, 2, 2, 2, 3, 3]
print(recursive(arr))
print(count(arr))
