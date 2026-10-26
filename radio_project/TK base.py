from tkinter import *
from tkinter import ttk, messagebox

window = Tk()
window.configure(background="white")
window.geometry('800x500+350+300')
window.title("Logger")

frame_main = Frame(window, background="grey")
frame_main.pack(expand=True)
frame_area = Frame(frame_main, background="black")
frame_area.pack(expand=True)
title1 = Frame(frame_area, height=100, width=800, background="blue")
title1.pack(side=TOP, fill=BOTH)
top = Frame(frame_area, height=200, width=800, background="green")
top.pack(side=TOP, fill=BOTH)
bottom = Frame(frame_area, height=200, width=800, background="green")
bottom.pack(side=BOTTOM, fill=BOTH)
top_left = Frame(top, height=200, width=400, background="white")
top_left.pack(side=LEFT, fill=BOTH)
top_right = Frame(top, height=200, width=400, background="white")
top_right.pack(side=RIGHT, fill=BOTH)
Log = Frame(top_left, height=200, width=400)
Log.pack(fill=BOTH)
search = Frame(top_right, height=200, width=400)
search.pack(fill=BOTH)
data = Frame(bottom, height=200, width=400)
data.pack(fill=BOTH)

test = Label(title1, text="Ben's logger")
test.pack()
tabControl = ttk.Notebook(Log)


def view_selected(choice):
    if choice == 1:
        output = "QRZ"

    elif choice == 2:
        output = "Lotw"

    elif choice == 3:
        output = "eQSL"

    elif choice == 4:
        output = "Clublog"
    else:
        output = "Invalid selection"
        print(choice)

    return messagebox.showinfo('PythonGuides', f'You Selected {output}.')


def ok():
    pass


def cancel():
    pass


def QRZ():
    # viewSelected(var)
    pass


def Lotw():
    # viewSelected(var)
    pass


def eQSL():
    # viewSelected(var)
    pass


def Club_log():
    # viewSelected(var)
    pass


def log(tab_control):
    var = 0
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='My info')
    tab_control.add(tab2, text='Qsl info')
    tab_control.pack(expand=1, fill="both")
    # my_data = ttk.Label(tab1, text="My Data")
    power = ttk.Label(tab1, text="Input Your power")
    power_entry = ttk.Entry(tab1)
    QTH = ttk.Label(tab1, text="Input Your QTH")
    QTH_entry = ttk.Entry(tab1)
    my_callsign = ttk.Label(tab1, text="My Call")
    my_callsign_entry = ttk.Entry(tab1)
    my_locator = ttk.Label(tab1, text="My Locator")
    my_locator_entry = ttk.Entry(tab1)
    CQ = ttk.Label(tab1, text="Input Your CQ zone")
    CQ_entry = ttk.Entry(tab1)
    ITU = ttk.Label(tab1, text="Input Your ITU zone")
    ITU_entry = ttk.Entry(tab1)
    Ok = ttk.Button(tab1, text="Ok", command=ok)
    Cancel = ttk.Button(tab1, text="Cancel", command=cancel)
    QSL_label = ttk.Label(tab2, text="click the systems that you QSL with")
    QSL_qrz = ttk.Radiobutton(tab2, text="QRZ.com", variable=var, value=1, command=QRZ)
    QSL_Logbook_of_the_world = ttk.Radiobutton(tab2, text="Lotw.com", variable=var, value=2, command=Lotw)
    QSL_eQSL = ttk.Radiobutton(tab2, text="eQSL.com", variable=var, value=3, command=eQSL)
    QSL_Clublog = ttk.Radiobutton(tab2, text="Clublog.com", variable=var, value=4, command=Club_log)

    # my_data.pack(side=TOP)
    power.pack(side=TOP)
    power_entry.pack(side=TOP)
    QTH.pack(side=TOP)
    QTH_entry.pack(side=TOP)
    my_callsign.pack(side=TOP)
    my_callsign_entry.pack(side=TOP)
    my_locator.pack(side=TOP)
    my_locator_entry.pack(side=TOP)
    CQ.pack(side=TOP)
    CQ_entry.pack(side=TOP)
    ITU.pack(side=TOP)
    ITU_entry.pack(side=TOP)
    Ok.pack(side=LEFT)
    Cancel.pack(side=RIGHT)
    QSL_label.pack(side=TOP)
    QSL_qrz.pack(side=TOP)
    QSL_Logbook_of_the_world.pack(side=TOP)
    QSL_eQSL.pack(side=TOP)
    QSL_Clublog.pack(side=TOP)


log(tabControl)
window.mainloop()
