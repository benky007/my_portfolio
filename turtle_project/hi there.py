import turtle
import random
import colorsys
from random import randint
import math

window = turtle.Screen()
ben = turtle.Turtle()
ben.hideturtle()
ben.pendown()


def begin():
    ben.clear()
    ben.pendown()
    window.bgcolor("white")
    start()


def cool_shape():
    def save():
        ts = ben.getscreen()
        file1 = open("hi_there_number", "r")
        file1_read = file1.read()
        num = 0
        if file1_read == "":
            writingfile = open("hi_there_number", "w")
            writingfile.write("1")
            writingfile.close()
            num += 1
        else:
            num = int(file1_read.replace(" ", "").replace("\n", "")) + 1
            writingfile = open("hi_there_number", "w")
            writingfile.write(str(num))
            writingfile.close()
        file1.close()
        ts.getcanvas().postscript(file=f"file{str(num)}.png")

    window.bgcolor('black')
    x = 1
    ben.speed(0)
    while x < 400:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        window.colormode(255)
        ben.pencolor(r, g, b)
        ben.forward(x)
        ben.right(90.991)
        x = x + 1
    window.onkey(begin, "Escape")
    window.onkey(save, "space")
    window.listen()
    window.mainloop()


def cool_shape1():
    def save():
        ts = ben.getscreen()
        file1 = open("hi_there_number", "r")
        file1_read = file1.read()
        num = 0
        if file1_read == "":
            writingfile = open("hi_there_number", "w")
            writingfile.write("1")
            writingfile.close()
            num += 1
        else:
            num = int(file1_read.replace(" ", "").replace("\n", "")) + 1
            writingfile = open("hi_there_number", "w")
            writingfile.write(str(num))
            writingfile.close()
        file1.close()
        ts.getcanvas().postscript(file=f"file{str(num)}.png")

    phi = 180 * (3 - math.sqrt(5))
    ben.speed(0)
    num1 = 1000
    for x1 in reversed(range(0, num1)):
        ben.fillcolor(colorsys.hsv_to_rgb(x1 / num1, 1.0, 1.0))
        ben.begin_fill()
        ben.circle(5 + x1/10, None, 11)
        ben.end_fill()
        ben.right(phi)
        ben.right(.8)
    window.onkey(begin, "Escape")
    window.onkey(save, "space")
    window.listen()
    window.mainloop()


def cool_shape2():
    def save():
        ts = ben.getscreen()
        file1 = open("hi_there_number", "r")
        file1_read = file1.read()
        num = 0
        if file1_read == "":
            writingfile = open("hi_there_number", "w")
            writingfile.write("1")
            writingfile.close()
            num += 1
        else:
            num = int(file1_read.replace(" ", "").replace("\n", "")) + 1
            writingfile = open("hi_there_number", "w")
            writingfile.write(str(num))
            writingfile.close()
        file1.close()
        ts.getcanvas().postscript(file=f"file{str(num)}.png")

    phi = 180 * (3 - math.sqrt(5))
    ben.speed(0)
    num1 = 1000
    ben.penup()
    for x1 in reversed(range(0, num1)):
        ben.fillcolor(colorsys.hsv_to_rgb(x1 / num1, 1.0, 1.0))
        ben.begin_fill()
        ben.circle(5 + x1/10, None, 11)
        ben.end_fill()
        ben.right(phi)
        ben.right(.8)
    window.onkey(save, "space")
    window.listen()
    window.mainloop()


def cool_shape3():
    def save():
        ts = ben.getscreen()
        file1 = open("hi_there_number", "r")
        file1_read = file1.read()
        num = 0
        if file1_read == "":
            writingfile = open("hi_there_number", "w")
            writingfile.write("1")
            writingfile.close()
            num += 1
        else:
            num = int(file1_read.replace(" ", "").replace("\n", "")) + 1
            writingfile = open("hi_there_number", "w")
            writingfile.write(str(num))
            writingfile.close()
        file1.close()
        ts.getcanvas().postscript(file=f"file{str(num)}.png")

    phi = 180 * (3 - math.sqrt(5))
    ben.speed(0)
    num1 = 1000
    ben.penup()
    for x1 in reversed(range(0, num1)):
        ben.fillcolor(colorsys.hsv_to_rgb(0, 0, x1/num1))
        ben.begin_fill()
        ben.circle(5 + x1/10, None, 11)
        ben.end_fill()
        ben.right(phi)
        ben.right(.8)
    window.onkey(begin, "Escape")
    window.onkey(save, "space")
    window.listen()
    window.mainloop()


