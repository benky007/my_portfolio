from tkinter import *

root = Tk()
root.configure(background="grey")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry("130x195")
root.resizable(0, 0)
# root.overrideredirect(1)

question = ""
answer = ""


def one():
    global question
    question += "1"
    display1.config(text=question)


def two():
    global question
    question += "2"
    display1.config(text=question)


def three():
    global question
    question += "3"
    display1.config(text=question)


def four():
    global question
    question += "4"
    display1.config(text=question)


def five():
    global question
    question += "5"
    display1.config(text=question)


def six():
    global question
    question += "6"
    display1.config(text=question)


def seven():
    global question
    question += "7"
    display1.config(text=question)


def eight():
    global question
    question += "8"
    display1.config(text=question)


def nine():
    global question
    question += "9"
    display1.config(text=question)


def zero():
    global question
    question += "0"
    display1.config(text=question)


def funcB():
    global question
    question += "("
    display1.config(text=question)


def funcLeftBracket():
    global question
    question += ")"
    display1.config(text=question)


def funcOperation(operation):
    global question
    global answer
    if answer != "":
        question = answer + operation
    else:
        question += operation
    display1.config(text=question)


def funcAC():
    global question
    question = ""
    display1.config(text=question)


def funcDecimal():
    global question
    question += "."
    display1.config(text=question)


def funcEquals():
    global question
    global answer
    global myList
    try:
        answer = str(eval(question))
        myList.insert(END, question + " = " + answer)
        question = answer
        display1.config(text=question)
        question = ""
    except TypeError:
        pass


def exit1():
    #    recent.pack_forget()
    #    recent1.pack_forget()
    #    recent2.pack_forget()
    exitH.pack_forget()
    frameHistory.pack_forget()
    historyTitle.pack_forget()
    historyScrollbar.pack_forget()
    historyContent.pack_forget()
    historyTitleLabel.pack_forget()
    myList.pack_forget()
    display.pack(side=TOP)
    func_row.pack(side=TOP, expand=True, fill=Y)
    row1.pack(side=TOP, expand=True, fill=Y)
    row2.pack(side=TOP, expand=True, fill=Y)
    row3.pack(side=TOP, expand=True, fill=Y)
    row4.pack(side=TOP, expand=True, fill=Y)
    row5.pack(side=TOP, expand=True, fill=Y)
    display1.pack(side=LEFT)
    bracket.pack(side=LEFT, fill=Y)
    Bracket.pack(side=LEFT, fill=Y)
    mod.pack(side=LEFT, fill=Y)
    AC.pack(side=LEFT, fill=Y)
    Seven.pack(side=LEFT, fill=Y)
    Eight.pack(side=LEFT, fill=Y)
    Nine.pack(side=LEFT, fill=Y)
    div.pack(side=LEFT, fill=Y)
    Four.pack(side=LEFT, fill=Y)
    Five.pack(side=LEFT, fill=Y)
    Six.pack(side=LEFT, fill=Y)
    times.pack(side=LEFT, fill=Y)
    One.pack(side=LEFT, fill=Y)
    Two.pack(side=LEFT, fill=Y)
    Three.pack(side=LEFT, fill=Y)
    sub.pack(side=LEFT, fill=Y)
    point.pack(side=LEFT, fill=Y)
    Zero.pack(side=LEFT, fill=Y)
    equals.pack(side=LEFT, fill=Y)
    plus.pack(side=LEFT, fill=Y)


def funcHistory():
    history()


