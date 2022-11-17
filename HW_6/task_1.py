# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;


# expression = '1-2*3'
expression = '((1+(2*3))*2)+(4+2)*2/4'

# Вапиант 1
def calculation(expr):
    operator_function = {
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    nums = []
    opers = []

    tokens = list('(' + expr + ')')

    while tokens:
        token = tokens.pop(0)

        if token.isdecimal():
            nums.append(float(token))
        else:
            if token == ')':
                oper = opers.pop()
                while opers and oper != '(':
                    b, a = nums.pop(), nums.pop()
                    f = operator_function[oper]
                    nums.append(f(a, b))

                    oper = opers.pop()

            else:
                opers.append(token)

    return nums[0]


print(f'1 вариант {expression} = {calculation(expression)}')

# Вапиант 2 Польская обратная запись

OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}


def eval_(formula):
    def parse(formula_string):
        number = ''
        for s in formula_string:
            if s in '1234567890.':
                number += s
            elif number:
                yield float(number)
                number = ''
            if s in OPERATORS or s in "()":
                yield s
        if number:
            yield float(number)

    def shunting_yard(parsed_formula):
        stack = []
        for token in parsed_formula:
            if token in OPERATORS:
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        stack = []
        for token in polish:
            if token in OPERATORS:
                y, x = stack.pop(), stack.pop()
                stack.append(OPERATORS[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]

    return calc(shunting_yard(parse(formula)))


print(f'2 вариант {expression} = {eval_(expression)}')
