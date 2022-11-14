# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

number_of_candies = 15
player_1 = 0
player_2 = 0
max_candies = 5
first_move = 1
second_move = 0


def taken_candies(num):
    while True:
        try:
            num = int(
                input(f'На столе лежит {number_of_candies} конфет, возьмите не более {max_candies} конфет: ') or 1)
            return num
        except ValueError:
            print('Ошибка!!! Вы ввели не число!')


def check_taken_candies(num):
    global number_of_candies, first_move, second_move
    first_move, second_move = second_move, first_move
    if 0 < num <= max_candies:
        number_of_candies -= num
        return number_of_candies
    else:
        print(f'Вы ввели число больше разрешенного максимума {max_candies}, поэтому вы взяли {max_candies} конфет')
        number_of_candies -= max_candies
        return number_of_candies


def bot_taken_candies(num):
    num = random.randint(1, max_candies)
    print(f'Bot взял {num} конфет')
    return num


def clever_bot_taken_candies(num):
    if number_of_candies > max_candies * 2:
        num = number_of_candies % (max_candies + 1)
    else:
        num = number_of_candies - max_candies - 1
    if num == 0:
        num = 1
    print(f'Bot взял {num} конфет')
    return num


type_game = int(
    input('Игра вариант игры: 1 - с игроком (по умолчанию) или 2 - с просто Ботом или 3 - с умным Ботом ') or 1)

if type_game == 1:
    name_player_1 = input('Введите имя 1 игрока: ')
    name_player_2 = input('Введите имя 2 игрока: ')
else:
    name_player_1 = input('Введите имя 1 игрока: ')
    name_player_2 = 'Bot'

player = random.randint(1, 2)

if player == 1:
    print(f'Первый ход у игрока - {name_player_1}')
else:
    print(f'Первый ход у игрока - {name_player_2}')
    name_player_1, name_player_2 = name_player_2, name_player_1
    first_move, second_move = second_move, first_move

while number_of_candies > 0:
    if type_game == 1:
        if number_of_candies > max_candies:
            player_1 = taken_candies(player_1)
            check_taken_candies(player_1)
            if number_of_candies > max_candies:
                player_2 = taken_candies(player_2)
                check_taken_candies(player_2)
    else:
        if number_of_candies > max_candies:
            if player == 1:
                player_1 = taken_candies(player_1)
            else:
                if type_game == 2:
                    player_1 = bot_taken_candies(player_1)
                else:
                    player_1 = clever_bot_taken_candies(player_2)
            check_taken_candies(player_1)

            if number_of_candies > max_candies:
                if player == 1:
                    if type_game == 2:
                        player_2 = bot_taken_candies(player_2)
                    else:
                        player_2 = clever_bot_taken_candies(player_2)
                else:
                    player_2 = taken_candies(player_2)
                check_taken_candies(player_2)

    if number_of_candies <= max_candies:
        if player == 1 and first_move:
            print(f'Осталось {number_of_candies} конфет и их забирает ПОБЕДИТЕЛЬ! - игрок : {name_player_1}')
            break
        elif player == 2 and first_move:
            print(f'Осталось {number_of_candies} конфет и их забирает ПОБЕДИТЕЛЬ! - игрок :  {name_player_2}')
            break
        elif player == 1 and second_move:
            print(f'Осталось {number_of_candies} конфет и их забирает ПОБЕДИТЕЛЬ! - игрок :  {name_player_2}')
            break
        elif player == 2 and second_move:
            print(f'Осталось {number_of_candies} конфет и их забирает ПОБЕДИТЕЛЬ! - игрок :  {name_player_1}')
            break
