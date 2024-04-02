# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
def revers(grades):
    max_grade = max(grades)
    min_grade = min(grades)
    list_1 = []
    for grade in grades:
        if grade == max_grade:
            list_1.append(min_grade)
        else:
            list_1.append(grade)
    return list_1
grades = [1,5,4,5,3]
result = revers(grades)
print(result)

# def find_max(list):
#     max=list[0]
#     for i in range(len(list)):
#         if list[i]>max:
#             max=list[i]
#     return max
# def find_min(list):
#     min=list[0]
#     for i in range(len(list)):
#         if list[i]<min:
#             min=list[i]
#     return min
# def change(list):
#     max=find_max(list)
#     min=find_min(list)
#     for i in range(len(list)):
#         if list[i]==max:
#             list[i]=min
#     return list
# list=[1, 3, 3, 3, 4]
# print(list)
# print(change(list))
