# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

string = input("Введите строку:").split()

result = dict()

for i in string:
    if i in result.keys():
        print(f'{i}_{result[i]}', end=" ")
        result[i] += 1
    else:
        print(i, end= " ")
        result[i] = 1

# list_1 = 'a a a b c a a d c d d'
# input_list = list_1.split()

# a = ''
# dict_1 = {}
# for i in input_list:
#     a += i
#     if i in dict_1:
#         dict_1[i] += 1
#         a += f'_{dict_1[i]}'
#     else:
#         dict_1[i] = 0
#     a += ' '

# print(a)
        
# # string = input("Введите строку:").split()

# # result = dict()

# # for i in string:
# #     if i in result.keys():
# #         print(f'{i}_{result[i]}', end=" ")
# #         result[i] += 1
# #     else:
# #         print(i, end= " ")
# #         result[i] = 1


# string = input("Введите строку:").split()

# result = dict()
# new_result = ""
# for i in string:
#     if i in result.keys():
#         new_result += f"{i}_{result[i]}"
#         result[i] += 1
#     else:
#         new_result += i
#         result[i] = 1
#     new_result += " "
# print(new_result)



# string = input("Введите строку:").split()

# result = dict()
# new_result = []
# for i in string:
#     if i in result.keys():
#         new_result.append(f"{i}_{result[i]}")
#         result[i] += 1
#     else:
#         new_result.append(i)
#         result[i] = 1
    
# print(" ".join(new_result))



# # string = input("Введите строку:").split()

# # result = dict()

# # for i in string:
# #     if i in result.keys():
# #         print(f'{i}_{result[i]}', end=" ")
# #         result[i] += 1
# #     else:
# #         print(i, end= " ")
# #         result[i] = 1


# string = input("Введите строку:").split()

# result = dict()
# new_result = ""
# for i in string:
#     if i in result.keys():
#         new_result += f"{i}_{result[i]}"
#         result[i] += 1
#     else:
#         new_result += i
#         result[i] = 1
#     new_result += " "
# print(new_result)



# string = input("Введите строку:").split()

# result = dict()
# new_result = []
# for i in string:
#     if i in result.keys():
#         new_result.append(f"{i}_{result[i]}")
#         result[i] += 1
#     else:
#         new_result.append(i)
#         result[i] = 1
    
# print(" ".join(new_result))



# string = input("Введите строку:").split()

# result = dict()
# new_result = []
# for i in string:
#     if i in result.keys():
#         new_result.append(f"{i}_{result[i]}")
#         result[i] += 1
#     else:
#         new_result.append(i)
#         result[i] = 1
    
# print(*new_result)
        
#  text = "a a a b c a a d c d d"
# new_text = ""
# for letter in text.split(" "):
#     counter = 0
#     for find_letters in new_text:
#         if find_letters == letter:
#             counter +=1
#     if counter > 0:
#         new_text = new_text + letter + "_" + str(counter) + " "
#     else:
#         new_text = new_text + letter + " "

# print(new_text)

