from tkinter import *
import re
import time


class Main:
    def __init__(self, master):
        self.master = master
        self.question = ""
        self.answer = ""
        self.question_list = []
        self.frame = Frame(master, background="black")
        self.frame.pack(expand=True)
        self.frame1 = Frame(self.frame, background="black")
        self.frame1.pack(expand=True)
        self.frameHistory = Frame(self.frame, background="black")
        title1 = Frame(self.frame1)
        title1.pack(side=TOP)
        display = Frame(self.frame1)
        display.pack(side=TOP)
        func_row = Frame(self.frame1)
        func_row.pack(side=TOP, expand=True, fill=Y)
        row1 = Frame(self.frame1)
        row1.pack(side=TOP, expand=True, fill=Y)
        row2 = Frame(self.frame1)
        row2.pack(side=TOP, expand=True, fill=Y)
        row3 = Frame(self.frame1)
        row3.pack(side=TOP, expand=True, fill=Y)
        row4 = Frame(self.frame1)
        row4.pack(side=TOP, expand=True, fill=Y)
        row5 = Frame(self.frame1)
        row5.pack(side=TOP, expand=True, fill=Y)
        self.historyTitle = Frame(self.frameHistory, background="black")
        self.historyContent = Frame(self.frameHistory)
        self.historyExit = Frame(self.frameHistory)
        # recent = Label(row1, text="", width=20, anchor="w", font=('Dejavu', 8, 'bold'), fg='black', bg='green')
        # recent1 = Label(row2, text="", width=20, anchor="w", font=('Dejavu', 8, 'bold'), fg='black', bg='green')
        # recent2 = Label(row3, text="", width=20, anchor="w", font=('Dejavu', 8, 'bold'), fg='black', bg='green')
        self.historyScrollbar = Scrollbar(self.historyContent)
        self.myList = Listbox(self.historyContent, height=9, yscrollcommand=self.historyScrollbar.set)
        self.historyTitleLabel = Label(self.historyTitle, text="History", font=('Dejavu', 8, 'bold'), fg='white',
                                       bg='black')
        self.exitH = Button(self.historyExit, text="Exit History", bg="black", fg="white", command=self.exit1,
                            font="none 12", width=20)
        title_calc = Label(title1, text="My Calculator", font=('Dejavu', 8, 'bold'), fg='white', bg='black')
        title_calc.pack(side=LEFT)
        self.display1 = Label(display, text=self.question, width=20, anchor="w", font=('Dejavu', 8, 'bold'),
                              fg='black', bg='green')
        self.display1.pack(side=LEFT)
        floor = Button(func_row, text="//", bg="black", fg="white", command=lambda: self.funcOperation("//"), width=3)
        floor.pack(side=LEFT, fill=BOTH, expand=True)
        power = Button(func_row, text="**", bg="black", fg="white", command=lambda: self.funcOperation("**"), width=3)
        power.pack(side=LEFT, fill=BOTH, expand=True)
        mod = Button(func_row, text="%", bg="black", fg="white", command=lambda: self.funcOperation("%"), width=3)
        mod.pack(side=LEFT, fill=BOTH, expand=True)
        AC = Button(func_row, text="AC", bg="black", fg="white", command=self.funcAC, width=5)
        AC.pack(side=LEFT, fill=BOTH, expand=True)
        Seven = Button(row1, text="7", bg="black", fg="white", command=lambda: self.number("7"), width=3)
        Seven.pack(side=LEFT, fill=Y)
        Eight = Button(row1, text="8", bg="black", fg="white", command=lambda: self.number("8"), width=3)
        Eight.pack(side=LEFT, fill=Y)
        Nine = Button(row1, text="9", bg="black", fg="white", command=lambda: self.number("9"), width=3)
        Nine.pack(side=LEFT, fill=Y)
        div = Button(row1, text="/", bg="black", fg="white", command=lambda: self.funcOperation("/"), width=5)
        div.pack(side=LEFT, fill=Y)
        Four = Button(row2, text="4", bg="black", fg="white", command=lambda: self.number("4"), width=3)
        Four.pack(side=LEFT, fill=Y)
        Five = Button(row2, text="5", bg="black", fg="white", command=lambda: self.number("5"), width=3)
        Five.pack(side=LEFT, fill=Y)
        Six = Button(row2, text="6", bg="black", fg="white", command=lambda: self.number("6"), width=3)
        Six.pack(side=LEFT, fill=Y)
        times = Button(row2, text="*", bg="black", fg="white", command=lambda: self.funcOperation("*"), width=5)
        times.pack(side=LEFT, fill=Y)
        One = Button(row3, text="1", bg="black", fg="white", command=lambda: self.number("1"), width=3)
        One.pack(side=LEFT, fill=Y)
        Two = Button(row3, text="2", bg="black", fg="white", command=lambda: self.number("2"), width=3)
        Two.pack(side=LEFT, fill=Y)
        Three = Button(row3, text="3", bg="black", fg="white", command=lambda: self.number("3"), width=3)
        Three.pack(side=LEFT, fill=Y)
        sub = Button(row3, text="-", bg="black", fg="white", command=lambda: self.funcOperation("-"), width=5)
        sub.pack(side=LEFT, fill=Y)
        point = Button(row4, text=".", bg="black", fg="white", command=lambda: self.number("."), width=3)
        point.pack(side=LEFT, fill=Y)
        Zero = Button(row4, text="0", bg="black", fg="white", command=lambda: self.number("0"), width=3)
        Zero.pack(side=LEFT, fill=Y)
        equals = Button(row4, text="=", bg="black", fg="white", command=self.funcEquals, width=3)
        equals.pack(side=LEFT, fill=Y)
        plus = Button(row4, text="+", bg="black", fg="white", command=lambda: self.funcOperation("+"), width=5)
        plus.pack(side=LEFT, fill=Y)
        historyButton = Button(row5, text="History", bg="black", fg="white", command=self.history, width=18)
        historyButton.pack(side=LEFT, fill=Y)

    def number(self, num):
        self.answer = ""
        self.question += num
        '''
        # print("JW:", self.question, re.split(r"(\D)", self.question)[:-1])
        # self.question_list = re.split("(\D)", self.question)[:-1]
        self.question_list = re.split("(\D)", self.question)
        # print(self.question_list[2])
        if num == "(" or num == ")":
            #self.question_list = re.split("(\D)", self.question)[:len(re.split("(\D)", self.question))-1]
            # self.question_list = re.split("(\D)", self.question)[:-1]
            if len(self.question_list) > 1:
                if self.question_list[2] == '':
                    self.question_list.remove(self.question_list[2])
            if self.question_list[self.question_list.index("(")-1] != "*":
                # print(self.question_list)
                self.question_list.insert(1, "*")
            if self.question_list[self.question_list.index("*")-1] == "(":
                value = self.question_list.index("*")
                del (self.question_list[value])
            if self.question_list[self.question_list.index("*")+1] == ")":
                value = self.question_list.index("*")
                del (self.question_list[self.question_list.index("*")])
            if len(self.question_list) > 0:
                self.question = "".join(self.question_list)
            # print("question_list:", self.question_list)
        '''
        self.display1.config(text=self.question)

    def process_key(self, event):
        if "0" <= event.char <= "9" or event.char == ".":
            self.number(event.char)
        if event.char == "*" or event.char == "/" or event.char == "+" or event.char == "-" or event.char == "%":
            self.funcOperation(event.char)
        if event.char == "=" or event.keysym == "Return":
            self.funcEquals()
        if event.keysym == "Delete":
            self.funcAC()

    def funcOperation(self, operation):
        if self.answer != "":
            self.question = self.answer + operation
            self.answer = ""
        else:
            self.question += operation
        self.display1.config(text=self.question)

    def funcAC(self):
        self.question = ""
        self.display1.config(text=self.question)

    def funcEquals(self):
        try:
            self.answer = str(eval(self.question))
            self.myList.insert(END, self.question + " = " + self.answer)
            self.question = self.answer
            self.display1.config(text=self.question)
        except SyntaxError:
            self.display1.config(text="Error")
            time.sleep(5)
        self.question = ""

    def exit1(self):
        self.frameHistory.pack_forget()
        self.frame1.pack(expand=True)

    def history(self):
        self.frame1.pack_forget()
        self.frameHistory.pack(expand=True)
        self.historyTitle.pack(side=TOP)
        self.historyTitleLabel.pack(side=TOP)
        self.historyContent.pack(side=TOP, expand=True)
        self.historyExit.pack(side=TOP)
        self.historyScrollbar.pack(side=RIGHT, fill=Y)
        self.myList.pack(side=LEFT, anchor=NE, fill=Y)
        self.exitH.pack(side=BOTTOM, anchor=S, fill=Y)
        self.historyScrollbar.config(command=self.myList.yview)

    def close(self, event):
        self.master.destroy()

    def check(self, event):
        ans = self.myList.selection_get()
        self.answer = ans.split(" ")[0]
        self.question = ans.split(" ")[0]
        self.display1.config(text=self.answer)

    def delete(self, event):
        self.question = self.question[:len(self.question) - 1]
        self.display1.config(text=self.question)

    def binds(self):
        self.myList.bind("<Double-Button-1>", app.check)
        self.master.bind('<Escape>', app.close)
        self.master.bind("<BackSpace>", app.delete)
        self.master.bind("<KeyRelease>", app.process_key)


if __name__ == '__main__':
    root = Tk()
    root.configure(background="grey")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.geometry("130x195")
    root.resizable(0, 0)
    # root.overrideredirect(1)
    app = Main(root)
    app.binds()
    root.mainloop()
