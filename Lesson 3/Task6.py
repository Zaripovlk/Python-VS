# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

arr=[0, -1, 5, 2, -5, -6, 12, 15, 18, 20, 25]
n=0
for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
        n=n+1
print(n)
