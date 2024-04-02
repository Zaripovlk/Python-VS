# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
import random
import os
os.system('cls' if os.name == 'nt' else 'clear')
# def revers_value(N):
#     num = input ("введите число: ")
#     if N==1:
#         return num
#     return revers_value(N-1)+ num

# print(revers_value(3))
def revers_value(N):
    num = str(random.randint(1, 99))
    if N==1:
        return num
    return revers_value(N-1)+ f' {num} '

print(revers_value(3))

# def reverse(arr):
#     if len(arr) > 0:
#         print(arr[-1], end=" ")
#         reverse(arr[:-1])
#     pass


# n = [3, 4, 5, 7]
# reverse(n)

# def num(n):
#     if n == 0:
#         return
#     admin = int(input())
#    num(n - 1)
#     print(admin)

# n = int(input("Введите количество элементов последовательности: "))
# print("Введите последовательность:")
# num(n)