# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

num = int(input('Введите число: '))

# def check_prime_number Вспомогательная функция для проверки, простое ли нужное число
def check_prime_number(num):
    count = 0
    for i in range(1,num//2+1):
        if num % i ==0:
            count += 1
    return True if count == 1 else False

# def finding_prime_factors ищет возможные простые множители
def finding_prime_factors(num):
    list_of_prime_factors = []
    for i in range (2, num//2+1):
        if num % i == 0:
            if check_prime_number(i) == True:
                list_of_prime_factors.append(i)
    if len(list_of_prime_factors) == 0:
        list_of_prime_factors.append(1)  
        list_of_prime_factors.append(num)    
    return list_of_prime_factors
print(f'Простые множители числа {num}: {finding_prime_factors(num)}')

# def prime_factors раскладывает число на простые множители, пробегаясь по списку из def finding_prime_factors
def prime_factors(num):
    list_of_prime_factors = []
    if finding_prime_factors(num) != [1, num]:
        for i in finding_prime_factors(num):
            while i <= num:
                if num % i == 0:
                    if check_prime_number(i) == True:
                        list_of_prime_factors.append(i)
                        num = num / i
                else:
                    break
    else:
        list_of_prime_factors = [1, num]
    return list_of_prime_factors

print(f'Число {num} можно представить как произведение {" * ".join(map(str,prime_factors(num)))}')

# Ниже функция по разложению на простые множители работает сама по себе, без предварительного списка от finding_prime_factors
#
# def self_prime_factors(num):
#     list_of_prime_factors = []
    
#     for i in range(2, num+1):
#         while i <= num:
#             if num % i == 0:
#                 if check_prime_number(i) == True:
#                     list_of_prime_factors.append(i)
#                     num = num / i
#             else:
#                 break
#     if len(list_of_prime_factors) == 1:
#         list_of_prime_factors.insert(0, 1)
#     return list_of_prime_factors
# print(f'Число {num} можно представить как произведение {" * ".join(map(str,self_prime_factors(num)))}')