# 4) Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

import random

k = random.randint(2, 6)
dict_ = {
    0: "\u2070",
    1: "\u00B9",
    2: "\u00B2",
    3: "\u00B3",
    4: "\u2074",
    5: "\u2075",
    6: "\u2076",
    7: "\u2077",
    8: "\u2078",
    9: "\u2079"
}

lst_coefficient = []
for i in range(k):
    lst_coefficient.append(random.randint(0, 100))

print(f'{k=}, {lst_coefficient}')
lst = []
i = 1
while i <= k:
    lst = [str('x' + dict_[k]) + '+']

    while i - 1 <= k:
        lst = [str('x' + dict_[k - i])] + lst
        i+=1
    i += 1
print(lst)
