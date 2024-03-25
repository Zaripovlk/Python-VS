# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
list1 = [1, 1, 2, 0, -1, 3, 4, 4]
num = set(list1)
print(len(num))

# list_1 = [1, 1, 2, 2, 3, 3, 4, 4]
# result_list = list()
# for i in list_1: #для каждого элемента в list_1
#   if i not in result_list:
#     result_list.append(i)
# print(result_list)
# print(len(result_list))


# n = [1, 1, 2, 0, -1, 3, 4, 4]
# dct = dict()
# for el in n:
#     dct.setdefault(el, 0)
#     dct[el] += 1
# print(len(dct))

