# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
watermelon = int(input("Количество арбузов: "))

for i in range(watermelon): # повторять столько раз,сколько всего арбузов
    weight = int(input("Вес: "))
    if i == 0:
        min_num = weight
        max_num = weight
    elif weight < min_num:
        min_num = weight
    elif weight > max_num:
        max_num = weight
print(min_num, "теще")
print(max_num, "нам")

# n = int(input("Введите число арбузов: "))
# arr = [int(input()) for _ in range(n)]
# print("Мой арбуз весит: ", max(arr))
# print("Арбуз для тёщи весит: ", min(arr)) 
# Решение со списком