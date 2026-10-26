from tkinter import *
import re
import time
from PIL import Image, ImageTk


class Main:
    def __init__(self, master):
        self.master = master
        self.question = ""
        self.answer = ""
        self.distance_x = 565
        self.distance_y = 200
        self.increase = 0
        self.question_list = []
        self.frame = Frame(master, background="black")
        self.frame.pack(expand=True)
        self.frame1 = Frame(self.frame, background="black")
        self.frame1.pack(expand=True)
        self.frameHistory = Frame(self.frame, background="black")
        self.btn0 = ImageTk.PhotoImage(Image.open("button0.png").resize((25+self.increase, 25+self.increase),
                                                                        Image.Resampling.LANCZOS))
        self.btn0_ = ImageTk.PhotoImage(Image.open("button0_.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btn1 = ImageTk.PhotoImage(Image.open("button1.png").resize((25+self.increase, 25+self.increase),
                                                                        Image.Resampling.LANCZOS))
        self.btn1_ = ImageTk.PhotoImage(Image.open("button1_.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btn2 = ImageTk.PhotoImage(Image.open("button2.png").resize((25+self.increase, 25+self.increase),
                                                                        Image.Resampling.LANCZOS))
        self.btn2_ = ImageTk.PhotoImage(Image.open("buton2_.png").resize((25+self.increase, 25+self.increase),
                                                                         Image.Resampling.LANCZOS))
        self.btn3 = ImageTk.PhotoImage(Image.open("button3.png").resize((25+self.increase, 25+self.increase),
                                                                        Image.Resampling.LANCZOS))
        self.btn3_ = ImageTk.PhotoImage(Image.open("button3_.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btn4 = ImageTk.PhotoImage(Image.open("button4.png").resize((25+self.increase, 25+self.increase),
                                                                        Image.Resampling.LANCZOS))
        self.btn4_ = ImageTk.PhotoImage(Image.open("button4_.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btn5 = ImageTk.PhotoImage(Image.open("button5.png").resize((25+self.increase, 25+self.increase),
                                                                        Image.Resampling.LANCZOS))
        self.btn5_ = ImageTk.PhotoImage(Image.open("button5_.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btn6 = ImageTk.PhotoImage(Image.open("button6.png").resize((25+self.increase, 25+self.increase),
                                                                        Image.Resampling.LANCZOS))
        self.btn6_ = ImageTk.PhotoImage(Image.open("button6_.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btn7 = ImageTk.PhotoImage(Image.open("button7.png").resize((25+self.increase, 25+self.increase),
                                                                        Image.Resampling.LANCZOS))
        self.btn7_ = ImageTk.PhotoImage(Image.open("button7_.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btn8 = ImageTk.PhotoImage(Image.open("button8.png").resize((25+self.increase, 25+self.increase),
                                                                        Image.Resampling.LANCZOS))
        self.btn8_ = ImageTk.PhotoImage(Image.open("button8_.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btn9 = ImageTk.PhotoImage(Image.open("button9.png").resize((25+self.increase, 25+self.increase),
                                                                        Image.Resampling.LANCZOS))
        self.btn9_ = ImageTk.PhotoImage(Image.open("button9_.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btnplus = ImageTk.PhotoImage(Image.open("button+.png").resize((25+self.increase, 25+self.increase),
                                                                           Image.Resampling.LANCZOS))
        self.btnplus_ = ImageTk.PhotoImage(Image.open("button+_.png").resize((25+self.increase, 25+self.increase),
                                                                             Image.Resampling.LANCZOS))
        self.btnmin = ImageTk.PhotoImage(Image.open("button-.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btnmin_ = ImageTk.PhotoImage(Image.open("button-_.png").resize((25+self.increase, 25+self.increase),
                                                                            Image.Resampling.LANCZOS))
        self.btndiv = ImageTk.PhotoImage(Image.open("buttondiv.png").resize((25+self.increase, 25+self.increase),
                                                                            Image.Resampling.LANCZOS))
        self.btndiv_ = ImageTk.PhotoImage(Image.open("buttondiv_.png").resize((25+self.increase, 25+self.increase),
                                                                              Image.Resampling.LANCZOS))
        self.btnfloor = ImageTk.PhotoImage(Image.open("buttonfloor.png").resize((25+self.increase, 25+self.increase),
                                                                                Image.Resampling.LANCZOS))
        self.btnfloor_ = ImageTk.PhotoImage(Image.open("buttonfloor_.png").resize((25+self.increase, 25+self.increase),
                                                                                  Image.Resampling.LANCZOS))
        self.btnmod = ImageTk.PhotoImage(Image.open("button%.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btnmod_ = ImageTk.PhotoImage(Image.open("button%_.png").resize((25+self.increase, 25+self.increase),
                                                                            Image.Resampling.LANCZOS))
        self.btnX = ImageTk.PhotoImage(Image.open("buttonX.png").resize((25+self.increase, 25+self.increase),
                                                                        Image.Resampling.LANCZOS))
        self.btnX_ = ImageTk.PhotoImage(Image.open("buttonX_.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btnpower = ImageTk.PhotoImage(Image.open("buttonpower.png").resize((25+self.increase, 25+self.increase),
                                                                                Image.Resampling.LANCZOS))
        self.btnpower_ = ImageTk.PhotoImage(Image.open("buttonpower_.png").resize((25+self.increase, 25+self.increase),
                                                                                  Image.Resampling.LANCZOS))
        self.btnequals = ImageTk.PhotoImage(Image.open("button=.png").resize((25+self.increase, 25+self.increase),
                                                                             Image.Resampling.LANCZOS))
        self.btnequals_ = ImageTk.PhotoImage(Image.open("button=_.png").resize((25+self.increase, 25+self.increase),
                                                                               Image.Resampling.LANCZOS))
        self.btndec = ImageTk.PhotoImage(Image.open("buttondec.png").resize((25+self.increase, 25+self.increase),
                                                                            Image.Resampling.LANCZOS))
        self.btndec_ = ImageTk.PhotoImage(Image.open("buttondec_.png").resize((25+self.increase, 25+self.increase),
                                                                              Image.Resampling.LANCZOS))
        self.btnac = ImageTk.PhotoImage(Image.open("buttonac.png").resize((25+self.increase, 25+self.increase),
                                                                          Image.Resampling.LANCZOS))
        self.btnac_ = ImageTk.PhotoImage(Image.open("buttonac_.png").resize((25+self.increase, 25+self.increase),
                                                                            Image.Resampling.LANCZOS))
        self.btnhis = ImageTk.PhotoImage(Image.open("buttonhis.png").resize((115+self.increase, 25+self.increase),
                                                                            Image.Resampling.LANCZOS))
        self.btnhis_ = ImageTk.PhotoImage(Image.open("buttonhis_.png").resize((115+self.increase, 25+self.increase),
                                                                              Image.Resampling.LANCZOS))
        self.btncalc = ImageTk.PhotoImage(Image.open("buttoncalc.png").resize((115+self.increase, 25+self.increase),
                                                                              Image.Resampling.LANCZOS))
        self.btncalc_ = ImageTk.PhotoImage(Image.open("buttoncalc_.png").resize((115+self.increase, 25+self.increase),
                                                                                Image.Resampling.LANCZOS))
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
        self.myList = Listbox(self.historyContent, height=10, yscrollcommand=self.historyScrollbar.set)
        self.historyTitleLabel = Label(self.historyTitle, text="History", font=('Dejavu', 8, 'bold'), fg='white',
                                       bg='black')
        self.exitH = Label(self.historyExit, image=self.btncalc, bg="black")
        title_calc = Label(title1, text="My Calculator", font=('Dejavu', 8, 'bold'), fg='white', bg='black')
        title_calc.pack(side=LEFT)
        self.display1 = Label(display, text=self.question, width=20, anchor="w", font=('Dejavu', 8, 'bold'),
                              fg='black', bg='green')
        self.display1.pack(side=LEFT)
        self.floor = Label(func_row, image=self.btnfloor, bg="black")
        self.floor.pack(side=LEFT, fill=BOTH, expand=True)
        self.power = Label(func_row, image=self.btnpower, bg="black")
        self.power.pack(side=LEFT, fill=BOTH, expand=True)
        self.mod = Label(func_row, image=self.btnmod, bg="black")
        self.mod.pack(side=LEFT, fill=BOTH, expand=True)
        self.AC = Label(func_row, image=self.btnac, bg="black")
        self.AC.pack(side=LEFT, fill=BOTH, expand=True)
        self.Seven = Label(row1, image=self.btn7, bg="black")
        self.Seven.pack(side=LEFT, fill=Y)
        self.Eight = Label(row1, image=self.btn8, bg="black")
        self.Eight.pack(side=LEFT, fill=Y)
        self.Nine = Label(row1, image=self.btn9, bg="black")
        self.Nine.pack(side=LEFT, fill=Y)
        self.div = Label(row1, image=self.btndiv, bg="black")
        self.div.pack(side=LEFT, fill=Y)
        self.Four = Label(row2, image=self.btn4, bg="black")
        self.Four.pack(side=LEFT, fill=Y)
        self.Five = Label(row2, image=self.btn5, bg="black")
        self.Five.pack(side=LEFT, fill=Y)
        self.Six = Label(row2, image=self.btn6, bg="black")
        self.Six.pack(side=LEFT, fill=Y)
        self.times = Label(row2, image=self.btnX, bg="black")
        self.times.pack(side=LEFT, fill=Y)
        self.One = Label(row3, image=self.btn1, bg="black")
        self.One.pack(side=LEFT, fill=Y)
        self.Two = Label(row3, image=self.btn2, bg="black")
        self.Two.pack(side=LEFT, fill=Y)
        self.Three = Label(row3, image=self.btn3, bg="black")
        self.Three.pack(side=LEFT, fill=Y)
        self.sub = Label(row3, image=self.btnmin, bg="black")
        self.sub.pack(side=LEFT, fill=Y)
        self.point = Label(row4, image=self.btndec, bg="black")
        self.point.pack(side=LEFT, fill=Y)
        self.Zero = Label(row4, image=self.btn0, bg="black")
        self.Zero.pack(side=LEFT, fill=Y)
        self.equals = Label(row4, image=self.btnequals, bg="black")
        self.equals.pack(side=LEFT, fill=Y)
        self.plus = Label(row4, image=self.btnplus, bg="black")
        self.plus.pack(side=LEFT, fill=Y)
        self.historyButton = Label(row5, image=self.btnhis, bg="black")
        self.historyButton.pack(side=LEFT, fill=Y)

    def press(self, event, num):
        if num == "0":
            self.Zero.config(image=self.btn0_)
            self.number("0")
        if num == "1":
            self.One.config(image=self.btn1_)
            self.number("1")
        if num == "2":
            self.Two.config(image=self.btn2_)
            self.number("2")
        if num == "3":
            self.Three.config(image=self.btn3_)
            self.number("3")
        if num == "4":
            self.Zero.config(image=self.btn4_)
            self.number("4")
        if num == "5":
            self.Five.config(image=self.btn5_)
            self.number("5")
        if num == "6":
            self.Six.config(image=self.btn6_)
            self.number("6")
        if num == "7":
            self.Seven.config(image=self.btn7_)
            self.number("7")
        if num == "8":
            self.Eight.config(image=self.btn8_)
            self.number("8")
        if num == "9":
            self.Nine.config(image=self.btn9_)
            self.number("9")
        if num == "+":
            self.plus.config(image=self.btnplus_)
            self.funcOperation("+")
        if num == "-":
            self.sub.config(image=self.btnmin_)
            self.funcOperation("-")
        if num == "*":
            self.times.config(image=self.btnX_)
            self.funcOperation("*")
        if num == "/":
            self.div.config(image=self.btndiv_)
            self.funcOperation("/")
        if num == "%":
            self.mod.config(image=self.btnmod_)
            self.funcOperation("%")
        if num == "ac":
            self.AC.config(image=self.btnac_)
            self.funcAC()
        if num == "//":
            self.floor.config(image=self.btnfloor_)
            self.funcOperation("//")
        if num == "**":
            self.power.config(image=self.btnpower_)
            self.funcOperation("**")
        if num == ".":
            self.point.config(image=self.btndec_)
            self.number(".")
        if num == "=":
            self.equals.config(image=self.btnequals_)
            self.funcEquals()
        if num == "his":
            self.historyButton.config(image=self.btnhis_)
            self.history()
        if num == "calc":
            self.exitH.config(image=self.btncalc_)
            self.exit1()

    def Release(self, event, num):
        if num == "0":
            self.Zero.config(image=self.btn0)
        if num == "1":
            self.One.config(image=self.btn1)
        if num == "2":
            self.Two.config(image=self.btn2)
        if num == "3":
            self.Three.config(image=self.btn3)
        if num == "4":
            self.Zero.config(image=self.btn4)
        if num == "5":
            self.Five.config(image=self.btn5)
        if num == "6":
            self.Six.config(image=self.btn6)
        if num == "7":
            self.Seven.config(image=self.btn7)
        if num == "8":
            self.Eight.config(image=self.btn8)
        if num == "9":
            self.Nine.config(image=self.btn9)
        if num == "+":
            self.plus.config(image=self.btnplus)
        if num == "-":
            self.sub.config(image=self.btnmin)
        if num == "*":
            self.times.config(image=self.btnX)
        if num == "/":
            self.div.config(image=self.btndiv)
        if num == "%":
            self.mod.config(image=self.btnmod)
        if num == "ac":
            self.AC.config(image=self.btnac)
        if num == "//":
            self.floor.config(image=self.btnfloor)
        if num == "**":
            self.power.config(image=self.btnpower)
        if num == ".":
            self.point.config(image=self.btndec)
        if num == "=":
            self.equals.config(image=self.btnequals)
        if num == "his":
            self.historyButton.config(image=self.btnhis)
        if num == "calc":
            self.exitH.config(image=self.btncalc)

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

    def move_L(self, event):
        if self.distance_x <= -138:
            self.distance_x = 1272
        self.distance_x -= 5
        self.master.geometry(f"130x210+{self.distance_x}+{self.distance_y}")

    def move_R(self, event):
        if self.distance_x >= 1272:
            self.distance_x = -138
        self.distance_x += 5
        self.master.geometry(f"130x210+{self.distance_x}+{self.distance_y}")

    def move_U(self, event):
        if self.distance_y >= 680:
            self.distance_y = -242
        self.distance_y -= 5
        self.master.geometry(f"130x210+{self.distance_x}+{self.distance_y}")

    def move_D(self, event):
        if self.distance_y <= -242:
            self.distance_y = 680
        self.distance_y += 5
        self.master.geometry(f"130x210+{self.distance_x}+{self.distance_y}")

    def binds(self):
        self.master.bind("<Left>", app.move_L)
        self.master.bind("<Right>", app.move_R)
        self.master.bind("<Up>", app.move_U)
        self.master.bind("<Down>", app.move_D)
        self.myList.bind("<Double-Button-1>", app.check)
        self.master.bind('<Escape>', app.close)
        self.master.bind("<BackSpace>", app.delete)
        self.master.bind("<KeyRelease>", app.process_key)
        self.Zero.bind("<Button-1>", lambda e: app.press(event=None, num="0"))
        self.Zero.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="0"))
        self.One.bind("<Button-1>", lambda e: app.press(event=None, num="1"))
        self.One.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="1"))
        self.Two.bind("<Button-1>", lambda e: app.press(event=None, num="2"))
        self.Two.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="2"))
        self.Three.bind("<Button-1>", lambda e: app.press(event=None, num="3"))
        self.Three.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="3"))
        self.Four.bind("<Button-1>", lambda e: app.press(event=None, num="4"))
        self.Four.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="4"))
        self.Five.bind("<Button-1>", lambda e: app.press(event=None, num="5"))
        self.Five.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="5"))
        self.Six.bind("<Button-1>", lambda e: app.press(event=None, num="6"))
        self.Six.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="6"))
        self.Seven.bind("<Button-1>", lambda e: app.press(event=None, num="7"))
        self.Seven.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="7"))
        self.Eight.bind("<Button-1>", lambda e: app.press(event=None, num="8"))
        self.Eight.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="8"))
        self.Nine.bind("<Button-1>", lambda e: app.press(event=None, num="9"))
        self.Nine.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="9"))
        self.plus.bind("<Button-1>", lambda e: app.press(event=None, num="+"))
        self.plus.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="+"))
        self.sub.bind("<Button-1>", lambda e: app.press(event=None, num="-"))
        self.sub.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="-"))
        self.div.bind("<Button-1>", lambda e: app.press(event=None, num="/"))
        self.div.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="/"))
        self.floor.bind("<Button-1>", lambda e: app.press(event=None, num="//"))
        self.floor.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="//"))
        self.mod.bind("<Button-1>", lambda e: app.press(event=None, num="%"))
        self.mod.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="%"))
        self.power.bind("<Button-1>", lambda e: app.press(event=None, num="**"))
        self.power.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="**"))
        self.times.bind("<Button-1>", lambda e: app.press(event=None, num="*"))
        self.times.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="*"))
        self.point.bind("<Button-1>", lambda e: app.press(event=None, num="."))
        self.point.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="."))
        self.equals.bind("<Button-1>", lambda e: app.press(event=None, num="="))
        self.equals.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="="))
        self.AC.bind("<Button-1>", lambda e: app.press(event=None, num="ac"))
        self.AC.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="ac"))
        self.historyButton.bind("<Button-1>", lambda e: app.press(event=None, num="his"))
        self.historyButton.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="his"))
        self.exitH.bind("<Button-1>", lambda e: app.press(event=None, num="calc"))
        self.exitH.bind("<ButtonRelease-1>", lambda e: app.Release(event=None, num="calc"))


if __name__ == '__main__':
    root = Tk()
    root.configure(background="grey")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.geometry("130x210+565+200")
    root.resizable(0, 0)
    root.overrideredirect(1)
    app = Main(root)
    app.binds()
    root.mainloop()
