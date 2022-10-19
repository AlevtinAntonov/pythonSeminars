# 1) Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)
import random

num = random.uniform(1, 5)
degree = random.randint(-10, -1)
d = 10 ** degree

result = round(num, -degree)
print(f'Число {num=}, точность округления {d=} результат = ', result)
