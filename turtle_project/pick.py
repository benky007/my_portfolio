import turtle
import time

bg = 'pink'
pc = 'purple'
fc = 'green'
full = 360
wd = 1
gap = 6
a = 1
ful = int(full/gap)
fula = int(full*a)
sides = 8
sleep = 50
rad = 100
forward = int(50)
star_f = 250
left = float(full/sides)
star = 0
circle = 0
ss = 0
fil = 1				#suggested sides under 8

window = turtle.Screen()
ben = turtle.Turtle()
turtle.setup(500, 500)
window.bgcolor(bg)
ben.color(pc)
ben.fillcolor(fc)
ben.hideturtle()
ben.speed(0)
ben.setpos(0, 0)
ben.width(wd)

if star != 1 and star != 0:
	star = 1
	
elif ss != 1 and ss != 0:
	ss = 1
	
elif circle != 1 and circle != 0:
	circle = 1
	
elif fil != 1 and fil != 0:
	fil = 1

elif star == 1 and circle == 1:
	ben.write("Sorry", align = "center", font  = ("Arial", 8, "normal"))
	time.sleep(5)
	ben.clear()
	ben.write("ERROR: Can't do a circle and a star at the same time.", align = "center", font = ("Arial", 8, "normal"))
	time.sleep(10)
	window.bye()

if star == 1 and ss != 1 and circle != 1 and fil != 1:
	for i in range(fula):
		ben.left(gap)
		for d in range(5):
			ben.forward(star_f)
			ben.left(144)
	time.sleep(sleep)
	
elif circle == 1 and ss != 1 and fil != 1 and star != 1:
	for i in range(fula):
		ben.left(gap)
		ben.circle(rad)
	circle = 0
	time.sleep(sleep)
	
elif ss == 1 and circle != 1 and star != 1 and fil != 1:
	for i in range(sides):
		ben.forward(forward)
		ben.left(left)
	ss = 0
	time.sleep(sleep)
	
elif ss == 1 and star == 1 and circle != 1 and fil != 1:
	for i in range(5):
		ben.forward(500)
		ben.left(144)
	ss = 0
	star = 0
	time.sleep(sleep)
elif ss == 1 and circle == 1 and star != 1 and fil != 1:
	ben.circle(rad)
	ss = 0
	circle = 0
	time.sleep(sleep)
	
elif fil == 1 and star != 1 and circle != 1 and ss != 1:
	ben.pendown()
	for i in range(ful):
		ben.left(gap)
		ben.begin_fill()
		for d in range(sides):
			ben.forward(forward)
			ben.left(left)
		ben.end_fill()
	time.sleep(sleep)
	
elif fil ==1 and circle == 1 and star != 1 and ss != 1:
	for i in range(ful):
		ben.left(gap)
		ben.color(fc)
		ben.begin_fill()
		ben.circle(rad)
		ben.end_fill()
		ben.color(pc)
		ben.width(5)
		ben.circle(rad)
		ben.width(1)
	time.sleep(sleep)
	
elif fil == 1 and star == 1 and circle != 1 and ss != 1:
	for i in range(ful/a):
		ben.left(gap)
		ben.begin_fill()
		for d in range(5):
			ben.color(fc)
			ben.forward(star_f)
			ben.left(144)
		ben.end_fill()
		ben.color(pc)
		ben.width(5)
		ben.forward(star_f)
		ben.left(144)
		ben.width(1)
	time.sleep(sleep)
	
elif fil == 1 and circle == 1 and ss == 1 and star != 1:
	ben.color(fc)
	ben.begin_fill()
	ben.circle(rad)
	ben.end_fill()
	ben.color(pc)
	ben.width(5)
	ben.circle(rad)
	ben.width(1)
	time.sleep(sleep)
	
elif fil == 1 and star == 1 and ss == 1 and circle != 1:
	ben.color(fc)
	ben.begin_fill()
	for i in range(5):
		ben.forward(star_f)
		ben.left(144)
	ben.end_fill()
	ben.color(pc)
	ben.width(5)
	ben.forward(star_f)
	ben.left(144)
	ben.width(1)
	time.sleep(sleep)
else:	
	for i in range(fula):
		ben.left(gap)
		for d in range(sides):
			ben.forward(forward)
			ben.left(left)
	time.sleep(sleep)
