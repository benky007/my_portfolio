import turtle
count = 0
class Main():
    def __init__(self):
        wn = turtle.Screen()
        wn.setup(600, 600)
        screen = wn.getcanvas()
        self.t = turtle.Turtle()
        self.x = 300
        self.y = 300
        screen.bind('<Motion>', self.set_coords)
        self.run()
    def set_coords(self, event):
        self.x = event.x
        self.y = event.y
    def run(self):
        while True:
            self.t.setposition(self.x-300, (self.y*-1)+300)
            wn.listen()    
            wn.onscreenclick(click, 1)
            print('3')
            wn.mainloop()
    def click(self):
        count+=1
        if count == 0:
            self.t.penup()
            print('1')
        elif count == 1:
            self.t.pendown()
            print('2')
        else:
            count = 0

m = Main()
