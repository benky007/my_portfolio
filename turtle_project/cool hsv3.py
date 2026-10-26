import turtle
import colorsys


def draw_stick(x, y, length, pensize, color, angle, angle2):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(angle2)
    turtle.pensize(pensize)
    turtle.down()
    turtle.color(color)
    turtle.circle(int(length), float(angle))


def draw_tree(x, y, angle2, length, pensize, hue, angle, n, run):
    if n == 0:
        return
    (r, g, b) = colorsys.hsv_to_rgb(hue, 1, 0.8)
    if run == 1:
        turtle.left(90)
        turtle.penup()
        turtle.goto(x, y-length/2)
        start = turtle.heading()
        turtle.pendown()
        turtle.color((r, g, b))
        turtle.pensize(pensize)
        turtle.forward(length/2)
        turtle.penup()
    draw_stick(x, y, length, pensize, (r, g, b), angle, angle2)
    tx = turtle.xcor()
    ty = turtle.ycor()
    angle2 = turtle.heading()

    draw_tree(tx, ty, angle2, length - 1/length, pensize - 1/pensize, hue - 1/hue+1, angle, n - 1, 0)
    draw_tree(tx, ty, angle2, (length - 1/length) * -1, pensize - 1/pensize, hue - 1/hue+1, angle, n - 1, 0)


turtle.Screen().getcanvas().master.geometry("800x800+10+10")
turtle.title("Rainbow Colored Tree")
turtle.speed(0)
turtle.hideturtle()
# turtle.tracer(0)
turtle.bgcolor('black')

draw_tree(0, 0, 90, 100, 5, 20, 15, 20, 1)
draw_tree(0, 0, 90, -100, 5, 20, 15, 20, 0)
print("done")
turtle.mainloop()
