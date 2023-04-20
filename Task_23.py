# Задача №23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает 
# количество элементов массива, больших предыдущего (элемента с предыдущим номером). 
# Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

from random import randint

n = int(input('Введите количество элементов в массиве: '))
arr = [randint(-9, 9) for i in range(n)]
count = 0
prev = arr[0]
print(arr)

for i in range(1, n):
    if arr[i] > prev:
        count += 1
        print(f'({prev} < {arr[i]})', end=" ")
    prev = arr[i]    
print(f'\nКоличество элементов, больших предыдущего: {count}')