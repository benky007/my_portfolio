from tkinter import *

window = Tk()
window.geometry('500x500')
window.configure(background="grey")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

Frame_main = Frame(window, background="grey")
Frame_main.pack(expand=True)

window.mainloop()
