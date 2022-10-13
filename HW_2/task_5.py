# 5 – Реализуйте алгоритм перемешивания списка.
import random

n = int(input('Введите длину списка n : '))
lst = []
for _ in range(n):
    lst.append(random.randint(0, 1000))
print('Исходный список: ', lst)
random.shuffle(lst)
print('Перемешанный исходный список: ', lst)

# copy_lst = lst[:] # копия списка для перемешивания
# print('Исходный список: ', lst)
# random.shuffle(copy_lst)
# print('Перемешанный список: ', copy_lst)
