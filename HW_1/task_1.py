# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
#  Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

while True:
    try:
        day_of_week = int(input('Введите день недели (цифра от 1 до 7): '))
        if day_of_week == 6 or day_of_week == 7:
            print('да')
            break
        elif 1 <= day_of_week <= 5:
            print('нет')
            break
        else:
            print(f'Введено некорректное число - {day_of_week} ')

    except ValueError:
        print('Ошибка ввода ! Введите целое число')
