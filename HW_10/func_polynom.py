from sympy import Symbol, collect


def convert(item):
    item = item.replace('=0', '')
    item = item.replace('^', '**')
    return item


def polynom_sum(polynom_1, polynom_2):
    x = Symbol('x')

    result = str(collect(str(polynom_1) + '+' + str(polynom_2), x))
    result = result.replace('**', '^')
    result = result.replace('*', '')
    result = result + '=0'

    print(f'Сумма многочленов {result=}')
    return result
