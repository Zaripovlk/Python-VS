# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# dc = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":" S007 "}]
# print({list(slovar.values())[0].strip() for slovar in dc}) первое решение


# dict_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# dict_2 = set()
# # Проходим по каждому словарю в списке
# for dictionary in dict_1:
#     # Проходим по каждому значению в словаре
#     for value in dictionary.values():
#         # Добавляем значение в множество
#         dict_2.add(value.strip())
# print(dict_2) второе решение

# https://tproger.ru/explain/python-dictionaries словари почитать