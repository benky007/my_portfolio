import turtle
turtle.setup(500,500)
ben = turtle.Turtle()
#Gap will always be 1 but if you want to decrese the gap add 1 and then keep adding
#half as much each time.
gap = 2
sides = 7
full_turn = 360
angle = (full_turn/sides)
forward = (full_turn/sides)
turn = (angle/gap)
for i in range(sides):
    for y in range(gap):
        ben.right(turn)
        for r in range(sides):
            ben.speed(1000)
            ben.forward(forward)
            ben.right(angle)

    
