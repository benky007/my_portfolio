import json
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

SETUP = "setup.json"


class opening:
    def __init__(self, master):
        self.filename = None
        self.master = master
        self.master.geometry("500x250")
        self.master.title("Initial Startup")
        self.master.resizable(False, False)
        with open(SETUP) as file:
            data = json.load(file)
            current_theme = data["themes"]["current"]
        colours = data["themes"][current_theme]
        self.background = [colours["clr4"], colours["clrA"]]
        self.foreground = [colours["clr3"], colours["clr1"], colours["clr2"]]
        self.border = colours["light_border"]
        self.test = colours["test"]
        self.master.config(bg=self.background[0])
        left = tkinter.Frame(self.master, bg=self.background[0], width=250, highlightbackground=self.border,
                             highlightthickness=0)
        left.pack(side=tkinter.LEFT, fill="y", expand=True, anchor=tkinter.W)
        left.pack_propagate(False)
        right = tkinter.Frame(self.master, bg=self.background[0], width=250, highlightbackground=self.border,
                              highlightthickness=1)
        right.pack(side=tkinter.RIGHT, fill="y", expand=True, anchor=tkinter.NW)
        right.pack_propagate(False)

        description_frame = tkinter.Frame(right, bg=self.background[0], height=130)
        description_frame.pack(side=tkinter.TOP, fill="x", expand=True, anchor=tkinter.N)
        description_frame.pack_propagate(False)
        options = tkinter.Frame(right, bg=self.background[0], height=120)
        options.pack(side=tkinter.BOTTOM, fill="x", expand=True, anchor=tkinter.S)
        options.pack_propagate(False)

        title = tkinter.Label(left, text="GUI\nBuilder", font=("Helvetica", 40), bg=self.background[1],
                              fg=self.foreground[2])
        title.pack(fill="x", expand=True)
        description1 = tkinter.Label(left, text="This is a tool to help\n"
                                                "you build the graphical user\n"
                                                "interfaces of your dream\n"
                                                "and never run out of\n"
                                                "creativity",
                                     font=("Helvetica", 15), bg=self.background[0], fg=self.foreground[0])
        description1.pack(fill="x", expand=True)

        description2 = tkinter.Label(description_frame, text="Fill in these details\n"
                                                             "to begin the process of\n"
                                                             "creating your perfect\n"
                                                             "working environment",
                                     font=("Helvetica", 15), bg=self.background[0], fg=self.foreground[1])
        description2.pack(fill="x", expand=True)
        description3 = tkinter.Label(description_frame, text="These details can\n"
                                                             "always be changed later in the settings",
                                     font=("Helvetica", 10), bg=self.background[0], fg=self.foreground[0])
        description3.pack(fill="x", expand=True)

        self.language = tkinter.StringVar()
        language_statement = tkinter.Label(options, text="Choose a language from the options:", bg=self.background[0],
                                           fg=self.foreground[2], anchor=tkinter.W)
        language_statement.pack(fill="x", expand=True, anchor=tkinter.W)
        language_choice = ttk.Combobox(options, textvariable=self.language, state="readonly", values=["English"],
                                       width=20)
        language_choice.pack(expand=True)

        path_statement = tkinter.Label(options, text="Choose a location to store project files:", bg=self.background[0],
                                       fg=self.foreground[2], anchor=tkinter.W)
        path_statement.pack(fill="x", expand=True, anchor=tkinter.W)

        path_entry_frame = tkinter.Frame(options, bg=self.test, height=20, width=147)
        path_entry_frame.pack(expand=True)
        path_entry_frame.pack_propagate(False)
        self.path_choice = ttk.Entry(path_entry_frame, width=16)
        self.path_choice.pack(side=tkinter.LEFT)
        file_explorer = tkinter.Button(path_entry_frame, text="Browse", command=lambda: self.browseFiles())
        file_explorer.pack(side=tkinter.LEFT)

        apply_button_frame = tkinter.Frame(options, bg=self.background[0], height=30, borderwidth=5)
        apply_button_frame.pack(fill="x", expand=True)
        apply_button_frame.pack_propagate(False)
        apply_button = tkinter.Button(apply_button_frame, text="Apply", command=lambda: self.apply())
        apply_button.pack(fill="x", expand=True)

    def browseFiles(self):
        self.filename = filedialog.askdirectory(initialdir="/", title="Select a File")
        self.path_choice.delete(0, tkinter.END)
        self.path_choice.insert(0, self.filename)

    def apply(self):
        if self.path_choice.get() is None:
            path = os.path.dirname(os.path.abspath(__file__))
        else:
            if os.path.isdir(self.path_choice.get()):
                path = self.path_choice.get()
            else:
                path = None
                messagebox.showerror('Path Error', 'Error: Path does not exist')
        if self.language.get() == "":
            messagebox.showerror('Language Error', 'Error: Enter a language')
        if path is not None and self.language.get() != "":
            with open(SETUP) as file:
                data = json.load(file)
            data["completed"] = 1
            data["lang"] = self.language.get()
            data["path"] = path
            with open(SETUP, "w") as file:
                json.dump(data, file)
            self.master.destroy()


if __name__ == '__main__':
    root = tkinter.Tk()

    with open(SETUP, "r") as f:
        initial_setup = json.load(f)
        if initial_setup["completed"] == 0:
            opening(root)
        else:
            pass

    root.mainloop()
