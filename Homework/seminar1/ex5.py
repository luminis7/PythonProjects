# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def definitionOfDistanse(x1, y1, x2, y2):
    distanse = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return round(distanse, 2)

print('Введите значение x1: ')
numX1 = int(input())

print('Введите значение y1: ')
numY1 = int(input())

print('Введите значение x2: ')
numX2 = int(input())

print('Введите значение y2: ')
numY2 = int(input())

print(f'Расстояние между точками ({numX1}, {numY1}) и ({numX2}, {numY2}) равно {definitionOfDistanse(numX1, numY1, numX2, numY2)}')