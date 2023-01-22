#  Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

str_of_nums = input('Введите целые числа черeз пробел: ')

str_to_lst = str_of_nums.split()

lst_to_int = list(map(int, str_to_lst))

list_of_double_digits = list(filter(lambda i: 9 < i < 100, lst_to_int))

print(str_to_lst)
print(lst_to_int)
print(f'Вы ввели следующие двузначные числа: {list_of_double_digits}')
