# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.2

from decimal import *

lst = [1.1, 1.2, 3.1, 5, 10.01]
lst_fraction = []
getcontext().prec = 1

for i in lst:
    lst_fraction.append(Decimal(i % 1)) # 1 variant
    # lst_fraction.append(Decimal(i) - int(i))  # 2 variant

print(f'Разница :', max(lst_fraction) - min(lst_fraction))
