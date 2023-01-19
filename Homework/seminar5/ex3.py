# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"

with open("Homework/seminar5/file.txt", "r") as file:
    text = file.read()


def rle_encode(data):
    encoding_list = ''
 
    i = 0
    while i < len(data):
        count = 1
 
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count = count + 1
            i = i + 1
 
        encoding_list += str(count) + data[i]
        i = i + 1
 
    return encoding_list

def rle_decode(data):
    decoding_list = ''
    count = ''
    for i in range(0, len(data), 2):
        decoding_list +=  int(data[i]) * data[i+1]
        
    return decoding_list

print(f'Текст до кодировки: {text} \n')
print(f'Текст после кодировки: {rle_encode(text)} \n')

encode_text = rle_encode(text)
print(f'Раскодированный текст: {rle_decode(encode_text)}')
