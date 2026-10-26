import turtle
import colorsys
import time


def draw_stick(x, y, length, pensize, color, angle):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(angle)
    turtle.pensize(pensize)
    turtle.down()
    turtle.color(color)
    turtle.fd(length)


def draw_tree(x, y, length, pensize, hue, angle, fat_angle, n):
    if n == 0:
        return
    (r, g, b) = colorsys.hsv_to_rgb(hue, 1, 1)
    draw_stick(x, y, length, pensize, (r, g, b), angle)
    tx = turtle.xcor()
    ty = turtle.ycor()

    draw_tree(tx, ty, length - 1, pensize * 0.7, hue - 1/hue, angle + fat_angle, fat_angle, n - 1)
    draw_tree(tx, ty, length - 1, pensize * 0.7, hue - 1/hue, angle - fat_angle, fat_angle, n - 1)


turtle.Screen().getcanvas().master.geometry("800x800+10+10")
turtle.title("Rainbow Colored Tree")
turtle.speed(0)
turtle.hideturtle()
# turtle.tracer(0)
turtle.bgcolor('black')

draw_tree(0, -30, 50, 6, 20, 90, 25, 6)
turtle.mainloop()
