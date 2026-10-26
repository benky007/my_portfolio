import time
import datetime
from tkinter import *

clock = ""


def hexClock():
    global clock
    clock = "hexadecimal"


def binaryClock():
    global clock
    clock = "binary"


def decimalClock():
    global clock
    clock = "decimal"


def start():
    global clock
    window = Tk()
    window.title("Decimal clock")
    clock = "decimal"
    labelClock = Label(window, font=('Dejavu', 80, 'bold'), fg='red', bg='black')
    labelClock.grid(row=0, column=0, columnspan=3)
    radioBinary = Radiobutton(window, text="Binary", variable=clock, value="binary", command=binaryClock)
    radioBinary.grid(row=1, column=0)
    radioBinary.deselect()
    radioDecimal = Radiobutton(window, text="Decimal", variable=clock, value="decimal", command=decimalClock)
    radioDecimal.grid(row=1, column=1)
    radioDecimal.select()
    radioHex = Radiobutton(window, text="Hexadecimal", variable=clock, value="hexadecimal", command=hexClock)
    radioHex.grid(row=1, column=2)
    radioHex.deselect()
    update_clock(window, labelClock)
    window.mainloop()


def update_clock(window, labelClock):
    global clock
    window.title(clock.capitalize() + " clock")
    t = datetime.datetime.now()
    hour, minute, second = t.strftime("%T").split(":")
    if clock == "binary":
        hour = bin(int(hour))[2:].zfill(5)
        minute = bin(int(minute))[2:].zfill(5)
        second = bin(int(second))[2:].zfill(5)
    if clock == "hexadecimal":
        hour = hex(int(hour))[2:].zfill(2).upper()
        minute = hex(int(minute))[2:].zfill(2).upper()
        second = hex(int(second))[2:].zfill(2).upper()
    labelClock.config(text=hour + ":" + minute + ":" + second)
    labelClock.after(500, update_clock, window, labelClock)


if __name__ == "__main__":
    start()
