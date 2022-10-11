# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

while True:
    try:
        quarter_number = int(input('Введите номер четверти координат: '))
        if 1 <= quarter_number <= 4:
            if quarter_number == 1:
                print(f'В 1 четверти диапазон возможных координат точек : x > 0 и y > 0')
                break
            elif quarter_number == 2:
                print(f'Во 2 четверти диапазон возможных координат точек : x < 0 и y > 0')
                break
            elif quarter_number == 3:
                print(f'В 3 четверти диапазон возможных координат точек : x < 0 и y < 0')
                break
            elif quarter_number == 4:
                print(f'В 4 четверти диапазон возможных координат точек : x > 0 и y < 0')
                break
        else:
            print(f'Введено некорректное число - {quarter_number} ')

    except ValueError:
        print('Ошибка ввода ! Введите целое число')
