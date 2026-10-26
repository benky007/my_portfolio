import turtle
turtle.setup(500,500)
window = turtle.Screen()
title = ""
window.title(title)
window.bgcolor("lightblue")
ben = Turtle.turtle()
Turtle.Pen("turtle")
count = 0
def draw(val):
    bla = (count - 1)*45
    if count == 0:
        if val == 1:
            ben.begin_fill()
        if val == 0:
            ben.speed(0)
        ben.forward(100)
        ben.right(67.5)
        ben.forward(0)
        ben.right(67.5)
        ben.forward(100)
        ben.right(180)
        
