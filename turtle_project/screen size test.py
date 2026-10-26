import turtle

turtle.setup(500, 500)
window = turtle.Screen()
window.bgcolor("dodger blue")
ben = turtle.Turtle()
ben.speed("fastest")

print(turtle.screensize())

window.setup(100, 100)
X = 10
Y = 10


def setup_win(X, Y):
    window.setup(X, Y)


def up(Y):
    Y += 1
    setup_win(X, Y)


def down(Y):
    Y = Y - 1
    setup_win(X, Y)


def left(X):
    X += 1
    setup_win(X, Y)


def right(X):
    X = X - 1
    setup_win(X, Y)


def start():
    window.onkey(up(Y), "Up")
    window.onkey(down(Y), "Down")
    window.onkey(left(X), "Left")
    window.onkey(right(X), "Right")
    window.listen()
    window.mainloop()


if __name__ == '__main__':
    start()

'''
mine turtle-1276, 655
mine comp-1920, 1080
mine size diag-14"
mine size X, Y(cm)-17.43, 31

mom turtle-1348, 704
mom comp-1366 768
mom size diag-15"
mom size X, Y(cm)-18.68, 33.21
'''
