# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите число: ')

sum_of_digs = sum(map(int, filter(lambda i: i.isdigit(), num)))

print(f'Сумма цифр числа {num} равна {sum_of_digs}')