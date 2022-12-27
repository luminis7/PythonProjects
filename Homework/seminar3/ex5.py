# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))
def fibonacci(n):
    if n == 0:
        return 0

    list = [0,1]

    for i in range(2, n+1):
        list.append(list[i-1] + list[i-2])

    for i in range(1, n+1):
        list.insert(0, list[1]-list[0])

    return list

print(fibonacci(n))