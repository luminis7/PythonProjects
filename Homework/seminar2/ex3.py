# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

from random import randint

n = int(input('Введите число: '))

list = [i for i in range(-n, n)]

indexs = [randint(0, n-1) for i in range(5)]

product = 1
for i in indexs:
    product *= list[i]

print(list)
print(indexs)
print(product)