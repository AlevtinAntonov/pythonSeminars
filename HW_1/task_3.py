# 3.Напишите программу, которая принимает на вход координаты точки (X и Y),
# причем X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
#  Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

while True:
    try:
        x = int(input('Введите координату х: '))
        y = int(input('Введите координату y: '))

        if x > 0 and y > 0:
            print(f'Точка с координатами x - {x} и y - {y} находится в 1 четверти')
            break
        elif x < 0 and y > 0:
            print(f'Точка с координатами x - {x} и y - {y} находится во 2 четверти')
            break
        elif x < 0 and y < 0:
            print(f'Точка с координатами x - {x} и y - {y} находится в 3 четверти')
            break
        elif x > 0 and y < 0:
            print(f'Точка с координатами x - {x} и y - {y} находится в 4 четверти')
            break
        elif x == 0 and y != 0:
            print(f'Точка с координатами x - {x} и y - {y} находится на оси X')
            break
        elif y == 0 and x != 0:
            print(f'Точка с координатами x - {x} и y - {y} находится на оси y')
            break
        elif x == 0 and y == 0:
            print(f'Точка с координатами x - {x} и y - {y} - это начало координат')
            break
    except ValueError:
        print('Ошибка ввода ! Введите целое число')