# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

lst = [1, 2,  5, 1, 5, 3, 3, 10]

print(f'Исходный список {lst}')
print(f'Cписок неповторяющихся элементов {list(x for i, x in enumerate(lst) if lst.count(x) == 1)}')
print(f'Cписок повторяющихся элементов set {list(set(x for i, x in enumerate(lst) if lst.count(x) > 1))}')
print(f'Cписок без дубликатов  {list(i for n, i in enumerate(lst) if i not in lst[:n])}')
print(f'Cписок без дубликатов dict {list(dict.fromkeys(lst))}')