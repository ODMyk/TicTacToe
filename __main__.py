import tkinter
import tkinter.messagebox
import tkinter.simpledialog
from random import randint

window = tkinter.Tk()
window.title("Tic Tac Toe")

def button():
	return tkinter.Button(window, text = "X", font="Arial 48", fg="white", bg="white", activebackground="white", activeforeground="white")

button1 = button()
button2 = button()
button3 = button()
button4 = button()
button5 = button()
button6 = button()
button7 = button()
button8 = button()
button9 = button()

buttons = {
    1: button1, 2: button2, 3: button3,
    4: button4, 5: button5, 6: button6,
    7: button7, 8: button8, 9: button9
}

ActivePlayer = 2
p1 = []
p2 = []

players = {1: [p1, "Player 1", "X", 0], 2: [p2, "Player 2", "O", 0]}
winning_combo = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))

w = tkinter.messagebox.askokcancel("Choose variant", "Do you want to choose unique nicknames for each player ?")

if w:
    for i in range(1, 3):
        players[i][1] = tkinter.simpledialog.askstring("Nickname", f"Player {i}, enter your nickname")
        if not players[i][1]:
            players[i][1] = f"Player {i}"

def SetLayout(ind, PlayerSymbol):
    buttons[ind].config(text = PlayerSymbol, state = tkinter.DISABLED)

def ChooseWinner():
    Winner = None

    for player in players.values():
        if Winner:
            break
        for combo in winning_combo:
            if set(combo).issubset(player[0]):
                Winner = player
                break

    if not Winner:
        if all(x["state"] == tkinter.DISABLED for x in buttons.values()):
            tkinter.messagebox.showinfo("Game Over!", "Draw!")
            retry()
    else:
        tkinter.messagebox.showinfo("Game Over!", f"{Winner[1]} is winner!")
        Winner[3] += 1
        retry()
        

def ButtonClick(ind):
    global ActivePlayer, p1, p2, players
    np = players[ActivePlayer % 2 + 1]
    np[0].append(ind)
    SetLayout(np[0][-1], np[2])
    print(f"{np[1]}: {np[0]}")
    ActivePlayer += 1
    ChooseWinner()

x = 1
for i in range(3):
    for j in range(3):
        buttons[x].grid(row=i, column=j, sticky="snew", ipadx=40, ipady=40)
        x += 1

button1.config(command = lambda: ButtonClick(1))
button2.config(command = lambda: ButtonClick(2))
button3.config(command = lambda: ButtonClick(3))
button4.config(command = lambda: ButtonClick(4))
button5.config(command = lambda: ButtonClick(5))
button6.config(command = lambda: ButtonClick(6))
button7.config(command = lambda: ButtonClick(7))
button8.config(command = lambda: ButtonClick(8))
button9.config(command = lambda: ButtonClick(9))

def AutoPlay():
    global p1, p2
    EmplyCells = []
    for i in range(9):
        if ( (i+1 in p1) or (i+1 in p2)):
            EmplyCells.append(i+1)
        RandomIndex = randint(0, len(EmplyCells)-1)
        tkinter.ButtonClick(EmplyCells[RandomIndex])

def retry():
    global players, buttons, ActivePlayer
    ActivePlayer = 2
    a1 = tkinter.messagebox.askokcancel("Exit?", "Do you want to play one more game ?")
    if not a1:
        tkinter.messagebox.showinfo("Scores", f"{players[1][1]} {players[1][3]}:{players[2][3]} {players[2][1]}")
        window.destroy()
    else:
        for player in players.values():
            player[0].clear()
        for button in buttons.values():
            button.config(text="X", state=tkinter.NORMAL, fg="white")

window.mainloop()