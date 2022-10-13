# 5 – Реализуйте алгоритм перемешивания списка.
import random

n = int(input('Введите длину списка n : '))
lst = []
for _ in range(n):
    lst.append(random.randint(0, 1000))
copy_lst = lst[:]

print('Исходный список: ', lst)
random.shuffle(copy_lst)
print('Перемешанный список: ', copy_lst)
