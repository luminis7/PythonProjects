# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1, 1.2, 3.1, 5, 10.01, 8.76]

list2 = [round(i % 1, 2) for i in list1 if i % 1 != 0]
print(list2)

maxnum = list2[0]
for i in list2:
    if i > maxnum:
        maxnum = i

minnum = list2[0]
for i in list2:
    if i < minnum:
        minnum = i

difference = maxnum - minnum

# или через встроенные функции
# difference = max(list2) - min(list2)

print(difference)

