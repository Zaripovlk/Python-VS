# Ваня и Петя поспорили, кто быстрее решит 
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не 
# такими смышлеными. Никто из ребят не смог до 
# конца сделать это задание. Они решили так: у кого 
# будет меньше ошибок в коде, тот и выиграл спор. За 
# помощью товарищи обратились к Вам, студентам.

High=0
number = None
while number != 0 :
    number = int (input ("введите пол. число: "))
    if number > High:
        High = number
    # if number==0:
    #     break
print (High)

# n = None
# b = set()
# while n != 0:
#     n = int(input("Введите число: "))
#     if n > 0:
#         b.add(n)
#     else:
#         continue
# max_num = max(b)
# print(max_num)

# Задача 26:

def degree(a, b, c=1):
    if b==0:
        return c
    c=c*a
    return degree(a, b-1, c)

print(degree(2, 3))



# # Задача 27:

# # import math

# def sign(b):
#    if (b>0):
#       return 1
#    elif (b<0):
#       return -1
#    else:
#       return 0


# def sum(a, b):
#     sign_b=sign(b)
#    # sign_b = int(math.copysign(1, b))
#     if b==0:
#         return a
#     a+=sign_b
#     b-=sign_b
#     return sum(a, b)

# print(sum(2,2))
