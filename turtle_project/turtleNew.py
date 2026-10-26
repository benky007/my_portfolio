import turtle

window = turtle.Screen()
window.setup(500, 500)
title = "turtle"
window.title(title)
window.bgcolor("lightblue")
colours = ["black", "white", "red", "green", "blue", "cyan", "yellow", "magenta"]
ben = turtle.Turtle()
ben.pensize(8)

ben.penup()
ben.goto(-15, -170)
ben.pendown()
for i in range(36):
    ben.forward(30)
    ben.left(10)

ben.penup()
ben.goto(-95, 20)
ben.pendown()
ben.left(90)
for u in range(45):
    ben.forward(2)
    ben.right(4)

ben.penup()
ben.goto(35, 20)
ben.pendown()
ben.left(-180)
for y in range(45):
    ben.forward(2)
    ben.right(4)

ben.penup()
ben.goto(-25, -20)
ben.pendown()

ben.setheading(0)
ben.forward(50)
ben.right(120)
ben.forward(50)
ben.right(120)
ben.forward(50)
ben.right(180)
ben.forward(50)
ben.setheading(-90)
mouth = ben.pos()

for p in range(80):
    ben.forward(2)
    ben.right(2)

ben.penup()
ben.goto(mouth)
ben.pendown()
ben.setheading(-90)
for o in range(80):
    ben.forward(2)
    ben.left(2)

ben.penup()
ben.goto(-133.02, 108.89)
ben.pendown()
ben.setheading(90)
ben.forward(120)
ben.right(130)
ben.forward(100)

ben.penup()
ben.goto(136.02, 108.89)
ben.pendown()
ben.setheading(90)
ben.forward(120)
ben.left(130)
ben.forward(100)

ben.penup()
ben.goto(-15.95, -101.89)
ben.setheading(-90)
ben.pendown()
for y in range(19):
    ben.forward(2.5)
    ben.left(10)

ben.penup()
ben.goto(mouth)
ben.setheading(-90)
ben.forward(175)
ben.write('bob', align="center", font=("arial", 50, "normal"))
canvas = window.getcanvas()
canvas.postscript(file='/home/pi/Python/prints/cat.ps')


def bye():
    window.bye()


def start():
    window.onkey(bye, 'Escape')
    window.listen()
    window.mainloop()


start()
