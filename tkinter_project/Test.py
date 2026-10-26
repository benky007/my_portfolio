from tkinter import *

root = Tk()
root.wm_title("Tkinter button")
root.geometry("320x200")

cool = Frame(root)
cool.pack(fill=BOTH, expand=1)


def clickExitButton():
    exit()


exitButton = Button(cool, text="Exit", command=clickExitButton)
exitButton.pack()

root.mainloop()
