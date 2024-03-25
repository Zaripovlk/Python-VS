# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_1 = [12, 7, -1, 21, 0]
k = 3
for _ in range(k):
    temp = list_1.pop() 
    list_1.insert(0, temp) 
print(list_1)

# list = [1, 2, 3, 4, 5]
# k = 3
# if k > len(list):
#     k = k % len(list)
# print(list[-k:] + list[:-k])


# numbers = [1, 2, 3, 4, 5]
# k = 3


# # Выполняем циклический сдвиг
# shifted_numbers = numbers[k:] + numbers[:k]

# print("После сдвига:", shifted_numbers)

# temp_days = [20,30,-1,1,4,7]
# k=int(input())
# temp_days = temp_days[k:]+temp_days[:-k]
# print(temp_days)