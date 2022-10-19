# 2) Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

import random

n = random.randint(2, 1000)
print(f'Задано натуральное число {n=}')

factors = []
i = 2
while i * i <= n:
    while n % i == 0:
        n //= i
        factors.append(i)
    i += 1
if n > 1:
    factors.append(n)

print(f'Список простых множителей -> {sorted(list(set(factors)))}')
