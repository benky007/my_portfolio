# import turtle
import re
import time
from sympy import symbols

# ben = turtle.Turtle()
# draw = turtle.Turtle()
# window = turtle.Screen()
# ben.speed(0)

function = "y=x^2 + 4x + 4"


def process1(func):
    func = "".join(function.split(" "))
    if func[0:2] == "y=":
        func = func[2:]
    parts = re.split(r'^\S=|([+-])', func)
    for i, part in enumerate(parts):
        if part == "+" or part == "-":
            parts[i] = "".join(parts[i] + parts[i + 1])
            parts.remove(parts[i + 1])
    var1 = "".join(parts)
    for i, character in enumerate(var1):
        if character == "^":
            var1 = var1.replace("^", "**")
        if character == "x" and var1[i - 1].isnumeric():
            var1 = var1[:i - 1] + "*" + var1[i - 1:]
    return var1, symbols('x')


def process2():
    exec("global y; y = equation")
    return y


def process(func):
    func = "".join(function.split(" "))
    if func[0:2] == "y=":
        func = func[2:]
    parts = re.split(r'^\S=|([+-])', func)
    for i, part in enumerate(parts):
        if part == "+" or part == "-":
            parts[i] = "".join(parts[i] + parts[i + 1])
            parts.remove(parts[i + 1])
    return parts


def dot(turtle1, rad, fill, fColor, pColor):
    turtle1.color(pColor)
    turtle1.penup()
    turtle1.right(90)
    turtle1.forward(rad)
    turtle1.left(90)
    turtle1.pendown()
    if fill and fColor != "":
        turtle1.fillcolor(fColor)
        turtle1.begin_fill()
    turtle1.circle(rad)
    if fill:
        turtle1.end_fill()
    turtle1.penup()
    turtle1.left(90)
    turtle1.forward(rad)
    turtle1.right(90)
    turtle1.pendown()


def axis(turtle1, w, h, scale):
    pos = turtle1.pos()
    head = turtle1.heading()
    turtle1.penup()
    turtle1.home()
    turtle1.pendown()
    dot(turtle1, 5, True, 'black', 'black')
    for sections in range(4):
        turtle1.forward(w / 2)
        turtle1.goto(pos)
        sec = w / 2 / scale
        # turtle1.write(int(sec)+bool(sec%1))
        # turtle1.write(sec)
        for lines in range(int(sec) + bool(sec % 1)):
            turtle1.forward(w / 2 / sec)
            dot(turtle1, 2, True, 'black', 'black')
            turtle1.left(90)
            turtle1.forward(h / 2)
            turtle1.left(180)
            turtle1.forward(h)
            turtle1.left(180)
            turtle1.forward(h / 2)
            turtle1.left(270)
        turtle1.goto(pos)
        turtle1.left(90)


# axis(ben, 500, 500, 25)
y = 0
equation, x = process1(function)
y = process2()

print(y)

# print(new)
time.sleep(2)
# ben.write(new)

# window.mainloop()