# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

original_list = [12,'sadf', 5643]

list_of_nums = list(filter(lambda i: type(i) is int, original_list))
list_of_str = list(filter(lambda i: type(i) is str, original_list))

print(f'Числа: {list_of_nums}')
print(f'Строки: {list_of_str}')
