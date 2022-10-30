# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# with open('file_encode.txt', 'w') as data:
#     data.write('aaaaaaa555555        пппппппп')
#
# def rle_encode(data):
#     encoding = ''
#     prev_char = ''
#     count = 1
#
#     if not data: return ''
#
#     for char in data:
#         if char != prev_char:
#             if prev_char:
#                 encoding += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         encoding += str(count) + prev_char
#         return encoding
#
# def rle_decode(data):
#     decode = ''
#     count = ''
#     for char in data:
#         if char.isdigit():
#             count += char
#         else:
#             decode += char * int(count)
#             count = ''
#     return decode
#
# with open('file_encode.txt', 'r') as data:
#     in_data = data.readline()
#
# with open('file_decode.txt', 'w') as file:
#     encoded_data = rle_encode(in_data)
#     file.write(encoded_data)
#
# print(f'Original string  {in_data}')
# print(f'Encoded  string ', rle_encode(in_data))
# print(f'Decoded  string ', rle_decode(encoded_data))

def encode_message(message):
    encoded_string = ""
    i = 0
    while (i <= len(message) - 1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message) - 1):
            # '''if the character at the current index is the same as the character at the next index. If the characters are the same, the count is incremented to 1'''
            if (message[j] == message[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        # '''the count and the character is concatenated to the encoded string'''
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string


def decode(our_message):
    decoded_message = ""
    i = 0
    j = 0
    # splitting the encoded message into respective counts
    while (i <= len(our_message) - 1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        # displaying the character multiple times specified by the count
        for j in range(run_count):
            # concatenated with the decoded message
            decoded_message = decoded_message + run_word
            j = j + 1
        i = i + 2
    return decoded_message


def display():
    # the original string
    our_message = "ааааааа555555        пппппппп"
    # pass in the original string
    encoded_message = encode_message(our_message)
    # pass in the decoded string
    decoded_message = decode(encoded_message)
    print("Original string: [" + our_message + "]")
    print("Encoded string: [" + encoded_message + "]")
    print("Decoded string: [" + decoded_message + "]")


display()
