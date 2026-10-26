from tkinter import *
import math

root = Tk()
root.configure(background="black")
root.geometry("400x100")
root.title("SWR Meter")

def callback():
    rho = math.sqrt(float(reflection.get()) / float(forward.get()))
    SWR = round((1 + rho) / (1 - rho), 1)

frm1 = Frame(root, background="black")
frm1.pack(side=TOP, fill = X)
label = Label(frm1, text="Enter forward power in watts:", bg="black", fg="white", font="none 12")
label.pack(side=LEFT, fill=X)
forward = Entry(frm1, text="Forward power", bg="white", fg="black", font="none 12")
forward.pack(side=RIGHT, fill=X)

forward.focus_set()

frm2 = Frame(root, background="black")
frm2.pack(side=TOP, fill = X)
label1 = Label(frm2, text="Enter reflected power in watts:", bg="black", fg="white", font="none 12")
label1.pack(side=LEFT, fill=X)
reflection = Entry(frm2, text="Reflected power", bg="white", fg="black", font="none 12")
reflection.pack(side=RIGHT, fill=X)

frm3 = Frame(root, background="black")
frm3.pack(side=TOP, fill = X)
calculate = Button(frm3, text="Get SWR", bg="black", fg="white", command=callback, font="none 12")
calculate.pack(side=TOP, fill=X)

'''frm4 = Frame(root, background="black")
frm4.pack(side=TOP, fill = X)
global SWR
if SWR==1:
    swr = Label(frm4, SWR, bg="black", fg="green")
    swr.pack(side=TOP, fill=X)
    swr2 = Label(frm4, text="That is a very good reading", bg="black", fg="white")
    swr2.pack(side=TOP, fill=X)
elif SWR>1 and SWR<3:
    swr3 = Label(frm4, SWR, bg="black", fg="yellow")
    swr3.pack(side=TOP, fill=X)
    swr4 = Label(frm4, text="That is an okay reading", bg="black", fg="white")
    swr4.pack(side=TOP, fill=X)
else SWR>3:
    swr5 = Label(frm4, SWR, bg="black", fg="red")
    swr5.pack(side=TOP, fill=X)
    swr6 = Label(frm4, text="That is a very bad reading", bg="black", fg="white")
    swr6.pack(side=TOP, fill=X)
    '''
root.mainloop()




#print(root.winfo_x())

