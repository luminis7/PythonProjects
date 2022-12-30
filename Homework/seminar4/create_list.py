from random import randint

def create_list():
    list_len = int(input('Введите число, равное длине списка: '))
    min = int(input('Введите минимальное значение в списке: '))
    max = int(input('Введите максимальное значение в списке: '))
    new_list = [randint(min, max) for i in range(list_len)]
    return new_list
