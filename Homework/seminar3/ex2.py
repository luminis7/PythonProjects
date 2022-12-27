# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# ! Для первой и второй задачи функция для создания списка содержится в файле create_list.py

from create_list import create_list
# исходный список
list1 = create_list()

# второй список
list2 = []

for i in range(len(list1)):
    if i < len(list1) / 2:
        list2.append(list1[i] * list1[(1+i)*(-1)])

print(list1)
print(list2)