# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

# 1 | 2 | X
# 4 | X | O
# X | 8 | O


cells = [1,2,3,4,5,6,7,8,9]

def playing_field():
	for i in range(3):
		print ('',cells[i*3], '|', cells[1+i*3], '|', cells[2+i*3])

def check_win():
	# Проверяем победу одного из игроков
	win = False

	win_combination = (
		(0,1,2), (3,4,5), (6,7,8),	
		(0,3,6), (1,4,7), (2,5,8),
		(0,4,8), (2,4,6) 			
	)

	for i in win_combination:
		if (cells[i[0]] == cells[i[1]] == cells[i[2]]):
			win = cells[i[0]]

	return win

def game_step(index, char):
	
	if (index > 10 or index < 1 or cells[index-1] in ('X','O')):
		return False

	cells[index-1] = char
	return True

def start_game():
	players_turn = 'X'
	step = 1

	playing_field()

	while (step < 9) and (check_win() == False):
		index = input('Введите номер ячейки для ' + players_turn + ': ')

		if (game_step(int(index), players_turn)):

			if (players_turn == 'X'):
				players_turn = 'O'
			else:
				players_turn = 'X'

			playing_field()
			
			step += 1
		else:
			print('Неверный номер! Повторите!')

	if (step == 9):
		print('Игра окончена. Ничья!')
	else:
		print('Выиграл игрок ' + check_win())


start_game()