import time
import datetime
from tkinter import *
import random

push1 = 0
window = Tk()
window.configure(background="white")
window.geometry('600x400+350+300')
window.title("Decimal clock")
clock = "decimal"
next_clock = "decimal"
timer = 0
frame1 = Frame(window, width=1200, height=50, bg="white")
frame1.pack(expand=True, side=TOP)
frame2 = Frame(window, width=1200, height=50, bg="white")
frame2.pack(expand=True, side=TOP)
frame3 = Frame(window, width=2000, height=1000, bg="white")
frame3.pack(expand=True, side=RIGHT)
frame4 = Frame(window, width=2000, height=1000, bg="white")
frame4.pack(expand=True, side=BOTTOM)
labelTimer1 = Label(frame1)
labelClock1 = Label(frame2)
button = Button(frame3)
labelRegion = Label(frame4)
enterRegion = Entry(frame4)
buttonRegion = Button(frame4)


def start():
    global window
    global clock
    global next_clock
    global timer
    global push1
    global labelTimer1
    global labelClock1
    global button
    labelTimer1 = Label(frame1, font=('Times', 40, 'bold'), fg='black', bg='white')
    labelTimer1.pack(expand=True, side=TOP)
    labelClock1 = Label(frame2, font=('Times', 80, 'bold'), fg='black', bg='white')
    labelClock1.pack(expand=True, side=LEFT)
    button = Button(frame3, height=500, width=1000, text="Hide time remaining", command=press)
    button.pack(expand=True, side=BOTTOM)
    update_clock()
    window.mainloop()


def press():
    global push1
    push1 = push1 + 1


def update_clock():
    global window
    global clock
    global next_clock
    global timer
    global labelTimer1
    global labelClock1
    global push1
    global button
    labelTimer1.config(bg="white", fg="black")
    labelClock1.config(bg="white", fg="black")
    window.configure(background="white")
    clock_types = ["binary", "hexadecimal", "decimal"]
    window.title(clock.capitalize() + " clock")
    t = datetime.datetime.now()
    hour, minute, second = t.strftime("%T").split(":")
    if clock == "binary":
        hour = bin(int(hour))[2:].zfill(5)
        minute = bin(int(minute))[2:].zfill(5)
        second = bin(int(second))[2:].zfill(5)
        labelTimer1.config(bg="green", fg="white")
        labelClock1.config(bg="green", fg="white")
        window.configure(background="green")
    if clock == "hexadecimal":
        hour = hex(int(hour))[2:].zfill(2).upper()
        minute = hex(int(minute))[2:].zfill(2).upper()
        second = hex(int(second))[2:].zfill(2).upper()
        labelTimer1.config(bg="red", fg="white")
        labelClock1.config(bg="red", fg="white")
        window.configure(background="red")
    if timer == 0:
        clock = next_clock
        timer = random.randint(60, 120) + 1
        next_clock = random.choice(clock_types)
    timer = timer - 1
    if push1 == 1:
        labelTimer1.pack_forget()
    if push1 == 2:
        push1 = 0
        labelClock1.pack_forget()
        button.pack_forget()
        labelTimer1.pack(expand=True, side=TOP)
        labelClock1.pack(expand=True)
        button.pack(expand=True, side=BOTTOM)
    labelTimer1.config(text="Time remaining: " + str(timer))
    labelClock1.config(text=hour + ":" + minute + ":" + second)
    labelClock1.after(1000, update_clock)


if __name__ == "__main__":
    start()
