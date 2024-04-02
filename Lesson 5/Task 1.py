# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1= 1,
#  ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# 0 1 1 2 3 5 8 13 21
def fibonacci(N):
    if N <= 1:
        return N
    return fibonacci (N-1)+ fibonacci(N-2) 

for i in range(10):
    print (fibonacci(i), end = " ")

