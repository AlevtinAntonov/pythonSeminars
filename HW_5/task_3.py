# 3. Создайте программу для игры в ""Крестики-нолики"".

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Крестики - нолики')
root.geometry("400x400")
field = []
btn = []
player = True
playArea = []
standings = []


def play(n):
    global player
    btn[n].config(text='X' if player else 'O', state=DISABLED)
    playArea[n] = 1 if player else -1
    standings[0] = playArea[0] + playArea[1] + playArea[2]
    standings[1] = playArea[3] + playArea[4] + playArea[5]
    standings[2] = playArea[6] + playArea[7] + playArea[8]
    standings[3] = playArea[0] + playArea[3] + playArea[6]
    standings[4] = playArea[1] + playArea[4] + playArea[7]
    standings[5] = playArea[2] + playArea[5] + playArea[8]
    standings[6] = playArea[0] + playArea[4] + playArea[8]
    standings[7] = playArea[2] + playArea[4] + playArea[6]
    print(n, standings[:], playArea[:])
    for i in range(8):
        if standings[i] == 3:
            messagebox.showinfo("Победитель", "Игорок 1 - ( X ) победил!")
            print('X победил')
        elif standings[i] == -3:
            messagebox.showinfo("Победитель", "Игорок 2 - ( О ) победил!")
            print('O победил')
    player = not (player)


for i in range(3):
    field.append(Frame())
    field[i].pack(expand=YES, fill=BOTH)
    for j in range(3):
        btn.append(Button(field[i], text=' ', font=('mono', 30, 'bold'), width=4, height=2))
        btn[i * 3 + j].config(command=lambda n=i * 3 + j: play(n))
        btn[i * 3 + j].pack(expand=YES, fill=BOTH, side=LEFT, padx=1, pady=1)
        playArea.append(0)
        standings.append(0)

root.mainloop()
