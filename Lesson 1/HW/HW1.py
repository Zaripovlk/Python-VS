# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.
# Пример:
# n = 123 -> res = 6 (1 + 2 + 3)
# n = 100 -> res = 1 (1 + 0 + 0)
n = int (input("введите число n:"))
res =n//100 + ((n//10)%10)+ n%10
print (res)

# второй способ
# n = str(n)
# res = int(n[0]) + int(n[1]) + int(n[2])