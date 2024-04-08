# Напишите функцию same_by(characteristic, objects), которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция 
# должна возвращать True. Аргумент characteristic - это 
# функция, которая принимает объект и вычисляет его 
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
import os
os.system('cls' if os.name == 'nt' else 'clear')
def same_by(characteristic, objects):
    # Проверяем на пустой список
    if not objects:
        return True

    # Вычисляем характеристики для всех объектов
    characteristics = [characteristic(obj) for obj in objects]

    # Проверяем на одинаковость характеристик
    return len(set(characteristics)) == 1


# Список объектов
objects = [2, 4, 6, 8]

# Вызываем функцию и выводим результат
print(same_by(lambda x: x % 2, objects))

# #дополнительное решение
# def same_by(charac, objects):
#     return len(set(map(charac, objects))) in [0, 1]
