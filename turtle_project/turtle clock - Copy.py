import time
import datetime
import turtle


def hexClock():
    global clock
    global font_size
    clock = "hexadecimal"
    font_size = 75


def binaryClock():
    global clock
    global font_size
    clock = "binary"
    font_size = 50


def decimalClock():
    global clock
    global font_size
    font_size = 75
    clock = "decimal"


def start():
    global clock
    global font_size
    turtle.setup()
    window = turtle.Screen()
    window.title("Decimal clock")
    window.bgcolor("white")
    font_size = 75
    ben = turtle.Turtle()
    ben.hideturtle()

    clock = "decimal"
    window.onkey(hexClock, "h")
    window.onkey(decimalClock, "d")
    window.onkey(binaryClock, "b")
    window.listen()

    window.tracer(0)  # Control animation updates ourself

    try:
        while True:
            ben.clear()
            window.title(clock.capitalize() + " clock")
            ben.sety(-font_size / 2)
            t = datetime.datetime.now()
            hour, minute, second = t.strftime("%T").split(":")
            if clock == "binary":
                hour = bin(int(hour))[2:].zfill(5)
                minute = bin(int(minute))[2:].zfill(5)
                second = bin(int(second))[2:].zfill(5)
            if clock == "hexadecimal":
                hour = hex(int(hour))[2:].zfill(2).upper()
                minute = hex(int(minute))[2:].zfill(2).upper()
                second = hex(int(second))[2:].zfill(2).upper()
            ben.undo()
            ben.write(hour + ":" + minute + ":" + second, move=False, align="center",
                      font=("arial", font_size, "normal"))
            window.update()
            time.sleep(.1)
        window.mainloop()
    except:
        pass


if (__name__ == "__main__"):
    start()
