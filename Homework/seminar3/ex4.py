# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def bynary_number(n):
    list = []
    answer = ""
    if n == 0:
        return "0"
    while n > 1:
        list.insert(0, n % 2)
        n = n // 2
    list.insert(0, 1)
    
    for i in list:
        answer += str(i)+""

    return answer

n = int(input('Введите число: '))

print(bin(n)) #для самопроверки
print(f'Двоичное представление числа {n} равно {bynary_number(n)}')



