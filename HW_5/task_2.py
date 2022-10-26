# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

number_of_candies = 221
player_1 = 0
player_2 = 0


def taken_candies(num):
    num = int(input(f'На столе лежит {number_of_candies} конфет, возьмите не более 28 конфет: ') or 1)
    return num


def check_taken_candies(num):
    global number_of_candies
    if 0 < num <= 28:
        number_of_candies -= num
        return number_of_candies
    else:
        number_of_candies -= 28
        return number_of_candies


name_player_1 = input('Введите имя 1 игрока: ')
name_player_2 = input('Введите имя 2 игрока: ')
player = random.randint(1, 3)

if player == 1:
    print(f'Первый ход у игрока - {name_player_1}')
else:
    print(f'Первый ход у игрока - {name_player_2}')

while number_of_candies > 0:
    if number_of_candies > 28:
        player_1 = taken_candies(player_1)
        check_taken_candies(player_1)
        if number_of_candies > 28:
            player_2 = taken_candies(player_2)
            check_taken_candies(player_2)
    if number_of_candies <= 28:
        print('<28')
        if player == 1:
            print(f'Осталось {number_of_candies} конфет и их забирает ПОБЕДИТЕЛЬ! - игрок : {name_player_1}')
            break
        else:
            print(f'Осталось {number_of_candies} конфет и их забирает ПОБЕДИТЕЛЬ! - игрок :  {name_player_2}')
            break

# type_game = int(input('Игра вариант игры: 1 - с игроком (по умолчанию) или 2 - с ботом  ') or 1)
#
# if type_game == 1:
#     name_player_1 = input('Введите имя 1 игрока: ')
#     name_player_2 = input('Введите имя 2 игрока: ')
# else:
#     name_player_1 = input('Введите имя 1 игрока: ')
#     name_player_2 = 'Bot'
#
# player = random.randint(1, 3)
#
# if player == 1:
#     print(f'Первый ход у игрока - {name_player_1}')
# else:
#     print(f'Первый ход у игрока - {name_player_2}')
#
# while number_of_candies > 0:
#     if number_of_candies > 28:
#         if type_game == 1 and player == 1:
#             player_1 = taken_candies(player_1)
#             check_taken_candies(player_1)
#         else:
#             player_1 -= random.randint(1, 29)
#             print(f'Bot взял {player_1} конфет ')
#             check_taken_candies(player_1)
#
#             if number_of_candies > 28:
#                 if type_game == 1 and player != 1:
#                     player_2 = taken_candies(player_2)
#                     check_taken_candies(player_2)
#                 else:
#                     player_2 -= random.randint(1, 29)
#                     print(f'Bot взял {player_2} конфет ')
#                     check_taken_candies(player_2)
#
#     if number_of_candies <= 28:
#         print('<28')
#         if player == 1:
#             print(f'Осталось {number_of_candies} конфет и их забирает ПОБЕДИТЕЛЬ! - игрок : {name_player_1}')
#             break
#         else:
#             print(f'Осталось {number_of_candies} конфет и их забирает ПОБЕДИТЕЛЬ! - игрок :  {name_player_2}')
#             break
