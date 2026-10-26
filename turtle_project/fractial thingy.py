import turtle
import math
import random
import sympy

ben = turtle.Turtle()
window = turtle.Screen()
ben.speed(0)
# ben.hideturtle()

x = sympy.symbols("x")
eq1 = sympy.sympify("-1*50*sqrt(3)*x")
eq2 = sympy.sympify("x*sqrt(3)+100*sqrt(3)")
eq3 = sympy.sympify("-1*x*sqrt(3)+100*sqrt(3)")


def half(coord1, coord2):
    result = [0, 0]
    result[0] = coord1[0]-((coord1[0]-coord2[0])/2)
    result[1] = coord1[1]-((coord1[1]-coord2[1])/2)
    return result


def dot(t, rad):
    t.penup()
    t.right(90)
    t.forward(rad)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(rad)
    t.right(90)
    t.pendown()


def start(t, eqs, x):
    t.penup()
    t.goto(-200, -1*(100*math.sqrt(3)))
    dot(t, 1)
    t.penup()
    t.goto(200, -1*(100*math.sqrt(3)))
    dot(t, 1)
    t.penup()
    t.goto(0, 100*math.sqrt(3))
    dot(t, 1)
    dots = [(0, 100*math.sqrt(3)), (-200, -1*(100*math.sqrt(3))), (200, -1*(100*math.sqrt(3)))]
    randomizing = True
    while randomizing:
        coords = (random.uniform(-200, 200), random.uniform(-1*50*math.sqrt(3), 50*math.sqrt(3)))
        # print(eqs[0].subs(x, 1))
        # print((eqs[1].subs(x, coords[0]))/2)
        # print((eqs[1].subs(x, coords[0]))/2)
        if eqs[0].subs(x, 1) < coords[1] and eqs[1].subs(x, coords[0]) > 2*coords[1] and eqs[1].subs(x, coords[0]) > 2*coords[1]:
            randomizing = False
        print(coords)
    t.penup()
    t.goto(coords)
    dot(t, 1)
    cool = False
    while not cool:
        try:
            pos = random.randint(0, 2)
            coords = half(coords, dots[pos])
            t.penup()
            t.goto(coords)
            dot(t, 1)
        except KeyboardInterrupt:
            cool = True




start(ben, (eq1, eq2, eq3), x)

window.mainloop()
