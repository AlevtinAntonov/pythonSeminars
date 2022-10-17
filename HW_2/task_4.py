# 4 – Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся
# в файле file.txt в одной строке одно число.
import random

n = int(input('Введите число n : '))
res = []
for _ in range(n):
    res.append(random.randint(-n, n))
print(res)

with open('file.txt', 'r') as position:
    product = 1
    for line in position:
        if int(line) < n:
            product *= res[int(line)]
print(f'Произведение элементов на указанных в file.txt позициях =  {product}')
