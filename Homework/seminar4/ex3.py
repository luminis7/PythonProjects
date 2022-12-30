# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
#  исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1
from create_list import create_list # функция создания списка в дополнительном файле

full_list = create_list()

print(f'Полный список: {full_list}')

def unique_items_of_list(list):
    unique_items = []
    
    for i in list:
        count = 0
        for j in list:
            if i == j:
                count +=1
        if count == 1:
            unique_items.append(i)
        
    return unique_items

print(f'Список уникальных элементов: {unique_items_of_list(full_list)}')
    
