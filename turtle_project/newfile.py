import turtle
angle = 239 #if you set it to anything below 90 it does a curcular pattern
step = 10
scale = 63
width = 10
window = turtle.Screen()
window.bgcolor("white")
ben = turtle.Turtle()
ben.color("black")
ben.width(width)
ben.speed(0)
ben.pendown()
size=0
for i in range(scale):
   size += step
   ben.left(angle)
   ben.forward(size)
window.mainloop()