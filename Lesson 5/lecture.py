#Задача: Необходимо создать функцию sumNumbers(n), которая будет считать
# сумму всех элементов от 1 до n.
import os
os.system('cls' if os.name == 'nt' else 'clear')
# def sumnumbers(N):
#     summa=0
#     for i in range (1,N+1):
#         summa +=i
#     print(summa)
# sumnumbers(5)


# вариант с возвращением функции
# import os
# os.system('cls' if os.name == 'nt' else 'clear')
# def sum_numbers(n , y='hello'):
#     print (y)
#     summa=0
#     for i in range (1,n+1):
#         summa +=i
#     return (summa) # окончание функции. Видим по тому что принт ниже не пишет слово стоп
#     print ('stop')
# a = sum_numbers(5, 'qwert')

# print(a)

# Задача №2 Описываем функцию с неограниченым количеством оргументов
# def sum_str(*args):
#     res = ''
#     for i in args:
#         res+=i
#     return res
# print (sum_str('q', 'e', 'l'))
# print (sum_str('q', 'e'))

# модульность
# import modul # создали модуль в другом файле и вызвали его
# from modul import max1 # сразу же импортировали макс1 из модуля
# import modul as m1 # импортировали функцию модуль и переименовали ее для нашей программы в М1
# print(m1.max1(10,9))

# Задача №3 последовательность фибаначи на рекурсию
# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2) #рекурсия
# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i)) # вызов рекурсии
# print (list_1)

# Задача №4 на быструю сортировку.
# “Программирование это разбиение чего-то большого и невозможного на что-то
# маленькое и вполне реальное”
# Быстрая сортировка принадлежит такой стратегии, как “разделяй и властвуй”.
# Сначала рассмотрим пример, затем напишем программный код
# Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой
# должен отгадать. Согласитесь, что мы можем перебирать эти значения в случайном
# порядке, например: 32, 27, 60, 73… Да, мы можем угадать в какой-то момент, но что
# если мы обратиться к стратегии “разделяй и властвуй” Обозначим друзей, друг_1
# это Иван, который загадал число, друг_2 это Петр, который отгадывает. Итак
# начнем:
# Иван загадал число 77.
# Петр: Число больше 50? Иван: Да.
# Петр: Число больше 75? Иван: Да.
# Петр: Число больше 87? Иван: Нет.
# Петр: Число больше 81? Иван: Нет.
# Петр: Число больше 78? Иван: Нет.
# Петр: Число больше 76? Иван: Да
# Число оказалось в диапазоне 76 < x < 78, значит это число 77. Задача решена. На
# самом деле мы сейчас познакомились с алгоритмом бинарного поиска, который
# также принадлежит стратегии “разделяй и властвуй”. Давайте перейдем к
# обсуждению программного кода быстрой сортировки.

#пример быстрой сортировки
# def quick_sort(array):
#     if len(array) <=1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# # print (quick_sort([14,5,9,6,3,58,7,5,2,7]))
# print (quick_sort([10,5,2]))

# пример сортировки слиянием
def merge_sort(nums):
    if len(nums) >1:
        mid = len(nums) //2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j =k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k]= right[j]
                j+=1
            k+=1
        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1

list1 = [1,5,6,9,8,7,2,1,55,2,4]
merge_sort(list1)
print (list1)