import turtle
import re
import math
import functools

ben = turtle.Turtle()
drawer = turtle.Turtle()
window = turtle.Screen()


def axis(turtle1, w, h, dots):
    pos = turtle1.pos()
    head = turtle1.heading()
    turtle1.penup()
    turtle1.home()
    turtle1.pendown()
    turtle1.dot(5, "black")
    for lines in range(4):
        for i in range(dots):
            if lines < 2:
                turtle1.forward(w / dots)
            else:
                turtle1.forward(h / dots)
            turtle1.dot(50 / dots, "black")
        print(turtle1.pos())
        turtle1.goto(0, 0)
        turtle1.left(90)
    turtle1.penup()
    turtle1.goto(pos)
    turtle1.setheading(head)
    turtle1.pendown()


def process_equations(input1):
    operator = 1
    for i in input1:
        if i == "-":
            operator = -1
    if input1.find("/") != -1:
        ans = input1.split("/")
        answer = process_equations(ans[0])
        for i in range(1, len(ans)):
            answer = answer / process_equations(ans[i])
    elif input1.find(".") != -1:
        try:
            ans = input1.split(".")
            answer = (int(ans[0]) + int(ans[1]) / 10 * len(ans[1])) * operator
        except:
            answer = "error"
    else:
        answer = int(input1)
    return answer


def plot_linear(turtle1, w, h, dots, gap):
    function = input("Enter the function you wish to display in the format y = mx + c\n")
    # print(function)
    function = "".join(function.split())[2:]
    # print(function)
    correct = None
    for t in re.split("[\d]", function):
        if t.find("x") != -1:
            correct = re.split("[\d]", function)[re.split("[\d]", function).index(t)]
    if correct is None:
        pass
        print("error")
        plot_linear(turtle1, w, h, dots, gap)
    functions = re.split("[\w]", correct)
    if len(functions) == 2:
        func = functions[1]
    else:
        func = functions[0]
    # print(functions)
    grad = function.split("x")[0]
    if grad == "":
        gradient = 1
    elif grad == "-":
        gradient = -1
    else:
        gradient = process_equations(grad)
    off = function.split("x")[1]
    if off == "":
        offset = 0
    else:
        offset = process_equations(off)
    name = "y"
    # print(gradient)
    # print(offset)
    # print(func)
    # turtle1.penup()
    for i in range(-w, w + 1):
        x = i / (w / dots)
        # print(x)
        # print(gradient*x)
        exec(f'{name} = {gradient} * x {offset}\nY=y*(h/dots)\nturtle1.goto(i, Y)\n# print(i, Y)')
        if eval('Y<h') and eval('Y>(-1*h)'):
            turtle1.pendown()
        else:
            turtle1.penup()
    # plot_linear(turtle1, w, h, dots, gap)


'''
def plot(turtle1, w, h, dots):
    equation = ""
    # function = input("Enter the function you wish to display")
    function = "y=x*10+7"
    print(function)
    function = function.split("=")[1]
    print(function)
    if function == function.split(" ")[0]:
        equation = function
    else:
        function = function.split(" ")
        for element in function:
            if element == "":
                function.remove("")
        for e in range(len(function)):
            equation += function[e]
    for n in list(equation):
        if n == "+":
            # print(equation.rsplit(equation[equation.index(n)-1]))
            equation1 = re.split("(\+)", equation)
            equation1 = [equation1[0], equation1[2]]
        if n == "-":
            # print(equation.rsplit(equation[equation.index(n)-1]))
            equation1 = re.split("(\-)", equation)
            equation1 = [equation1[0], equation1[1] + equation1[2]]
    print(equation1)
    if equation1[0].find("/") != -1:
        print(equation1[0][-2:])
        print("woop")
        y1 = x/int(equation1[0][-2:])
    elif equation1[0].find("*") != -1:
        print(equation1)
        if 
'''


def windowClose():
    window.bye()


def heart(turtle1, w, h, dots):
    if w > h:
        sec = w
    else:
        sec = h
    for i in range(dots):
        for d in range(sec / dots):
            x = 0
    y1 = (math.pow(x, (2 / 3)) + math.sqrt(((math.pow(x, (4 / 3))) + 4 + (-4 * math.sqrt(x))))) / 2
    y2 = (math.pow(x, (2 / 3)) - math.sqrt(((math.pow(x, (4 / 3))) + 4 + (-4 * math.sqrt(x))))) / 2


def event_handler(key):
    if key == "a":
        axis(ben, width, height, scale)
    elif key == "Return":
        plot_linear(drawer, width, height, scale, scale1)
    elif key == "BackSpace":
        try:
            drawer.clear()
            drawer.penup()
            drawer.home()
        except:
            pass


width = 300
height = 300
scale = 10
scale1 = 1
# axis(ben, width, height, scale)
# plot_linear(drawer, width, height, scale, scale1)

window.onkey(windowClose, "Escape")
for k in ["a", "Return", "BackSpace"]:
    window.onkeypress(functools.partial(event_handler, k), key=k)
window.listen()
window.mainloop()
