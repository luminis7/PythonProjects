# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)
from random import randint

total_number = 120

while(total_number >0):
    players_turn = int(input('Введите число конфет от 1 до 28: '))
    if(players_turn > 28):
        print('Вы взяли слишком много')
        players_turn = int(input('Введите число конфет от 1 до 28 еще раз: '))
        total_number -= players_turn
    else:
        total_number -= players_turn
    print(f'Вы взяли {players_turn} конфет. Осталось {total_number} конфет')

    if (total_number == 0):
        print('Вы победили!')

    elif(total_number > 28):
        if(total_number < 58):
            b = total_number - 29
        else:
            b = randint(1, 28)
        total_number -= b
        print(f'Компьютер взял {b} конфет, осталось {total_number} конфет')

    else:
        b = total_number
        total_number -= b
        print(f'Компьютер взял {b} конфет, осталось {total_number} конфет. Победа компьютера')
