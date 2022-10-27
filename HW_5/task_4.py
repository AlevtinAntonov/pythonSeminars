# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file_encode.txt', 'w') as data:
    data.write('AAABBCCCC ddddFFFFjjjj LLLLuuuuuTTTTTAAAA')

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

with open('file_encode.txt', 'r') as data:
    in_data = data.readline()

with open('file_decode.txt', 'w') as file:
    encoded_data = rle_encode(in_data)
    file.write(encoded_data)

print(f'Original string  {in_data}')
print(f'Encoded  string ', rle_encode(in_data))
print(f'Decoded  string ', rle_decode(encoded_data))

