# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file_encode.txt', 'w') as data:
    data.write('aaaaaaa555555        пппппппп')


def rle_encode(data):
    encoding = ''
    i = 0

    while i <= len(data) - 1:
        count = 1
        char = data[i]
        j = i
        while j < len(data) - 1:
            if data[j] == data[j + 1]:
                count += 1
                j += 1
            else:
                break
        encoding = encoding + str(count) + char
        i = j + 1
    return encoding


def rle_decode(data):
    decode = ''
    i = 0
    j = 0
    while (i <= len(data) - 1):
        run_count = int(data[i])
        run_word = data[i + 1]
        for j in range(run_count):
            decode = decode + run_word
            j += 1
        i += 2
    return decode  #


with open('file_encode.txt', 'r') as data:
    in_data = data.readline()

with open('file_decode.txt', 'w') as file:
    encoded_data = rle_encode(in_data)
    file.write(encoded_data)

print(f'Original string  {in_data}')
print(f'Encoded  string ', rle_encode(in_data))
print(f'Decoded  string ', rle_decode(encoded_data))