def shape_1():
    def save():
        ts = ben.getscreen()
        file1 = open("hi_there_number", "r")
        file1_read = file1.read()
        num = 0
        if file1_read == "":
            writingfile = open("hi_there_number", "w")
            writingfile.write("1")
            writingfile.close()
            num += 1
        else:
            num = int(file1_read.replace(" ", "").replace("\n", "")) + 1
            writingfile = open("hi_there_number", "w")
            writingfile.write(str(num))
            writingfile.close()
        file1.close()
        ts.getcanvas().postscript(file=f"file{str(num)}.png")

    window.bgcolor('black')
    ben.speed(0)
    ben.color('white')

    def drawCircles(t, size, change):
        for i in range(10):
            t.circle(size)
            size = size - change

    def drawSpecial(t, size, repeat, change):
        for i in range(repeat):
            drawCircles(t, size, change)
            t.right(360 / repeat)

    x = 0
    while x < 50:
        x += 5
        drawSpecial(ben, 100 + x, 10, 5)
        window.colormode(255)
        ben.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    window.colormode(255)
    ben.color(255, 255, 255)
    # t.color(0, 0, 0)
    drawSpecial(ben, 100 + x, 10, 5)
    window.onkey(begin, "Escape")
    window.onkey(save, "space")
    window.listen()
    window.mainloop()


def shape_2():
    def save():
        ts = ben.getscreen()
        file1 = open("hi_there_number", "r")
        file1_read = file1.read()
        num = 0
        if file1_read == "":
            writingfile = open("hi_there_number", "w")
            writingfile.write("1")
            writingfile.close()
            num += 1
        else:
            num = int(file1_read.replace(" ", "").replace("\n", "")) + 1
            writingfile = open("hi_there_number", "w")
            writingfile.write(str(num))
            writingfile.close()
        file1.close()
        ts.getcanvas().postscript(file=f"file{str(num)}.png")

    phi = 180 * (3 - math.sqrt(5))
    ben.speed(0)
    num1 = 1000
    ben.penup()
    for x1 in reversed(range(0, num1)):
        ben.fillcolor(colorsys.hsv_to_rgb(x1 / num1, 1.0, 1.0))
        ben.begin_fill()
        ben.circle(5 + x1/10)
        ben.end_fill()
        ben.right(phi)
        ben.right(.8)
    window.onkey(save, "space")
    window.listen()
    window.mainloop()


def shape_3():
    def save():
        ts = ben.getscreen()
        file1 = open("hi_there_number", "r")
        file1_read = file1.read()
        num = 0
        if file1_read == "":
            writingfile = open("hi_there_number", "w")
            writingfile.write("1")
            writingfile.close()
            num += 1
        else:
            num = int(file1_read.replace(" ", "").replace("\n", "")) + 1
            writingfile = open("hi_there_number", "w")
            writingfile.write(str(num))
            writingfile.close()
        file1.close()
        ts.getcanvas().postscript(file=f"file{str(num)}.png")

    ben.speed(0)
    num1 = 500
    num2 = num1
    ben.penup()
    for x1 in reversed(range(0, num1)):
        ben.dot(num2/200 + x1, colorsys.hsv_to_rgb(x1 / num1, 1.0, 1.0))
    print("done")
    window.onkey(save, "space")
    window.listen()
    window.mainloop()


def start():
    window.onkey(window.bye, "Escape")
    window.onkey(cool_shape, "1")
    window.onkey(cool_shape1, "2")
    window.onkey(cool_shape2, "3")
    window.onkey(cool_shape3, "4")
    window.onkey(shape_1, "5")
    window.onkey(shape_2, "6")
    window.onkey(shape_3, "7")
    window.listen()
    window.mainloop()


if __name__ == '__main__':
    start()
