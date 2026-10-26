from tkinter import *


class Main:
    def __init__(self, master):
        self.master = master
        frame_top = Frame(master, background="white", height=250, bd=0, highlightcolor="#c8c8c8",
                          highlightbackground="#c8c8c8", highlightthickness="10")
        frame_top.pack(side=TOP, fill="x")


if __name__ == '__main__':
    root = Tk()
    root.configure(bg="#C8C8C8")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.geometry("500x500")
    root.resizable(0, 0)
    # root.overrideredirect(1)
    app = Main(root)
    # app.binds()
    root.mainloop()
