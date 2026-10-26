import turtle
turtle.setup(500,500)
ben = turtle.Turtle()
for r in range(2):
    ben.left(18)
    for i in range(4):
        ben.forward(36)
        ben.left(36)
    ben.forward(70)
ben.goto(0, 0)
ben.hideturtle()
