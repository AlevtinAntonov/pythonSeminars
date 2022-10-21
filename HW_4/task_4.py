# 4) Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

import random

k = random.randint(2, 6)
lst_coefficient = []
for i in range(k + 1):
    lst_coefficient.append(random.randint(0, 100))
print(f'{k=}, {lst_coefficient=}')

lst_coefficient.reverse()

polynom = '+'.join([f'{(j, "")[j == 1]}x^{i}' for i, j in enumerate(lst_coefficient) if j][::-1])
polynom = polynom.replace('x^0', '')
polynom = polynom.replace('x^1', 'x')
polynom = polynom + '=0'
print(polynom)
with open('file.txt', 'a') as file:
    data = '\n' + polynom
    file.write(data)


# import random
#
# k = random.randint(2, 6)
# dict_ = {
#     0: "\u2070",
#     1: "\u00B9",
#     2: "\u00B2",
#     3: "\u00B3",
#     4: "\u2074",
#     5: "\u2075",
#     6: "\u2076",
#     7: "\u2077",
#     8: "\u2078",
#     9: "\u2079"
# }
#
# lst_coefficient = []
# for i in range(k + 1):
#     lst_coefficient.append(random.randint(0, 100))
# print(f'{k=}, {lst_coefficient=}')
#
# lst_coefficient.reverse()
#
# polynom = '+'.join([f'{(j, "")[j == 1]}x{dict_[i]}' for i, j in enumerate(lst_coefficient) if j][::-1])
# polynom = polynom.replace(('x' + str(dict_[0])), '')
# polynom = polynom.replace(str(dict_[1]), '')
# polynom = polynom + '=0'
# print(polynom)
#
# with open('file.txt', 'ab') as file:
#     data = '\n' + polynom
#     file.write(data.encode('utf8'))
