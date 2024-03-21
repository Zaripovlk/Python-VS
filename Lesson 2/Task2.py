# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# def fib_for(n):
#     n1 = 0
#     n2 = 1
#     if n <= 0:
#         return 'Введите число больше 0'
#     elif n == 1:
#         return n1
#     elif n == 2:
#         return n2
#     else:
#         for i in range(2, n):
#             n1, n2 = n2, n1 + n2
#         return n2
# n = int(input("Введите целое  число: "))
# A= int(input("Введите целое  число A: "))
# a = 0
# b = 1
# i = 1
# while i <= n:
#     c = a + b
#     a = b
#     b = c
#     i += 1
#     if A == b:
#         print ("yes")
#     else: print(-1)
A = int(input("Введите число: "))
temp = 0
n1 = 1
n2 = 1
counter = 2  # Так как первые числа известны
while temp <= A:
    temp = n1 + n2 # сложили два последних
    n1 = n2 # перенесли предпоследнее
    n2 = temp # вместо предпоследнего записали последнее
    counter += 1
    if temp > A:
        counter = 0
if counter != 0:
    print(counter)
else:
    print(-1)


#     x = int(input("Введите число: "))
# a, b = 0, 1
# n = 1
# count = 1
# while n <= x:
#     n = a + b
#     a, b = b, n
#     count += 1
# if x == 1:
#     print(2,3)    
# elif x == 0:
#     print(1)   
# elif x == a:
#     print(count)
# else:
#     print(-1)
    
#     A=int(input())
# f1=0
# f2=1
# f3=1
# count=4
# while A>1: 
#     f4=f2+f3 #3 #8
#     f5=f3+f4 #5 #13
    
#     f2=f4
#     f3=f5
#     count=count+1
#     print(f4, f5)
#     if f5==A or f4==A:
#         print('Число фибоначи равно - ', A, 'и его порядковый номер - ',count)
#         break
#     if f4>A:
#         print("-1",count)
#         break