# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.

# 2*x^2  + 4*x        5*x^2 + 2*x
#     7x^2 + 6x

# 2*x^6  + 4*x      5*x^2 + 2*x
#     2*x^6 + 5x^2 + 6x

data1 = '4*x^3+8*x^2+4*x+5'
data2 = '2*x^2+8*x+5'

str1 = data1.split('+')

data1_dictionary = {}
for i in range(len(str1)):
    data1_dictionary = {i: str1[i]}

str1[0].split('^')

print(str1)

print(data1_dictionary)

