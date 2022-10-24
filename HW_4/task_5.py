# 5) Даны два файла, в каждом из которых находится запись многочлена.
#     Задача - сформировать файл, содержащий сумму многочленов.

from sympy import Symbol, collect
def convert(item):
    item = item.replace('=0', '')
    item = item.replace('x+', '*x+')
    item = item.replace('x^', '*x**')
    return item


with open('file_1.txt', 'r') as data_1:
    polynom_1 = data_1.readline()
with open('file_2.txt', 'r') as data_2:
    polynom_2 = data_2.readline()
print(f'Исходный многочлен из file_1.txt {polynom_1=}')
print(f'Исходный многочлен из file_2.txt {polynom_2=}')

polynom_1 = convert(polynom_1)
polynom_2 = convert(polynom_2)

x = Symbol('x')

result = str(collect(str(polynom_1) + '+' + str(polynom_2), x))
result = result.replace('**', '^')
result = result.replace('*', '')
result = result + '=0'

print(f'Сумма многочленов {result=}')

