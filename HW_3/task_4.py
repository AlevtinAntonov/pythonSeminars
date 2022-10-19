# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
#  Пример:
#
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Введите десятичное число: '))
numb = ''

while num > 0:
    numb = str(num % 2) + numb
    num = num // 2

print(numb)

# 2 variant
num_2 = int(input('Введите десятичное число: '))
print(bin(num_2).replace("0b", ""))
