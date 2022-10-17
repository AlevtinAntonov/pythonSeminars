# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.2

from decimal import *

lst = [1.1, 1.2, 3.1, 5, 10.01]
lst_fraction = []
getcontext().prec = 2

for i in lst:
    # lst_fraction.append(i % 1) # 1 variant
    lst_fraction.append(i - int(i))  # 2 variant

print(f'Разница :', Decimal(max(lst_fraction)) - Decimal(min(lst_fraction)))
