import turtle
import time
turtle.setup(500, 500)
window = turtle.Screen()
title = "Angles Maths Problems"
window.title(title)
window.bgcolor("lightblue")
colours = ["black", "white", "red", "green", "blue", "cyan", "yellow", "magenta"]
X = 0
me = turtle.Turtle()
me.hideturtle()

def shape1():
    global X
    me.penup()
    me.right(180)
    me.forward(100)
    me.right(180)
    me.pendown()
    me.forward(40)
    me.write("2X + 20")
    me.forward(60)
    me.left(150)
    me.forward(100)
    me.right(180)
    me.forward(100)
    me.left(30)
    me.right(180)
    me.forward(0)
    me.right(180)
    me.write("20X + 50")
    me.forward(100)
    me.penup()
    me.right(180)
    me.forward(100)
    me.forward(100)
    me.right(90)
    me.forward(200)
    me.right(90)
    me.write("Press 'return' when you know what X == ?")
    X = 5
    
def shape2():
    pass
    
def shape3():
    pass
    
def shape4():
    pass
    
def shape5():
    pass
    
def shape6():
    pass
    
def shape7():
    pass
    
def shape8():
    pass
    
def shape9():
    pass
    
def shape10():
    pass

def click():
    global X
    ans = int(input("What do you think X is equal to ?\n"))
    if ans == X:
        points = 1
        Next = int(input("Welldone, would you like to do another question or\nwould you like to get your score and leave(1 or 2)\n"))
        if Next == 1:
            print("Nice job, your points are", str(points))
            time.sleep(5)
            start()
        else:
            print("Okay, your points are ", str(points), " and goodbye")
            time.sleep(5)
            window.bye()
    else:
        points = 0
        Next = int(input("Terrible the answer is ", str(X), ". So would you like try another \nquestion or would you like to get your score and leave(1 or 2)\n"))
        if Next == 1:
            print("Okay, your points are ", str(points))
            time.sleep(5)
            start()
        else:
            print("Good, your points are ", str(points), " and goodbye")
            time.sleep(5)
            window.bye()

def escape():
    window.bye()

def start():
    me.clear()
    print("What shape problem would you like to see(0-9)?\n")
    window.onkey(shape1, "0")
    window.onkey(shape2, "1")
    window.onkey(shape3, "2")
    window.onkey(shape4, "3")
    window.onkey(shape5, "4")
    window.onkey(shape6, "5")
    window.onkey(shape7, "6")
    window.onkey(shape8, "7")
    window.onkey(shape9, "8")
    window.onkey(shape10, "9")
    window.onkey(click, "Return")
    window.onkey(escape, "Escape")
    window.listen()
    window.mainloop()
    
if __name__ == '__main__':
    start()
