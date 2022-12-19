# (!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.


print('Введите значение X: ')
numX = int(input())

print('Введите значение Y: ')
numY = int(input())

print('Введите значение Z: ')
numZ = int(input())

print(not(numX or numY or numZ)) == (not numX and not numY and not numZ)
