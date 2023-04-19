# Задача 18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

n = int(input('Введите количество элементов в массиве: '))
array = [randint(1, 9) for i in range(n)]
print(array)

x = int(input('Введите число X от 1 до 10: '))
closest_diff = abs(array[0] - x)
closest_i = 0
flag = True

while flag: # проверка на правильность ввода числа X
    if 1 <= x < 10:
        flag = False
    else:
        x = int(input('Не корректное значение! Введите число X от 1 до 10: '))

for i in range(1, n):
    diff = abs(array[i] - x)
    if diff < closest_diff:
        closest_diff = diff
        closest_i = i
print(f'Cамый близкий по величине элемент к числу {x} -> {array[closest_i]}')