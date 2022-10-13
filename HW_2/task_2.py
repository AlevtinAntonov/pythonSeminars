# 2 –Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# 1 вариант
# import math
#
# num = int(input('Введите целое число N : '))
# if num > 0:
#     set_of_product_of_numbers = [1]
#     for i in range(2, num + 1):
#         set_of_product_of_numbers.append(math.factorial(i))
#     print(f'Набор произведений чисел от 1 до {num} ', set_of_product_of_numbers)
# else:
#     print('Число должно быть больше 0')

# 2 вариант без import math

num = int(input('Введите целое число N : '))
if num > 0:
    set_of_product_of_numbers = [1]
    product = 1
    for i in range(2, num + 1):
        product *= i
        set_of_product_of_numbers.append(product)
    print(f'Набор произведений чисел от 1 до {num} ', set_of_product_of_numbers)
else:
    print('Число должно быть больше 0')
