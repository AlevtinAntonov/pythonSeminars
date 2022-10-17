# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
#
#  Пример:
#
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [2, 3, 5, 9, 3]
# 1 variant
sum_odd_elements = 0

for i in lst[1::2]:
    sum_odd_elements += i

print('1 вариант: ', sum_odd_elements)

# 2 variant
sum_odd = print('2 вариант: ', sum(y for x, y in enumerate(lst) if x % 2 != 0))
