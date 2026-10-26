import tkinter

root = tkinter.Tk()
root.geometry('500x500')
root.configure(bg='black')

canvas = tkinter.Canvas(root, width=400, height=400, bg="blue")
canvas.place(x=50, y=50)

lab = tkinter.Label(canvas, text="Label")
lab.place(x=50, y=50)

root.mainloop()