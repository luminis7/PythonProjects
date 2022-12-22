# 1) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

temp = int(input('Введите число: '))

def factorial(temp):
    factorial = 1
    for i in range(1, temp+1):
        factorial *=i
    return factorial

list = [factorial(i) for i in range(1, temp+1)]

print(f'Набор произведений чисел от 1 до {temp}: \n{list}')
