# 3. Создайте программу для игры в ""Крестики-нолики"".

# 1 вариант консоль
board = list(range(1, 10))


def game_board(board):
    print('-' * 12)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-' * 12)


def choosing_move(tic_tac_toe):
    valid = False
    while not valid:
        player_index = input('Ваш ход, выберите ячейку ' + tic_tac_toe + ' --> ')
        try:
            player_index = int(player_index)
        except:
            print('Ошибка! Что-то пошло не так :)')
            continue
        if player_index >= 1 and player_index <= 9:
            if (str(board[player_index - 1]) not in 'XO'):
                board[player_index - 1] = tic_tac_toe
                valid = True
            else:
                print('Поле уже занято')
        else:
            print('Еще раз попробуй')


def checking_winnings(board):
    winning = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
               (0, 3, 6), (1, 4, 7), (2, 5, 8),
               (0, 4, 8), (2, 4, 6))
    for i in winning:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


def play(board):
    counter = 0
    win = False
    while not win:
        game_board(board)
        if counter % 2 == 0:
            choosing_move('X')
        else:
            choosing_move('0')
        counter += 1
        if counter > 4:
            tt_win = checking_winnings(board)
            if tt_win:
                game_board(board)
                print(f'Победитель - {tt_win}')
                win = True
                break
            if counter == 9:
                game_board(board)
                print('Игра окончена : победила, ДРУЖБА :)')
                break
        game_board(board)


play(board)

# 2 вариант tkinter
# from tkinter import *
# from tkinter import messagebox
#
# root = Tk()
# root.title('Крестики - нолики')
# root.geometry("400x400")
# field = []
# btn = []
# player = True
# playArea = []
# standings = []
#
#
# def play(n):
#     global player
#     btn[n].config(text='X' if player else 'O', state=DISABLED)
#     playArea[n] = 1 if player else -1
#     standings[0] = playArea[0] + playArea[1] + playArea[2]
#     standings[1] = playArea[3] + playArea[4] + playArea[5]
#     standings[2] = playArea[6] + playArea[7] + playArea[8]
#     standings[3] = playArea[0] + playArea[3] + playArea[6]
#     standings[4] = playArea[1] + playArea[4] + playArea[7]
#     standings[5] = playArea[2] + playArea[5] + playArea[8]
#     standings[6] = playArea[0] + playArea[4] + playArea[8]
#     standings[7] = playArea[2] + playArea[4] + playArea[6]
#     print(n, standings[:], playArea[:])
#     for i in range(8):
#         if standings[i] == 3:
#             messagebox.showinfo("Победитель", "Игорок 1 - ( X ) победил!")
#             print('X победил')
#         elif standings[i] == -3:
#             messagebox.showinfo("Победитель", "Игорок 2 - ( О ) победил!")
#             print('O победил')
#     player = not (player)
#
#
# for i in range(3):
#     field.append(Frame())
#     field[i].pack(expand=YES, fill=BOTH)
#     for j in range(3):
#         btn.append(Button(field[i], text=' ', font=('mono', 30, 'bold'), width=4, height=2))
#         btn[i * 3 + j].config(command=lambda n=i * 3 + j: play(n))
#         btn[i * 3 + j].pack(expand=YES, fill=BOTH, side=LEFT, padx=1, pady=1)
#         playArea.append(0)
#         standings.append(0)
#
# root.mainloop()
