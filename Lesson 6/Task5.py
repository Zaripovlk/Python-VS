# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:    Вывод:
# 300      220 284

# первый вариант
# number = 10000


# def friendlyNumber(num):
#         out=0
#         for div in range(1, int(num/2+1)):
#             if num%div==0:
#                 out+=div
#         return out


# for current_num in range (2, number):
#     m=friendlyNumber(current_num)
#     n=friendlyNumber(m)     
#     if n==current_num and n <m:
#         print(n,' ',m)

# второй вариант
def sum_div(n):
    res = 0
    for i in range(1, n/2):
        if n % i == 0:
            res += i
    return res

# третье решение

# k = 300
# for i in range(1, k):
#     for j in range(i + 1, k):
#         if sum_div(j) == i and sum_div(i) == j:
#             print(i, j)


# def sum_div(n):
#     res = 1  # Инициализация результата с 1, так как 1 делитель у любого числа
#     i = 2    # Начинаем с 2, так как 1 уже включено в сумму
#     while i * i <= n:
#         if n % i == 0:
#             res += i
#             if i != n // i:  # Проверяем, чтобы не учитывать квадратный корень дважды
#                 res += n // i
#         i += 1
#     return res

# k = 10000
# div_sum = [sum_div(n) for n in range(k)]  # Заранее вычисляем суммы делителей для всех чисел до k

# for i in range(1, k):
#     if div_sum[i] < k and i != div_sum[i] and div_sum[div_sum[i]] == i:
#         print(i, div_sum[i])