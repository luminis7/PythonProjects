# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и вывести многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 
# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h
#     a, b, c, d, e, h - рандом

from random import randint

k = int(input('Введите число: '))

list_of_coefficients = [randint(0,100) for i in range(k+1)]
list_of_power = [i for i in range(k, 1, -1)]

#Формируем список из всех необходимых значений polynominal_list
polynominal_list = []

for i in range(len(list_of_power)):
    polynominal_list.append(list_of_coefficients[i])
    polynominal_list.append('*x^')
    polynominal_list.append(list_of_power[i])
    polynominal_list.append('+')

polynominal_list.append(list_of_coefficients[-2])
polynominal_list.append('*x')
polynominal_list.append('+')
polynominal_list.append(list_of_coefficients[-1])

# И преобразуем его строку
polynominal_str = ''
for i in polynominal_list:
    polynominal_str += str(i)+''

print(polynominal_str)

