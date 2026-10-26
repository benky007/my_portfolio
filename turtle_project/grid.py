import turtle

window = turtle.Screen()
window.setup(500, 500)
title = ""
window.title(title)
window.bgcolor("#A827CF")
ben = turtle.Turtle()
ben.speed('fastest')

ben.goto(0, 0)
ben.setheading(0)
ben.penup()
ben.goto(-638, 328)
ben.pendown()
for f in range(12):
    for i in range(12):
        ben.forward(10)
        ben.right(90)
        ben.forward(10)
        ben.right(90)
        ben.forward(10)
        ben.right(90)
        ben.forward(10)
        ben.right(90)
        ben.forward(10)
    ben.right(90)
    ben.penup()
    ben.forward(20)
    ben.right(90)
    ben.forward(120)
    ben.right(90)
    ben.forward(10)
    ben.pendown()
    ben.right(90)

ben.color('#21EB49')
ben.width(3)

ben.penup()
ben.goto(-640, 270)
ben.setheading(270)
ben.pendown()
ben.circle(60)


def close():
    window.bye()


print("done")
window.onkey(close, "Escape")
window.listen()
window.mainloop()
