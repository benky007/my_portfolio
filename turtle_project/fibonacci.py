import turtle
import math

window = turtle.Screen()
window.setup(500, 500)
title = ""
window.title(title)
window.bgcolor("#A827CF")
ben = turtle.Turtle()
ben.speed('fastest')

fib = []
'''
ben.goto(0, 0)
ben.setheading(0)
ben.penup()
ben.goto(-640, 330)
ben.pendown()
for f in range(66):
    for i in range(128):
        ben.forward(10)
        # print(ben.pos(), (128*i/2, 65*f/2))
        ben.right(90)
        ben.forward(10)
        ben.right(90)
        ben.forward(10)
        ben.right(90)
        ben.forward(10)
        ben.right(90)
        ben.forward(10)
    ben.right(90)
    ben.forward(20)
    ben.right(90)
    ben.penup()
    ben.forward(1280)
    ben.pendown()
    ben.right(90)
    ben.forward(10)
    ben.right(90)
    '''

ben.color("#21EB49")
ben.width(3)

for n in range(100):
    n = n + 1
    num = eval(str((1 / math.sqrt(5)) * ((((1 + math.sqrt(5)) / 2) ** n)-(((1 - math.sqrt(5)) / 2) ** n))))
    fib.append(str(num).split('.')[0])
# print(fib)

ben.setheading(270)
ben.penup()
ben.goto(0, 0)
ben.pendown()
for i in range(len(fib)):
    # print(fib[i])
    # print(fib)
    ben.circle(int(fib[i])*10, 90)


def close():
    window.bye()


print("done")
window.onkey(close, "Escape")
window.listen()
window.mainloop()
