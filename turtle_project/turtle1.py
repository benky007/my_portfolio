import turtle
ben = turtle.Turtle()
window = turtle.Screen()
window.setup(500, 500)


def forward():
    ben.forward(100)


def left():
    ben.left(10)


def right():
    ben.right(10)


def hide():
    ben.hideturtle()


def show():
    ben.showturtle()


def up():
    ben.up()


def down():
    ben.down()


def start():
    window.onkey(forward, "Up")
    window.onkey(left, "Left")
    window.onkey(right, "Right")
    window.onkey(hide, "h")
    window.onkey(show, "s")
    window.onkey(up, "u")
    window.onkey(down, "d")
    window.listen()
    window.mainloop()


if __name__ == "__main__":
    start()
