from tkinter import *

root = Tk()
root.configure(background="black")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.geometry("400x100")
root.title("SWR Meter")

def callback():
    '''
    fward = root.entry.get()
    root.destroy()
    ref = root.entry1.get()
    root.destroy
    '''
    pass

frame = Frame(root, background="black")
frame.grid(row=0, column=0)
label = Label(frame, text="Enter forward power in watts:", bg="black", fg="white", font="none 12")
label.grid(row=1, column=0, sticky=N+E+S+W)
entry = Entry(frame, text="Forward power", bg="white", fg="black", font="none 12")
entry.grid(row=1, column=1, sticky=N+E+S+W)
label1 = Label(frame, text="Enter reflected power in watts:", bg="black", fg="white", font="none 12")
label1.grid(row=2, column=0, sticky=N+E+S+W)
entry1 = Entry(frame, text="Reflected power", bg="white", fg="black", font="none 12")
entry1.grid(row=2, column=1, sticky=N+E+S+W)
submit = Button(frame, text="Get SWR", bg="black", fg="white", command=callback, font="none 12")
submit.grid(row=3, column=0, sticky=N+E+S+W)
root.mainloop()

#print(root.winfo_x())

