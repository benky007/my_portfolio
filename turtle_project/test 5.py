import turtle
Ben = turtle.Turtle()
turtle.setup(500,500)
window = turtle.Screen()
def forward():
    Ben.forward(50)


def start():
    window.onkey(forward, "f")
    window.listen()
    window.mainloop()
if __name__=='__main__':
    start()