frame = Frame(root, background="grey")
frame.pack(expand=True)
frame1 = Frame(frame, background="black")
frame1.pack(expand=True)
frameHistory = Frame(frame, background="black")
title1 = Frame(frame1)
title1.pack(side=TOP)
display = Frame(frame1)
display.pack(side=TOP)
func_row = Frame(frame1)
func_row.pack(side=TOP, expand=True, fill=Y)
row1 = Frame(frame1)
row1.pack(side=TOP, expand=True, fill=Y)
row2 = Frame(frame1)
row2.pack(side=TOP, expand=True, fill=Y)
row3 = Frame(frame1)
row3.pack(side=TOP, expand=True, fill=Y)
row4 = Frame(frame1)
row4.pack(side=TOP, expand=True, fill=Y)
row5 = Frame(frame1)
row5.pack(side=TOP, expand=True, fill=Y)
historyTitle = Frame(frameHistory)
historyContent = Frame(frameHistory)
historyExit = Frame(frameHistory)
# recent = Label(row1, text="", width=20, anchor="w", font=('Dejavu', 8, 'bold'), fg='black', bg='green')
# recent1 = Label(row2, text="", width=20, anchor="w", font=('Dejavu', 8, 'bold'), fg='black', bg='green')
# recent2 = Label(row3, text="", width=20, anchor="w", font=('Dejavu', 8, 'bold'), fg='black', bg='green')
historyScrollbar = Scrollbar(historyContent)
myList = Listbox(historyContent, height=9, yscrollcommand=historyScrollbar.set)
historyTitleLabel = Label(historyTitle, text="History", font=('Dejavu', 8, 'bold'), fg='white', bg='black')
exitH = Button(historyExit, text="Exit History", bg="black", fg="white", command=exit1, font="none 12", width=10)
title_calc = Label(title1, text="My Calculator", font=('Dejavu', 8, 'bold'), fg='white', bg='black')
title_calc.pack(side=LEFT)
display1 = Label(display, text=question, width=20, anchor="w", font=('Dejavu', 8, 'bold'), fg='black', bg='green')
display1.pack(side=LEFT)
bracket = Button(func_row, text="(", bg="black", fg="white", command=funcB, width=3)
bracket.pack(side=LEFT, fill=BOTH, expand=True)
Bracket = Button(func_row, text=")", bg="black", fg="white", command=funcLeftBracket, width=3)
Bracket.pack(side=LEFT, fill=BOTH, expand=True)
mod = Button(func_row, text="%", bg="black", fg="white", command=lambda: funcOperation("%"), width=3)
mod.pack(side=LEFT, fill=BOTH, expand=True)
AC = Button(func_row, text="AC", bg="black", fg="white", command=funcAC, width=5)
AC.pack(side=LEFT, fill=BOTH, expand=True)
Seven = Button(row1, text="7", bg="black", fg="white", command=seven, width=3)
Seven.pack(side=LEFT, fill=Y)
Eight = Button(row1, text="8", bg="black", fg="white", command=eight, width=3)
Eight.pack(side=LEFT, fill=Y)
Nine = Button(row1, text="9", bg="black", fg="white", command=nine, width=3)
Nine.pack(side=LEFT, fill=Y)
div = Button(row1, text="/", bg="black", fg="white", command=lambda: funcOperation("/"), width=5)
div.pack(side=LEFT, fill=Y)
Four = Button(row2, text="4", bg="black", fg="white", command=four, width=3)
Four.pack(side=LEFT, fill=Y)
Five = Button(row2, text="5", bg="black", fg="white", command=five, width=3)
Five.pack(side=LEFT, fill=Y)
Six = Button(row2, text="6", bg="black", fg="white", command=six, width=3)
Six.pack(side=LEFT, fill=Y)
times = Button(row2, text="*", bg="black", fg="white", command=lambda: funcOperation("*"), width=5)
times.pack(side=LEFT, fill=Y)
One = Button(row3, text="1", bg="black", fg="white", command=one, width=3)
One.pack(side=LEFT, fill=Y)
Two = Button(row3, text="2", bg="black", fg="white", command=two, width=3)
Two.pack(side=LEFT, fill=Y)
Three = Button(row3, text="3", bg="black", fg="white", command=three, width=3)
Three.pack(side=LEFT, fill=Y)
sub = Button(row3, text="-", bg="black", fg="white", command=lambda: funcOperation("-"), width=5)
sub.pack(side=LEFT, fill=Y)
point = Button(row4, text=".", bg="black", fg="white", command=funcDecimal, width=3)
point.pack(side=LEFT, fill=Y)
Zero = Button(row4, text="0", bg="black", fg="white", command=zero, width=3)
Zero.pack(side=LEFT, fill=Y)
equals = Button(row4, text="=", bg="black", fg="white", command=funcEquals, width=3)
equals.pack(side=LEFT, fill=Y)
plus = Button(row4, text="+", bg="black", fg="white", command=lambda: funcOperation("+"), width=5)
plus.pack(side=LEFT, fill=Y)
historyButton = Button(row5, text="history", bg="black", fg="white", command=funcHistory, width=17)
historyButton.pack(side=LEFT, fill=Y)


def history():
    #    global recent
    #    global recent1
    #    global recent2
    #    Recent1 = past[length - 1]
    #    Recent2 = past[length - 2]
    #    Recent3 = past[length - 3]
    One.pack_forget()
    Two.pack_forget()
    Three.pack_forget()
    Four.pack_forget()
    Five.pack_forget()
    Six.pack_forget()
    Seven.pack_forget()
    Eight.pack_forget()
    Nine.pack_forget()
    Zero.pack_forget()
    bracket.pack_forget()
    Bracket.pack_forget()
    mod.pack_forget()
    AC.pack_forget()
    div.pack_forget()
    times.pack_forget()
    sub.pack_forget()
    point.pack_forget()
    equals.pack_forget()
    plus.pack_forget()
    display1.pack_forget()
    func_row.pack_forget()
    row1.pack_forget()
    row2.pack_forget()
    row3.pack_forget()
    row4.pack_forget()
    row5.pack_forget()
    display.pack_forget()
    #    recent.config(text=Recent1)
    #    recent.pack(side=LEFT)
    #    recent1.config(text=Recent2)
    #    recent1.pack(side=LEFT)
    #    recent2.config(text=Recent3)
    #    recent2.pack(side=LEFT)
    frameHistory.pack(expand=True)
    historyTitle.pack(side=TOP)
    historyContent.pack(side=TOP, expand=True)
    historyExit.pack(side=TOP)
    historyScrollbar.pack(side=RIGHT, fill=Y)
    myList.pack(side=LEFT, anchor=NE, fill=Y)
    exitH.pack(side=BOTTOM, anchor=S, fill=Y)
    historyScrollbar.config(command=myList.yview)


root.mainloop()
