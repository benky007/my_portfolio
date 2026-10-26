import turtle
import math
import sympy

ben = turtle.Turtle()
ben.speed(0)
ben.hideturtle()
drawer = turtle.Turtle()
drawer.speed(0)
window = turtle.Screen()


def dot(t, rad):
    t.penup()
    t.right(90)
    t.forward(rad)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(rad)
    t.right(90)
    t.pendown()


def axis(turtle1, w, h, dots, total):
    pos = turtle1.pos()
    head = turtle1.heading()
    turtle1.fillcolor('black')
    turtle1.penup()
    turtle1.home()
    turtle1.pendown()
    dot(turtle1, 2)
    for lines in range(2):
        for i in range(total[0] // dots):
            turtle1.forward(w / (total[0] / dots))
            if total[0] / dots > total[0] // dots:
                turtle1.forward((total[0] - ((total[0] // dots) * dots)) / (total[0] // dots))
            dot(turtle1, 2)
        turtle1.goto(0, 0)
        turtle1.left(180)
    turtle1.left(270)
    for lines in range(2):
        for i in range(total[1] // dots):
            turtle1.forward(h / (total[1] / dots))
            if total[1] / dots > total[0] // dots:
                turtle1.forward((total[1] - ((total[1] // dots) * dots)) / (total[1] // dots))
            dot(turtle1, 2)
        turtle1.goto(0, 0)
        turtle1.left(180)
    turtle1.penup()
    turtle1.goto(pos)
    turtle1.setheading(head)
    turtle1.pendown()


def plot(draw, w, h, total, acc, equ):
    x, y = sympy.symbols('x y')
    eq = sympy.sympify(equ)
    count = 0
    for i in range(-1 * total[0] * acc, total[0] * acc):
        if -1 * total[1] <= eq.subs(x, i / acc) <= total[1]:
            count += 1
            if count == 1:
                draw.penup()
                draw.goto(w * ((i / acc) / xmax), h * (eq.subs(x, i / acc) / ymax))
                draw.pendown()
            print(f"{i/acc}, {eq.subs(x, i / acc)}")
            draw.goto(w * ((i / acc) / xmax), h * (eq.subs(x, i / acc) / ymax))
        else:
            count = 0


def windowClose():
    window.bye()


def heart(turtle1, w, h, dots):
    if w > h:
        sec = w
    else:
        sec = h
    for i in range(dots):
        for d in range(sec / dots):
            x = 0
    y1 = (math.pow(x, (2 / 3)) + math.sqrt(((math.pow(x, (4 / 3))) + 4 + (-4 * math.sqrt(x))))) / 2
    y2 = (math.pow(x, (2 / 3)) - math.sqrt(((math.pow(x, (4 / 3))) + 4 + (-4 * math.sqrt(x))))) / 2
    turtle1.goto(y1, y2)


width = 300
height = 300
scale = 1
xmax = 10
ymax = 10
accuracy = 100
axis(ben, width, height, scale, (xmax, ymax))
running = True
while running:
    equation = input("Enter the equation you want to plot(or CLR to clear the previous or ESC to leave)\n")
    if equation == "CLR":
        drawer.clear()
    elif equation == "ESC":
        windowClose()
    else:
        plot(drawer, width, height, (xmax, ymax), accuracy, equation)

window.mainloop()
