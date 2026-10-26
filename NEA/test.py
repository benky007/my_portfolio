import tkinter

root = tkinter.Tk()
root.geometry('200x200')
root.title('Project 1')

window = tkinter.Canvas(root, width=200, height=200, background="white")
window.place(x=0, y=0)

temp = tkinter.Label(window, width=20, height=1, anchor="center", bg="green", bd=0, cursor="arrow", font=("Helvetica", 20, "normal"), fg="black", justify="left", padx=0, pady=0, relief="flat", text="WOOOOO", underline=-1, wraplength=0)
temp.place(x=5, y=50)

root.mainloop()
