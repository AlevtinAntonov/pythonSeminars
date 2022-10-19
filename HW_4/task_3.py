# 3) Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

import random

random_lst = []
lst_length = random.randint(10, 30)
for i in range(lst_length):
    random_lst.append(random.randint(0, 10))

print(f'Исходный список {random_lst}')
print(f'Cписок неповторяющихся элементов {list(x for i, x in enumerate(random_lst) if random_lst.count(x) == 1)}')
