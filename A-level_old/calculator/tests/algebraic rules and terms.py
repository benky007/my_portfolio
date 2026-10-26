import math
from sympy import *
import re

expression = "3ab + 7ab + 2b(4a - 2b)"


class change:
    def __init__(self, og):
        self.x0 = None
        self.x1 = None
        self.x2 = None
        self.x3 = None
        self.x4 = None
        self.x5 = None
        self.x6 = None
        self.x7 = None
        self.x8 = None
        self.x9 = None
        self.x10 = None
        self.x11 = None
        self.x12 = None
        self.x13 = None
        self.x14 = None
        self.x15 = None
        self.x16 = None
        self.x17 = None
        self.x18 = None
        self.x19 = None
        self.answer = 0
        self.og = og
        self.vars()
        current = self.process(self.og)
        current = simplify(current)
        spited = str(current)
        spited = spited.split(" ")
        for count, section in enumerate(spited):
            for element in section:
                if element == "(":
                    start = count
                if element == ")":
                    end = count
        if start == end:
            next = self.parse(spited[start])
            spited[start] = next
        else:
            next = self.parse("".join(spited[start:end + 1]))
            spited[start:end + 1] = self.process(str(next)).split(" ")
        spited = " ".join(spited)
        print(spited)
        self.final = simplify(spited)
        print(self.final)
        spited = str(self.final).replace("*", "")
        spited = spited.split(" ")
        for count, section in enumerate(spited):
            for element in section:
                if element == "(":
                    start = count
                if element == ")":
                    end = count
        if start == end:
            next = self.parse(spited[start])
            spited[start] = next
        else:
            next = self.parse("".join(spited[start:end + 1]))
            spited[start:end + 1] = self.process(str(next)).split(" ")
        spited = " ".join(spited)
        print(spited)
        self.final = spited

    def vars(self):
        letters = list(dict.fromkeys(re.findall("[a-zA-Z]+", self.og)))
        try:
            self.x0 = symbols(letters[0])
            self.x1 = symbols(letters[1])
            self.x2 = symbols(letters[2])
            self.x3 = symbols(letters[3])
            self.x4 = symbols(letters[4])
            self.x5 = symbols(letters[5])
            self.x6 = symbols(letters[6])
            self.x7 = symbols(letters[7])
            self.x8 = symbols(letters[8])
            self.x9 = symbols(letters[9])
            self.x10 = symbols(letters[10])
            self.x11 = symbols(letters[11])
            self.x12 = symbols(letters[12])
            self.x13 = symbols(letters[13])
            self.x14 = symbols(letters[14])
            self.x15 = symbols(letters[15])
            self.x16 = symbols(letters[16])
            self.x17 = symbols(letters[17])
            self.x18 = symbols(letters[18])
            self.x19 = symbols(letters[19])
        except IndexError:
            pass

    def process(self, processing):
        last_char = ""
        new = processing
        count1 = 0
        for char in new:
            char = new[count1]
            if last_char == " " and char == "(" and (new[count1 - 2].isdigit() or new[count1 - 2].isalpha()):
                # print("1")
                new = new[:count1 - 1] + new[count1:]
                count1 -= 1
                last_char = new[count1 - 1]
            if last_char == " " and char.isalpha() and new[count1 - 2].isdigit():
                # print("2")
                new = new[:count1 - 1] + new[count1:]
                count1 -= 1
                last_char = new[count1 - 1]
            if last_char == " " and ((char.isdigit() and new[count1 - 2] == "*") or (char == "*" and new[count1 - 2].isdigit())):
                # print("3")
                new = new[:count1 - 1] + new[count1:]
                count1 -= 1
                last_char = new[count1 - 1]
            if last_char == " " and ((char.isalpha() and new[count1 - 2] == "*") or (char == "*" and new[count1 - 2].isalpha())):
                # print("4")
                new = new[:count1 - 1] + new[count1:]
                count1 -= 1
                last_char = new[count1 - 1]
            if (char.isdigit() or char.isalpha()) and (last_char == "+" or last_char == "-"):
                # print("5")
                new = new[:count1] + " " + new[count1:]
                count1 += 1
            if (char == "+" or char == "-") and (last_char.isdigit() or last_char.isalpha()):
                # print("6")
                new = new[:count1] + " " + new[count1:]
                count1 += 1
            if last_char == " " and char.isalpha() and new[count1 - 2].isalpha():
                # print("7")
                new = new[:count1 - 1] + new[count1:]
                count1 -= 1
                last_char = new[count1 - 1]
            if last_char.isdigit() and char.isalpha():
                # print("8")
                new = new[:count1] + "*" + new[count1:]
                count1 += 1
            if last_char.isalpha() and char.isalpha():
                # print("9")
                new = new[:count1] + "*" + new[count1:]
                count1 += 1
            last_char = char
            count1 += 1
        return new

    def parse(self, s):
        li = []

        open1 = 0
        closed = False
        start_index = -1

        for index, c in enumerate(s):
            if c == '(':
                if open1 == 0:
                    start_index = index
                open1 += 1

            elif c == ')':
                open1 -= 1
                if open1 == 0:
                    closed = True

            elif closed:
                li.append(s[start_index: index + 1])
                closed = False

            elif open1 == 1:
                li.append(c)

        start = s[:start_index]
        past = ""
        for index, element in enumerate(li):
            if element.isdigit():
                li[index] = start + "*" + li[index]
            if element == ".":
                element[index - 1:index] = element[index - 1] + element[index]
            if past.isdigit() and element.isdigit():
                element[index - 1:index] = element[index - 1] + element[index]
            past = element

        return " ".join(li)

    def simp(self, expr):
        numbers = expr.split("*")
        coefficient = 1
        ex = [""]
        for number in numbers:
            try:
                if number.isdigit() or int(number) < 0:
                    coefficient = coefficient * int(number)
            except ValueError:
                if number.isalpha():
                    if len(ex) == 0:
                        ex[0] = number
                    else:
                        last = 0
                        for index, i in enumerate(ex):
                            if i < number:
                                last = (index, number)
                                print(last)
                            if i == number:
                                ex.insert(index+1, number)
                        ex.insert(last[0]-1, last[1])
        return str(coefficient) + "".join(ex)

    def get(self):
        return self.final


calc = change(expression)
print(calc.get())
print(calc.simp("2*b*9*a*x*3*c"))
