import turtle
turtle.setup(500,500)
window = turtle.Screen()
window.title("Shape Maker 101")
window.bgcolor("white")
ben = turtle.Turtle()
#Gap will always be 1 but if you want to decrese the gap add 1 and then keep addinghalf as much each time.
colors = ["black", "white", "red", "green", "blue", "cyan", "yellow", "magenta"]
current_pen_color = 0
current_color = 0
line_length = 0
line_width = 0
speed = 0
gap = 0
sides = 0
full_turn = 360
def changeSpeed():
    global speed
    speed = (speed - 1) % 100
def hideTurtle():
    ben.hideturtle()
def showTurtle():
    ben.showturtle()
def decreseLine():
    global line_length
    line_length = (line_length - 1) % 50
    print(line_length)
def lineLength():
    global line_length
    line_length = (line_length + 1) % 50
    print(line_length)
def decreseWidth():
    global line_width
    line_width = (line_width - 1) % 50
    print(line_width)
def lineWidth():
    global line_width
    line_width = (line_width + 1) % 50
    print(line_width)
def windowClose():
    window.bye()
def backgroundColor():
    global current_color
    current_color = (current_color + 1) % len(colors)
    window.bgcolor(colors[current_color])
def penColor():
    global current_pen_color
    current_pen_color = (current_pen_color + 1) % len(colors)
    ben.pencolor(colors[current_pen_color])
def changeGap():
    global gap
    gap = (gap + 1) % 50
def changeSides():
    global sides
    sides = (sides + 1) % 100
def makeShape():
    angle = (full_turn/sides)
    forward = (full_turn/sides +line_length)
    ben.width(line_width)
    for i in range(sides):
        for y in range(gap):
            ben.right(angle/gap)
            for r in range(sides):
                ben.speed(speed)
                ben.forward(forward)
                ben.right(angle)

def decreseSides():
    global sides
    sides = (sides - 1) % 100    
def start():
    window.onkey(showTurtle, "S")
    window.onkey(hideTurtle, "H")
    window.onkey(decreseSides, "S")
    window.onkey(makeShape, "m")
    window.onkey(changeSpeed, "f")
    window.onkey(changeGap, "g")
    window.onkey(changeSides, "s")
    window.onkey(penColor, "p")
    window.onkey(backgroundColor, "b")
    window.onkey(lineWidth, "w")
    window.onkey(lineLength,"l")
    window.onkey(windowClose, "Escape")
    window.listen()
    window.mainloop()
if __name__=='__main__':
    start()

    
