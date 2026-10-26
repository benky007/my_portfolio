import turtle
from tkinter import *
from tkinter import colorchooser

window = turtle.Screen()
window.setup(500, 500)
title = ""
window.title(title)
window.bgcolor("lightblue")
# colours = ["black", "white", "red", "green", "blue", "cyan", "yellow", "magenta"]
# current_colour = 0
current_color = 0
current_pen_colour = 0
current_fill_color = 0
radius = 10
current_length = 100
memory = []
commands = []
nathan = turtle.Turtle()


def currentPos():
    nathan.goto(-638, 327.5)
    print(nathan.pos())
    print(nathan.heading())
    

def increaseLine():
    global current_length
    current_length = (current_length + 1) % 200
    print(current_length)


def decreaseLine():
    global current_length
    current_length = (current_length - 1) % 100
    print(current_length)


def pickTitle():
    global title
    title = input("Show a title name?\n")
    window.title(title)


def backgroundColour():
    global current_color
    # current_color = (current_color + 1) % len(colours)
    # window.bgcolor(colours[current_color])
    current_color = chooser('Choose your background colour')
    window.bgcolor(current_color)


'''
def decreaseHexagon():
    global current_length
    current_length = (current_length - 1) % 100
def increaseHexagon():
    global current_length
    current_length = (current_length + 1) % 100
'''


def drawHexagon():
    global current_length
    global commands
    # memory.add("Hex")
    for i in range(6):
        nathan.forward(current_length)
        nathan.right(60)
    commands.append('dH')


def decreasePentagon():
    global current_length
    current_length = (current_length - 1) % 100


def increasePentagon():
    global current_length
    current_length = (current_length + 1) % 100


def drawPentagon():
    global current_length
    global commands
    for i in range(5):
        nathan.forward(current_length)
        nathan.right(72)
    commands.append('dP')


def decreseOctagon():
    global current_length
    current_length = (current_length - 1) % 100


def increseOctagon():
    global current_length
    current_length = (current_length + 1) % 100


def drawOctagon():
    global current_length
    global commands
    for i in range(8):
        nathan.forward(current_length)
        nathan.right(45)
    commands.append('dO')


def endFill():
    global commands
    nathan.end_fill()
    commands.append('eF')


def startFill():
    global commands
    nathan.begin_fill()
    commands.append('sF')


def fillColor():
    global current_fill_color
    # current_fill_color = (current_fill_color + 1) % len(colours)
    # nathan.fillcolor(colours[current_fill_color])
    current_fill_color = chooser('Choose your fill colour')
    nathan.fillcolor(current_fill_color)


def penColour():
    global current_pen_colour
    # current_pen_colour = (current_pen_colour + 1) % len(colours)
    # nathan.pencolor(colours[current_pen_colour])
    current_pen_colour = chooser('Choose your pen colour')
    nathan.pencolor(current_pen_colour)


def circleIncrease():
    global radius
    radius = (radius + 1) % 100


def circleDecrease():
    global radius
    radius = (radius - 1) % 100


def drawCircle():
    global radius
    global commands
    nathan.circle(radius)
    commands.append('dC')


def windowClose():
    window.bye()


def widthDecrease():
    global commands
    nathan.width(nathan.width() - 1)
    commands.append('wD')


def widthIncrease():
    global commands
    nathan.width(nathan.width() + 1)
    commands.append('wI')


def penUp():
    global commands
    nathan.penup()
    commands.append('pU')


def penDown():
    global commands
    nathan.pendown()
    commands.append('pD')


def moveForward():
    global commands
    nathan.forward(current_length)
    commands.append('mF')


def chooser(line):
    color_code = colorchooser.askcolor(title=line)
    return color_code[1]


def moveLeft():
    global commands
    nathan.left(30)
    commands.append('mL')


def moveRight():
    global commands
    nathan.right(30)
    commands.append('mR')


def write():
    ans = input("What do you want to write?")
    nathan.write(ans)


def command():
    s = input('What command do you want?\nPick (1, print), (2, clear all), (3, undo), (4, ?)')
    if s == '1':
        canvas = window.getcanvas()
        canvas.postscript(file='/home/pi/Python/prints/cat.ps')
    elif s == '2':
        nathan.reset()
    elif s == '3':
        undoLast()
    else:
        print('Input invalid')


def undoLast():
    global commands
    commands = commands[:len(commands) - 1]
    for k in range(len(commands)):
        new_command = commands[k]
        if new_command == 'dH':
            drawHexagon()
        elif new_command == 'dP':
            drawPentagon()
        elif new_command == 'dO':
            drawOctagon()
        elif new_command == 'eF':
            endFill()
        elif new_command == 'sF':
            startFill()
        elif new_command == 'dC':
            drawCircle()
        elif new_command == 'wD':
            widthDecrease()
        elif new_command == 'wI':
            widthIncrease()
        elif new_command == 'pU':
            penUp()
        elif new_command == 'pD':
            penDown()
        elif new_command == 'mF':
            moveForward()
        elif new_command == 'mL':
            moveLeft()
        elif new_command == 'mR':
            moveRight()
        else:
            pass


def start():
    window.onkey(currentPos, "3")
    window.onkey(increaseLine, "1")
    window.onkey(decreaseLine, "0")
    window.onkey(write, "T")
    window.onkey(pickTitle, "t")
    window.onkey(backgroundColour, "B")
    window.onkey(startFill, "f")
    window.onkey(endFill, "F")
    window.onkey(fillColor, "c")
    window.onkey(command, 'q')
    window.onkey(drawHexagon, "x")
    window.onkey(increasePentagon, "I")
    window.onkey(decreasePentagon, "R")
    window.onkey(drawPentagon, "P")
    window.onkey(increseOctagon, "o")
    window.onkey(decreseOctagon, "D")
    window.onkey(drawOctagon, "O")
    window.onkey(penColour, "p")
    window.onkey(circleIncrease, "i")
    window.onkey(circleDecrease, "r")
    window.onkey(drawCircle, "C")
    window.onkey(moveForward, "Up")
    window.onkey(moveLeft, "Left")
    window.onkey(moveRight, "Right")
    window.onkey(penUp, "u")
    window.onkey(penDown, "d")
    window.onkey(widthIncrease, "w")
    window.onkey(widthDecrease, "W")
    window.onkey(windowClose, "Escape")
    window.listen()
    window.mainloop()


if __name__ == '__main__':
    start()
