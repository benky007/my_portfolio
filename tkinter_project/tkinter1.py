from tkinter import *
import random


def click(player, output):
    player.get()
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    if computer == "rock" and player == "rock":
        output.config(text="You drawed")
    elif computer == "rock" and player == "paper":
        output.config(text="You won")
    elif computer == "rock" and player == "scissors":
        output.config(text="You lost")
    elif computer == "paper" and player == "rock":
        output.config(text="You won")
    elif computer == "paper" and player == "paper":
        output.config(text="You drawed")
    elif computer == "paper" and player == "scissors":
        output.config(text="You lost")
    elif computer == "scissors" and player == "rock":
        output.config(text="You lost")
    elif computer == "scissors" and player == "paper":
        output.config(text="You won")
    elif computer == "scissors" and player == "scissors":
        output.config(text="You drawn")


window = Tk()
window.title("Rock Paper Scissors Game")
window.configure(background="black")

title1 = Label(window, text="My Rock Paper Scissors Game", bg="black", fg="white", font="none 12")
title1.grid(row=0, rowspan=2, column=0, columnspan=30)
title2 = Label(window, text="By", bg="black", fg="white", font="none 12")
title2.grid(row=2, rowspan=2, column=0, columnspan=30)
title3 = Label(window, text="Ben", bg="black", fg="white", font="none 12")
title3.grid(row=4, rowspan=2, column=0, columnspan=30)
player = Entry(window, width=40, bg="white", fg="black")
player.grid(row=6, rowspan=10, column=0, columnspan=10)
output = Text(window, width=40, height=10, wrap=WORD, background="white")
output.grid(row=30, rowspan=10, column=0, columnspan=40)
submit = Button(window, text="submit", width=10, command=lambda: click(player, output))
submit.grid(row=25, rowspan=2, column=0, columnspan=5)
label = Label(window, text="The score:", bg="black", fg="white")
label.grid(row=27, rowspan=2, column=0, columnspan=10)
window.mainloop()
