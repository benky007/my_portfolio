import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.geometry('500x500')

style = ttk.Style()
style.theme_create("dark", settings={
    "TNotebook": {
        "configure": {
            "background": "blue", # darkest grey
            "tabmargins": [2, 5, 0, 0]
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": "green", # darker grey
            "padding": [10, 2],
            "font": "white"
        },
        "map": {
            "background": [("selected", "purple")], # lighter grey
            "expand": [("selected", [1, 1, 1, 0])]
        }
    }
})
style.theme_use("dark")
notebook = ttk.Notebook(root, width=250, height=250)
notebook.place(x=0, y=0)

current_project = tkinter.Frame(notebook, background="yellow", width=250, height=250)
current_project.place(x=0, y=0)
notebook.add(current_project, text="weird")

root.mainloop()
