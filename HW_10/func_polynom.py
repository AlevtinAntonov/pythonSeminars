import re
from sympy import Symbol, collect


def convert(item):
    item = re.sub(r'(\d)(x)', r'\1*\2', item)
    # item = item.replace('X', 'x')
    item = item.replace('^', '**')
    item = item[:-2:]
    return item


def polynom_sum(polynom_1, polynom_2):
    x = Symbol('x')

    result = str(collect(str(polynom_1) + '+' + str(polynom_2), x))
    result = result.replace('**', '^')
    result = result.replace('*', '')
    result = result + '=0'

    print(f'Сумма многочленов {result=}')
    return result

print(convert('x^2-1=0'))
print(convert('x^2+1=0'))
polynom_sum()