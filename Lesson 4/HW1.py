# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# Пример

# На входе:

import os
os.system('cls' if os.name == 'nt' else 'clear')

# var1 = "5 4" # количество элементов первого и второго множества
# var2 = "1 3 5 7 9" # элементы первого множества через пробел
# var3 = "2 3 4 5" # элементы второго множества через пробел
# На выходе:



# var1  = [int (num) for num in var1.split()]
# var2  = [int (num) for num in var2.split()]
# var3  = [int (num) for num in var3.split()]
# len1, len2 = var1
# result=[]
# for i in range (len1):
#     for j in range (len2):
#         if var2[i] == var3[j]:
#             result.append(var3[j])
# # result.sort() первый вариант сортировки
# # print (sorted(result)) второй вариант сортировки
# for i in range(len(result)-1):
#     if result[i] > result[i+1]:
#         result[i], result[i+1] = result[i+1], result [i]
# print (result) #первый вариант решения
var1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'
var2  = [int (num) for num in var2.split()]
var3  = [int (num) for num in var3.split()]
var2 = set(var2)
print (var2)
var3 = set(var3)
result = var2 & var3 
print(*sorted(result))