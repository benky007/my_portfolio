from tkinter import *


def one(event=None):
    print("1")


def two(event=None):
    print("2")


def three(event=None):
    print("3")


def four(event=None):
    print("4")


root = Tk()
menu = Menu(root, tearoff=0)
menu.add_command(label="One", accelerator="Ctrl+1", command=one)
menu.add_command(label="Two", accelerator="Ctrl+2", command=two)
menu.add_command(label="Three", accelerator="Ctrl+3", command=three)
menu.add_command(label="Four", accelerator="Ctrl+4", command=four)
if (root.tk.call('tk', 'windowingsystem') == 'aqua'):
    root.bind('<2>', lambda e: menu.post(e.x_root, e.y_root))
    root.bind('<Control-1>', lambda e: menu.post(e.x_root, e.y_root))
else:
    root.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))

root.bind('<Control-Key-1>', one)
root.bind('<Control-Key-2>', two)
root.bind('<Control-Key-3>', three)
root.bind('<Control-Key-4>', four)
root.mainloop()
