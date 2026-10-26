import time
from tkinter import *

root = Tk()
root.geometry('600x200+350+300')
root.title('Tkinter Clock')

frame = Frame(root, width=200, height=100, bg='green')
frame.pack()

binary = 0
hexadecimal = 0
decimal = 1


def start():
    while True:
        hour = int(time.strftime("%H"))
        mini = int(time.strftime("%M"))
        sec = int(time.strftime("%S"))
        bin_hour = bin(hour)
        bin_min = bin(mini)
        bin_sec = bin(sec)
        hex_hour = hex(hour)
        hex_min = hex(mini)
        hex_sec = hex(sec)

        if binary == 1:
            timee = str(bin_hour) + ":" + str(bin_min) + ":" + str(bin_sec)
        elif hexadecimal == 1:
            timee = str(hex_hour) + ":" + str(hex_min) + ":" + str(hex_sec)
        else:
            timee = hour, ":", mini, ":", sec

        clock = Label(frame, padx=25, pady=40, bd=3, fg='dark green', font=('arial', 48, 'bold'), text=timee,
                      bg='light green')
        clock.pack()

        time.sleep(1)


start()
