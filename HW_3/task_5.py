# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
#  Пример:
#
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://ru.wikipedia.org/wiki/Негафибоначчи
# #:~:text=В математике%2C числа негафибоначчи — отрицательно индексированные элементы
# # последовательности чисел Фибоначчи.)

num = int(input('Введите целое число: '))
# 1 variant
fib = [0, 1]

if num > 2:
    for i in range(2, num):
        fib.append(fib[i - 1] + fib[i - 2])

non_fib = [-1, 1]

for i in range(3, num):
    non_fib.insert(0, (-1) ** (i + 1) * fib[i])

print(f'Для k = {num} -> ', non_fib + fib)

# 2 variant
fibo_nums = []
a, b = 1, 1

for i in range(num - 1):
    fibo_nums.append(a)
    a, b = b, a + b

a, b = 0, 1

for i in range(num):
    fibo_nums.insert(0, a)
    a, b = b, a - b

print(f'Для k = {num} -> ', fibo_nums)
