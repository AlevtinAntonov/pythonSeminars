from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Игра Крестики-Нолики')


# X начинает
clicked = True
count = 0


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  X ВЫИГРАЛ !!")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  X ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  X ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  X ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  X ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  X ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  X ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  X ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  0 ВЫИГРАЛ !!")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  0 ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  0 ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  0 ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  0 ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  0 ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  0 ВЫИГРАЛ !!")
        disable_all_buttons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Крестики-Нолики", "ПОЗДРАВЛЯЕМ !  0 ВЫИГРАЛ !!")
        disable_all_buttons()

    if count == 9 and winner == False:
        messagebox.showinfo("Крестики-Нолики", "ЭТО НИЧЬЯ! \n Никто Не Выиграл!")
        disable_all_buttons()


def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Крестики-Нолики", "Эта клетка уже выбрана\n Выбери другую клетку...")


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Меню", menu=options_menu)
options_menu.add_command(label="Новая Игра", command=reset)

reset()

root.mainloop()


# # Инициализация карты
# maps = [1, 2, 3,
#         4, 5, 6,
#         7, 8, 9]
#
# # Инициализация победных линий
# victories = [[0, 1, 2],
#              [3, 4, 5],
#              [6, 7, 8],
#              [0, 3, 6],
#              [1, 4, 7],
#              [2, 5, 8],
#              [0, 4, 8],
#              [2, 4, 6]]

#
# # Вывод карты на экран
# def print_maps():
#     print(maps[0], end=" ")
#     print(maps[1], end=" ")
#     print(maps[2])
#
#     print(maps[3], end=" ")
#     print(maps[4], end=" ")
#     print(maps[5])
#
#     print(maps[6], end=" ")
#     print(maps[7], end=" ")
#     print(maps[8])
#
#
# # Сделать ход в ячейку
# def step_maps(step, symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
#
#
# # Получить текущий результат игры
# def get_result():
#     win = ""
#
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"
#
#     return win
#
#
# # Искусственный интеллект: поиск линии с нужным количеством X и O на победных линиях
# def check_line(sum_O, sum_X):
#     step = ""
#     for line in victories:
#         o = 0
#         x = 0
#
#         for j in range(0, 3):
#             if maps[line[j]] == "O":
#                 o = o + 1
#             if maps[line[j]] == "X":
#                 x = x + 1
#
#         if o == sum_O and x == sum_X:
#             for j in range(0, 3):
#                 if maps[line[j]] != "O" and maps[line[j]] != "X":
#                     step = maps[line[j]]
#
#     return step
#
#
# # Искусственный интеллект: выбор хода
# def AI():
#     step = ""
#
#     # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
#     step = check_line(2, 0)
#
#     # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
#     if step == "":
#         step = check_line(0, 2)
#
#         # 3) если 1 фигура своя и 0 чужих - ставим
#     if step == "":
#         step = check_line(1, 0)
#
#         # 4) центр пуст, то занимаем центр
#     if step == "":
#         if maps[4] != "X" and maps[4] != "O":
#             step = 5
#
#             # 5) если центр занят, то занимаем первую ячейку
#     if step == "":
#         if maps[0] != "X" and maps[0] != "O":
#             step = 1
#
#     return step
#
#
# # Основная программа
# game_over = False
# human = True
#
# while game_over == False:
#
#     # 1. Показываем карту
#     print_maps()
#
#     # 2. Спросим у играющего куда делать ход
#     if human == True:
#         symbol = "X"
#         step = int(input("Человек, ваш ход: "))
#     else:
#         print("Компьютер делает ход: ")
#         symbol = "O"
#         step = AI()
#
#     # 3. Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
#     if step != "":
#         step_maps(step, symbol)  # делаем ход в указанную ячейку
#         win = get_result()  # определим победителя
#         if win != "":
#             game_over = True
#         else:
#             game_over = False
#     else:
#         print("Ничья!")
#         game_over = True
#         win = "дружба"
#
#     human = not (human)
#
# # Игра окончена. Покажем карту. Объявим победителя.
# print_maps()
# print("Победил", win)