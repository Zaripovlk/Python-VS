# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
# import os
# os.system('cls' if os.name == 'nt' else 'clear')
# def is_prime(N):
#     for i in range(2,N//2): # выбрасываем половину стека
#         if N % i ==0:
#             return 'no'
#     return 'yes'
# print (is_prime(17))

# def func(n):   решение 
#     num = 2
#     while n % num != 0:
#         num += 1
#     return num == n

# print(func(6))
# import os
# os.system('cls' if os.name == 'nt' else 'clear')
# def is_prime(N):
#     if N%2 == 0:
#         return 'no'
#     for i in range(2,N//2): # выбрасываем половину стека
#         if N % i ==0:
#             return 'no'
#     return 'yes'
# print (is_prime(17))


def simple_number(number, dev=2):
    if number==dev:
           # print('yes')
            return 'yes'
    if number%dev==0:
            #print('no')
            return 'no'
    return simple_number(number, dev+1)
    

print (simple_number(15))