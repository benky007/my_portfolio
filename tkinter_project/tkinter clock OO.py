import time
import datetime
from tkinter import *


class Window:
    def __init__(self, master):
        self.master = master
        self.clock = "decimal"
        self.labelClock = Label(master, font=('Dejavu', 80, 'bold'), fg='red', bg='black')
        self.labelClock.grid(row=0, column=0, columnspan=3)
        radioBinary = Radiobutton(master, text="Binary", variable=self.clock, value="binary",
                                  command=lambda: self.clockType("binary"))
        radioBinary.grid(row=1, column=0)
        radioBinary.deselect()
        radioDecimal = Radiobutton(master, text="Decimal", variable=self.clock, value="decimal",
                                   command=lambda: self.clockType("decimal"))
        radioDecimal.grid(row=1, column=1)
        radioDecimal.select()
        radioHex = Radiobutton(master, text="Hexadecimal", variable=self.clock, value="hexadecimal",
                               command=lambda: self.clockType("hexadecimal"))
        radioHex.grid(row=1, column=2)
        radioHex.deselect()
        self.update_clock()
        master.mainloop()

    def update_clock(self):
        self.master.title(self.clock.capitalize() + " clock")
        t = datetime.datetime.now()
        hour, minute, second = t.strftime("%T").split(":")
        if self.clock == "binary":
            hour = bin(int(hour))[2:].zfill(5)
            minute = bin(int(minute))[2:].zfill(5)
            second = bin(int(second))[2:].zfill(5)
        if self.clock == "hexadecimal":
            hour = hex(int(hour))[2:].zfill(2).upper()
            minute = hex(int(minute))[2:].zfill(2).upper()
            second = hex(int(second))[2:].zfill(2).upper()
        self.labelClock.config(text=hour + ":" + minute + ":" + second)
        self.labelClock.after(500, self.update_clock)

    def clockType(self, typeOfClock):
        self.clock = typeOfClock


if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.title("Decimal clock")
    main()
