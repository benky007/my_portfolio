from tkinter import *

root = Tk()
root.configure(background="black")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
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
frame.pack()
label = Label(frame, text="Enter forward power in watts:", bg="black", fg="white", font="none 12")
label.pack(side=TOP, expand=1, fill=Y)
entry = Entry(frame, text="Forward power", bg="white", fg="black", font="none 12")
entry.pack(side=RIGHT, expand=1, fill=X)
label1 = Label(frame, text="Enter reflected power in watts:", bg="black", fg="white", font="none 12")
label1.pack(side=TOP, expand=1, fill=Y)
entry1 = Entry(frame, text="Reflected power", bg="white", fg="black", font="none 12")
entry1.pack(side=RIGHT, expand=1, fill=X)
submit = Button(frame, text="Get SWR", bg="black", fg="white", command=callback, font="none 12")
submit.pack(side=BOTTOM, expand=1, fill=X)
root.mainloop()

#print(root.winfo_x())

