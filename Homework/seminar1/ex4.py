# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def coordinatesOfThePlane(num):
    if num == 1:
        print('x > 0, y > 0')
    elif num == 2:
        print('x < 0, y > 0')
    elif num == 3:
        print('x < 0, y < 0')
    elif num == 4:
        print('x > 0, y < 0')
    else:
        print('Значение находится за пределами возможных значений четверти')

print('Введите номер четверти: ')
number = int(input())

coordinatesOfThePlane(number)
