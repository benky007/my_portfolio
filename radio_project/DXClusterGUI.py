from tkinter import *

window = Tk()
window.geometry('140x165')
window.configure(background="grey")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
num = 0

Frame_main = Frame(window, background="grey")
Frame_main.pack(expand=True)
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
myList = Listbox(window, yscrollcommand=scrollbar.set)
myList.pack(side=LEFT, fill=BOTH)


def insert1():
    myList.insert(END, "This is line number " + str(1))


def run():
    insert1()
    window.after(100, run)


scrollbar.config(command=myList.yview)

window.after(100, run)
window.mainloop()
