import tkinter
from tkinter import ttk
import json
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
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
            self.master.update()


class app:  # this is the main class of the program
    def __init__(self, master, setup):  # this will initialise this main window
        self.click = None
        self.dimensions = None
        self.coords = None
        self.moving = None
        self.new_width = None
        self.new_height = None
        self.open_projects = []
        self.toolbar2 = None
        self.main_canvas = None
        self.toolbar1 = None
        self.master = master
        self.master.title("NEA")
        self.data = setup
        colours = self.data["themes"][self.data["themes"]["current"]]
        self.background = [colours["clr4"], colours["clrA"]]
        self.foreground = [colours["clr3"], colours["clr1"], colours["clr2"]]
        self.border = colours["light_border"]
        self.test = colours["test"]
        self.menu()

    def initiate_objects(self, tool_bar1, main_canvas, tool_bar2):
        self.toolbar1 = tool_bar1
        self.main_canvas = main_canvas
        self.toolbar2 = tool_bar2

    def find_tool(self, command, checkTool):
        if checkTool in self.toolbar1.tools:
            if command == "show":
                self.toolbar1.show(checkTool)
            else:
                self.toolbar1.hide(checkTool)
        elif checkTool in self.toolbar2.tools:
            if command == "show":
                self.toolbar2.show(checkTool)
            else:
                self.toolbar2.hide(checkTool)
        else:
            if command == "show":
                if checkTool in self.data["previous"]["toolbars"]["left"][3]:
                    self.toolbar1.show(checkTool)
                elif checkTool in self.data["previous"]["toolbars"]["right"][3]:
                    self.toolbar2.show(checkTool)
                else:
                    self.toolbar1.show(checkTool)
            else:
                pass

    def menu(self):  # this will initialise the menu at the top
        menu = tkinter.Menu(self.master, tearoff=0)

        fileMenu = tkinter.Menu(menu, tearoff=0)
        fileMenu.add_command(label="New", command=lambda: self.new())
        fileMenu.add_command(label="Open", command=lambda: self.open())
        fileMenu.add_command(label="Save", command="")
        fileMenu.add_command(label="Export", command="")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=lambda: self.exit())
        menu.add_cascade(label="File", menu=fileMenu)

        viewMenu = tkinter.Menu(menu, tearoff=0)
        widgetMenu = tkinter.Menu(viewMenu, tearoff=0)
        widgetMenu.add_command(label="Show", command=lambda: self.find_tool("show", "Widget"))
        widgetMenu.add_command(label="Hide", command=lambda: self.find_tool("hide", "Widget"))
        viewMenu.add_cascade(label="Widget Tool", menu=widgetMenu)
        customisationMenu = tkinter.Menu(viewMenu, tearoff=0)
        customisationMenu.add_command(label="Show", command=lambda: self.find_tool("show", "Customisation"))
        customisationMenu.add_command(label="Hide", command=lambda: self.find_tool("hide", "Customisation"))
        viewMenu.add_cascade(label="Customisation Tool", menu=customisationMenu)
        layoutMenu = tkinter.Menu(viewMenu, tearoff=0)
        layoutMenu.add_command(label="Show", command=lambda: self.find_tool("show", "Layout"))
        layoutMenu.add_command(label="Hide", command=lambda: self.find_tool("hide", "Layout"))
        viewMenu.add_cascade(label="Layout Tool", menu=layoutMenu)
        creatorMenu = tkinter.Menu(viewMenu, tearoff=0)
        creatorMenu.add_command(label="Show", command="")
        creatorMenu.add_command(label="Hide", command="")
        # viewMenu.add_cascade(label="Creator Tool", menu=creatorMenu, state="disabled")
        IDEMenu = tkinter.Menu(viewMenu, tearoff=0)
        IDEMenu.add_command(label="Show", command="")
        IDEMenu.add_command(label="Hide", command="")
        # viewMenu.add_cascade(label="IDE Tool", menu=IDEMenu, state="disabled")
        menu.add_cascade(label="View", menu=viewMenu)

        settingsMenu = tkinter.Menu(menu, tearoff=0)
        layoutManagerMenu = tkinter.Menu(settingsMenu, tearoff=0)
        leftBarMenu = tkinter.Menu(layoutManagerMenu, tearoff=0)
        leftBarMenu.add_command(label="Show", command="")
        leftBarMenu.add_command(label="Hide", command="")
        leftBarMenu.add_command(label="Tearoff", command="")
        layoutManagerMenu.add_cascade(label="Left Tool Bar", menu=leftBarMenu, state="disabled")
        rightBarMenu = tkinter.Menu(layoutManagerMenu, tearoff=0)
        rightBarMenu.add_command(label="Show", command="")
        rightBarMenu.add_command(label="Hide", command="")
        rightBarMenu.add_command(label="Tearoff", command="")
        layoutManagerMenu.add_cascade(label="Right Tool Bar", menu=rightBarMenu, state="disabled")
        settingsMenu.add_cascade(label="Layout Manager", menu=layoutManagerMenu)
        applicationStyleMenu = tkinter.Menu(settingsMenu, tearoff=0)
        for theme in list(self.data["themes"])[:-1]:
            applicationStyleMenu.add_command(label=theme, command="")
        applicationStyleMenu.add_command(label="Import", command="")
        settingsMenu.add_cascade(label="Application Style", menu=applicationStyleMenu)
        menu.add_cascade(label="Settings", menu=settingsMenu)

        helpMenu = tkinter.Menu(menu, tearoff=0)
        guides = tkinter.Menu(helpMenu, tearoff=0)
        guides.add_command(label="Guide 1", command="")
        guides.add_command(label="Guide 2", command="")
        guides.add_command(label="Guide 3", command="")
        helpMenu.add_cascade(label="Guides", menu=guides, state="disabled")
        menu.add_cascade(label="Help", menu=helpMenu)

        aboutMenu = tkinter.Menu(menu, tearoff=0)
        aboutMenu.add_command(label="About", command="")
        aboutMenu.add_command(label="Contact Us", command="")
        menu.add_cascade(label="About", menu=aboutMenu)

        self.master.config(menu=menu)

    def new(self):  # this will create a new GUI that will be a blank template
        try:
            path = self.new_project()[:-4]
            os.mkdir(path)
            self.open_projects.append(project(path, (float(self.new_width), float(self.new_height))))
            self.open_projects[-1].save()
            self.main_canvas.load(self.open_projects[-1].data)
            widgets = self.main_canvas.Widgets
            for widget in widgets:
                widget.bind("<Button-1>", lambda event: self.select(event, widget))
        except TypeError:
            pass

    def new_project(self):
        filename = filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension=".txt",
                                                filetypes=[('GUI files', '*.GUI')], initialdir=self.data["path"])
        if filename != "":
            dimensions = tkinter.Toplevel(self.master)
            dimensions.resizable(width=False, height=False)
            dimensions.config(bg=self.background[0])
            dimensions.geometry("180x202")
            frame1 = tkinter.Frame(dimensions, width=160, height=192, bg=self.background[0])
            frame1.place(x=10, y=10)
            frame2 = tkinter.Frame(frame1, width=150, height=54, bg=self.background[1], highlightcolor="Black",
                                   highlightthickness=1)
            frame2.place(x=5, y=5)
            frame3 = tkinter.Frame(frame1, width=150, height=54, bg=self.background[1], highlightcolor="Black",
                                   highlightthickness=1)
            frame3.place(x=5, y=65)
            frame4 = tkinter.Frame(frame1, width=150, height=54, bg=self.background[0], highlightcolor="Black",
                                   highlightthickness=0)
            frame4.place(x=5, y=125)
            statement1 = tkinter.Label(frame2, text="Enter GUI width(px):", bg=self.background[1],
                                       fg=self.foreground[0])
            statement1.place(x=2, y=2)
            width_entry = tkinter.Entry(frame2)
            width_entry.place(x=2, y=30)
            statement2 = tkinter.Label(frame3, text="Enter GUI height(px):", bg=self.background[1],
                                       fg=self.foreground[0])
            statement2.place(x=2, y=2)
            height_entry = tkinter.Entry(frame3)
            height_entry.place(x=2, y=30)
            create = tkinter.Button(frame4, text="Create", width=16, height=1,
                                    command=lambda: self.get_entry(dimensions, (width_entry.get(), height_entry.get())))
            create.place(x=12, y=22)
            dimensions.transient(self.master)
            dimensions.grab_set()
            self.master.wait_window(dimensions)
            return filename
        else:
            return None

    def get_entry(self, top, size):
        self.new_width, self.new_height = size
        self.kill_top(top, size)

    @staticmethod
    def kill_top(top, size):
        width_error = False
        height_error = False
        width_empty_error = False
        height_empty_error = False
        if size[0] == "":
            width_empty_error = True
        if size[1] == "":
            height_empty_error = True
        try:
            x = float(size[0])
            x += 1
        except (TypeError, ValueError):
            width_error = True
        try:
            y = float(size[1])
            y += 1
        except (TypeError, ValueError):
            height_error = True
        if width_empty_error or height_empty_error:
            messagebox.showerror(title="Entry error",
                                 message="Error: All fields must be filled")
        elif width_error and height_error:
            messagebox.showerror(title="Entry error",
                                 message="Error: Width and height must be floating point or integer values")
        elif width_error:
            messagebox.showerror(title="Entry error",
                                 message="Error: Width must be a floating point or integer value")
        elif height_error:
            messagebox.showerror(title="Entry error",
                                 message="Error: Height must be a floating point or integer value")
        else:
            top.destroy()
            top.update()

    def edit(self, event, new, focussed):
        pass

    def open(self):  # this will open a file explorer to choose a directory in the correct format to load
        dirname = filedialog.askdirectory(initialdir=self.data["path"], title="Select Project Directory")
        if dirname != "":
            self.open_projects.append(project(dirname, (0, 0)))
            self.open_projects[-1].read()
            self.main_canvas.load(self.open_projects[-1].data)
            for i in range(len(self.open_projects[-1].data["Widgets"])):
                new = self.main_canvas.add(self.open_projects[-1].data["Widgets"][i])
                new.bind("<Button-1>", lambda event: self.select(event, event.widget))
        else:
            pass

    def select(self, event, name):
        if isinstance(name, int):
            self.main_canvas.select_id(name)
        else:
            self.main_canvas.select_object(name)
        try:
            select1 = self.toolbar1.select(self.main_canvas.selected["Type"],
                                           self.main_canvas.selected["attr"])
            select1[0].bind("<Button-1>", lambda event: self.edit(event, select1[1], self.main_canvas.selected))
        except AttributeError:
            try:
                select2 = self.toolbar2.select(self.main_canvas.selected["Type"],
                                               self.main_canvas.selected["attr"])
                select2[0].bind("<Button-1>", lambda event: self.edit(event, select2[1], self.main_canvas.selected))
            except AttributeError:
                pass

    def exit(self):
        try:
            self.open_projects[-1].save()
            self.master.destroy()
        except IndexError:
            self.master.destroy()


class editing:  # this is the class that runs and handles the editing part of the screen
    def __init__(self, master, setup):  # this will initialise the editing suite
        self.window = None
        self.focussed = None
        self.ratio = None
        self._data = None
        self.widgets = []
        self.coords = []
        self.master = master
        self.setup = setup
        self.colours = self.setup["themes"][self.setup["themes"]["current"]]
        self.style = ttk.Style()
        self.style.theme_create("dark", settings={
            "TNotebook": {
                "configure": {
                    "background": self.colours["clr4"],
                    "tabmargins": [2, 5, 0, 0]
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "background": self.colours["clr9"],
                    "padding": [10, 2],
                    "foreground": self.colours["clr1"]
                },
                "map": {
                    "background": [("selected", self.colours["clr8"])],
                    "expand": [("selected", [1, 1, 1, 0])]
                }
            }
        })
        self.style.theme_use("dark")
        self.notebook = ttk.Notebook(self.master, width=650, height=650)
        self.notebook.place(x=0, y=0)

    def load(self, data):
        self._data = data
        current_project = tkinter.Frame(self.notebook, background=self.colours["clr8"], width=650, height=650)
        current_project.place(x=0, y=0)
        self.notebook.add(current_project, text=self._data["root"]["title"])

        if self._data["root"]["width"] > self._data["root"]["height"]:
            self.ratio = 500 / self._data["root"]["width"]
        elif self._data["root"]["width"] < self._data["root"]["height"]:
            self.ratio = 500 / self._data["root"]["height"]
        else:
            self.ratio = 500 / self._data["root"]["width"]

        self.window = tkinter.Canvas(current_project, width=self.ratio * self._data["root"]["width"],
                                     height=self.ratio * self._data["root"]["height"], bg=self._data["root"]["bg"])
        self.window.place(x=75, y=75)

    def add(self, widget):
        # print(widget)
        if widget["Type"] == "Frame":
            temp = tkinter.Frame(self.window, width=widget["attr"]["width"], height=widget["attr"]["height"],
                                 bd=widget["attr"]["bd"], relief=widget["attr"]["relief"],
                                 cursor=widget["attr"]["cursor"], highlightthickness=widget["attr"]["ht"],
                                 highlightcolor=widget["attr"]["hc"], highlightbackground=widget["attr"]["hb"],
                                 bg=widget["attr"]["bg"])
            temp.place(x=self.ratio * widget["attr"]["x"], y=self.ratio * widget["attr"]["y"])
            self.widgets.append(temp)
        elif widget["Type"] == "Button":
            temp = tkinter.Button(self.window, width=widget["attr"]["width"], height=widget["attr"]["height"],
                                  activebackground=widget["attr"]["ab"], activeforeground=widget["attr"]["af"],
                                  bd=widget["attr"]["bd"], bg=widget["attr"]["bg"], fg=widget["attr"]["fg"],
                                  font=font.Font(family=widget["attr"]["font"][0],
                                                 size=int(self.ratio * widget["attr"]["font"][1]),
                                                 weight=widget["attr"]["font"][2]),
                                  highlightcolor=widget["attr"]["hc"],
                                  justify=widget["attr"]["justify"], padx=widget["attr"]["padx"],
                                  pady=widget["attr"]["pady"], relief=widget["attr"]["relief"],
                                  state="disabled", underline=widget["attr"]["uline"],
                                  wraplength=widget["attr"]["wl"], highlightbackground=widget["attr"]["hb"],
                                  highlightthickness=widget["attr"]["ht"], text=widget["attr"]["text"])
            temp.place(x=self.ratio * widget["attr"]["x"], y=self.ratio * widget["attr"]["y"])
            self.widgets.append(temp)
        elif widget["Type"] == "Label":
            temp = tkinter.Label(self.window, width=widget["attr"]["width"], height=widget["attr"]["height"],
                                 anchor=widget["attr"]["anchor"], bg=widget["attr"]["bg"], bd=widget["attr"]["bd"],
                                 cursor=widget["attr"]["cursor"], font=font.Font(family=widget["attr"]["font"][0],
                                                                                 size=int(self.ratio *
                                                                                          widget["attr"]["font"][
                                                                                              1]),
                                                                                 weight=widget["attr"]["font"][2]),
                                 fg=widget["attr"]["fg"],
                                 justify=widget["attr"]["justify"], padx=widget["attr"]["padx"],
                                 pady=widget["attr"]["pady"], relief=widget["attr"]["relief"],
                                 text=widget["attr"]["text"],
                                 underline=widget["attr"]["uline"],
                                 wraplength=widget["attr"]["wl"], highlightbackground=widget["attr"]["hb"],
                                 highlightthickness=widget["attr"]["ht"])
            temp.place(x=self.ratio * widget["attr"]["x"], y=self.ratio * widget["attr"]["y"])
            self.widgets.append(temp)
        elif widget["Type"] == "Entry":
            temp = tkinter.Entry(self.window, width=widget["attr"]["width"], bg=widget["attr"]["bg"],
                                 bd=widget["attr"]["bd"],
                                 cursor=widget["attr"]["cursor"], font=font.Font(family=widget["attr"]["font"][0],
                                                                                 size=int(self.ratio *
                                                                                          widget["attr"]["font"][
                                                                                              1]),
                                                                                 weight=widget["attr"]["font"][2]),
                                 show=widget["attr"]["show"],
                                 exportselection=widget["attr"]["es"], fg=widget["attr"]["fg"],
                                 highlightcolor=widget["attr"]["hc"], justify=widget["attr"]["justify"],
                                 relief=widget["attr"]["relief"], selectbackground=widget["attr"]["sb"],
                                 selectborderwidth=widget["attr"]["sbw"], selectforeground=widget["attr"]["sf"],
                                 state="disabled", highlightbackground=widget["attr"]["hb"],
                                 highlightthickness=widget["attr"]["ht"])
            temp.place(x=self.ratio * widget["attr"]["x"], y=self.ratio * widget["attr"]["y"])
            self.widgets.append(temp)
        elif widget["Type"] == "Checkbutton":
            temp = tkinter.Checkbutton(self.window, width=widget["attr"]["width"], height=widget["attr"]["height"],
                                       activebackground=widget["attr"]["ab"], activeforeground=widget["attr"]["af"],
                                       bg=widget["attr"]["bg"], bd=widget["attr"]["bd"],
                                       cursor=widget["attr"]["cursor"],
                                       disabledforeground=widget["attr"]["df"],
                                       font=font.Font(family=widget["attr"]["font"][0],
                                                      size=int(self.ratio * widget["attr"]["font"][1]),
                                                      weight=widget["attr"]["font"][2]),
                                       fg=widget["attr"]["fg"], highlightcolor=widget["attr"]["hc"],
                                       justify=widget["attr"]["justify"], offvalue=widget["attr"]["ofv"],
                                       onvalue=widget["attr"]["onv"], padx=widget["attr"]["padx"],
                                       pady=widget["attr"]["pady"], relief=widget["attr"]["relief"],
                                       selectcolor=widget["attr"]["sc"], state="disabled",
                                       underline=widget["attr"]["uline"], text=widget["attr"]["text"],
                                       wraplength=widget["attr"]["wl"], highlightbackground=widget["attr"]["hb"],
                                       highlightthickness=widget["attr"]["ht"])
            temp.place(x=self.ratio * widget["attr"]["x"], y=self.ratio * widget["attr"]["y"])
            self.widgets.append(temp)
        elif widget["Type"] == "Radiobutton":
            temp = tkinter.Radiobutton(self.window, width=widget["attr"]["width"], height=widget["attr"]["height"],
                                       activebackground=widget["attr"]["ab"], activeforeground=widget["attr"]["af"],
                                       anchor=widget["attr"]["anchor"], bg=widget["attr"]["bg"],
                                       borderwidth=widget["attr"]["bd"], cursor=widget["attr"]["cursor"],
                                       font=font.Font(family=widget["attr"]["font"][0],
                                                      size=int(self.ratio * widget["attr"]["font"][1]),
                                                      weight=widget["attr"]["font"][2]), fg=widget["attr"]["fg"],
                                       highlightcolor=widget["attr"]["hc"],
                                       highlightbackground=widget["attr"]["hb"],
                                       highlightthickness=widget["attr"]["ht"],
                                       justify=widget["attr"]["justify"], padx=widget["attr"]["padx"],
                                       pady=widget["attr"]["pady"], relief=widget["attr"]["relief"],
                                       selectcolor=widget["attr"]["sc"], state="disabled",
                                       text=widget["attr"]["text"], underline=widget["attr"]["uline"],
                                       value=widget["attr"]["value"],
                                       wraplength=widget["attr"]["wl"])
            temp.place(x=self.ratio * widget["attr"]["x"], y=self.ratio * widget["attr"]["y"])
            self.widgets.append(temp)
        else:
            temp = None
        return temp


class project:
    def __init__(self, name, dimensions):
        self._path = name
        self.title = self._path.split("/")[-1]
        self.dimensions = dimensions
        self.initial = {
            "root": {"bg": "white", "width": self.dimensions[0], "height": self.dimensions[1], "title": self.title},
            "Widgets": []}
        self.defaults = {"Frame": {"x": 0, "y": 0, "width": 100, "height": 40, "bd": 0, "relief": "flat",
                                   "cursor": "arrow", "ht": 1, "hc": "black", "hb": "black", "bg": "white"},
                         "Button": {"x": 0, "y": 0, "width": 13, "height": 2, "ab": "white", "af": "black", "bd": 0,
                                    "bg": "white", "fg": "black", "font": ["Helvetica", 10, "normal"], "hc": "black",
                                    "justify": "left", "padx": 0, "pady": 0, "relief": "flat", "state": "normal",
                                    "uline": -1, "wl": 0, "hb": "black", "ht": 1, "text": "Button"},
                         "Label": {"x": 0, "y": 0, "width": 13, "height": 2, "anchor": "center", "bg": "white",
                                   "bd": 0, "hb": "black", "ht": 1, "cursor": "arrow",
                                   "font": ["Helvetica", 10, "normal"], "fg": "black",
                                   "justify": "left", "padx": 0, "pady": 0, "relief": "flat", "text": "Label",
                                   "uline": -1, "wl": 0},
                         "Entry": {"x": 0, "y": 0, "width": 13, "bg": "white", "bd": 0, "cursor": "arrow",
                                   "font": ["Helvetica", 10, "normal"], "show": "", "es": 0, "fg": "black",
                                   "hc": "black", "hb": "black", "ht": 1,
                                   "justify": "left", "relief": "flat", "sb": "white", "sbw": 0, "sf": "black",
                                   "state": "normal"},
                         "Checkbutton": {"x": 0, "y": 0, "width": 13, "height": 2, "ab": "white",
                                         "af": "black", "bg": "white", "bd": 0, "cursor": "arrow",
                                         "df": "gray", "font": ["Helvetica", 10, "normal"], "fg": "black",
                                         "hc": "black",
                                         "justify": "left", "hb": "black", "ht": 1,
                                         "ofv": 0, "onv": 1, "padx": 0, "pady": 0, "relief": "flat", "sc": "black",
                                         "state": "normal", "uline": -1, "text": "Checkbutton", "wl": 0},
                         "Radiobutton": {"x": 0, "y": 0, "width": 13, "height": 2, "ab": "white", "af": "black",
                                         "anchor": "center", "bg": "white", "bd": 0, "cursor": "arrow",
                                         "font": ["Helvetica", 10, "normal"], "fg": "black", "hc": "black",
                                         "hb": "black", "ht": 1,
                                         "justify": "left", "padx": 0, "pady": 0, "relief": "flat", "sc": "black",
                                         "state": "normal", "text": "Radiobutton", "uline": -1, "value": 1, "wl": 0}}

        # format will be like above but for widgets it will be {"root": {"bg": "white", "width": self.dimensions[0],
        # "height": self.dimensions[1], "title": self.title}, "Widgets": []}
        # "Widgets": [{"ID": 0, "Type": "Frame",
        # "Attributes": {"x": x, "y": y, "width": width, "height": height, "font": FONT(in tuple), "Bg": Bg,
        # "Bd": Bd, "Cursor": cursor, "highlightbackground": hb, "highlightthickness": ht, "highlightcolor": hc,
        # "relief": relief, "ab": 0, "af": 0, "fg": 0, "justify": 0, "padx": 0, "pady": 0, "state": 0, "uline": 0,
        # "wl": 0, "anchor": 0, "text": 0, "es": 0, "sb": 0, "sbw": 0, "sf": 0, "show": 0, "df": 0, "ofv": 0,
        # "onv": 0, "sc": 0, "value": 0}}, ]

    def add_widget(self, type1, x, y):
        if len(self.data["Widgets"]) > 0:
            self.data["Widgets"].append(
                {"ID": self.data["Widgets"][-1]["ID"] + 1, "Type": type1, "attr": self.defaults[type1]})
        else:
            self.data["Widgets"].append({"ID": 0, "Type": type1, "attr": self.defaults[type1]})
        self.data["Widgets"][-1]["attr"].update({"x": x, "y": y})

    @property
    def data(self):
        return self.initial

    @data.setter
    def data(self, value):
        self.initial = value

    @property
    def path(self):
        return self._path

    def save(self):
        with open(f"{self._path}/{self.title}.json", "w") as file:
            json.dump(self.data, file, indent=4)

    def read(self):
        with open(f"{self._path}/{self.title}.json", "r") as file:
            self.data = json.load(file)


class toolBar:  # this is a class that handles the frames on the screen in which the tools are kept in
    def __init__(self, master, setup, contents):  # this will initialise the position and size of the toolbar
        self.master = master
        self.setup = setup
        self.contents = contents
        colours = self.setup["themes"][self.setup["themes"]["current"]]
        self.background = [colours["clr4"], colours["clrA"]]
        self.foreground = [colours["clr3"], colours["clr1"], colours["clr2"]]
        self.border = colours["light_border"]
        self.test = colours["test"]

        frame = tkinter.Frame(self.master, width=200, height=650, bg=self.background[0], highlightcolor="black",
                              highlightthickness=0)
        frame.place(x=0, y=0)
        self.notebook = ttk.Notebook(frame, width=198, height=650)
        self.notebook.place(x=0, y=0)

        if "Widget" in self.contents[3]:
            self.widgetTool_frame = tkinter.Frame(self.notebook, bg=self.background[1])
            self.widgetTool_frame.place(x=0, y=0)
            self.widget = widgetTool(self.widgetTool_frame, self.setup)
            self.notebook.add(self.widgetTool_frame, text="Widget")
        else:
            self.widget = None
        if "Customisation" in self.contents[3]:
            self.customisationTool_frame = tkinter.Frame(self.notebook, bg=self.background[1])
            self.customisationTool_frame.place(x=0, y=0)
            self.customisation = customisationTool(self.customisationTool_frame, self.setup)
            self.notebook.add(self.customisationTool_frame, text="Customisation")
        else:
            self.customisation = None
        if "Layout" in self.contents[3]:
            self.layoutTool_frame = tkinter.Frame(self.notebook, bg=self.background[1])
            self.layoutTool_frame.place(x=0, y=0)
            self.layout = layoutTool(self.layoutTool_frame, self.setup)
            self.notebook.add(self.layoutTool_frame, text="Layout")
        else:
            self.layout = None

    def show(self, tool_):
        tabs = [self.notebook.tab(i, option="text") for i in self.notebook.tabs()]
        if tool_ == "Widget" and tool_ not in tabs:
            self.notebook.add(self.widgetTool_frame, text="Widget")
        elif tool_ == "Customisation" and tool_ not in tabs:
            self.notebook.add(self.customisationTool_frame, text="Customisation")
        elif tool_ == "Layout" and tool_ not in tabs:
            self.notebook.add(self.layoutTool_frame, text="Layout")
        else:
            pass

    def hide(self, tool):
        tabs = [self.notebook.tab(i, option="text") for i in self.notebook.tabs()]
        index = None
        if tool == "Widget":
            for _, tab in enumerate(tabs):
                if tab == "Widget":
                    index = _
            try:
                self.notebook.forget(self.notebook.tabs()[index])
            except TypeError:
                pass
        elif tool == "Customisation":
            for _, tab in enumerate(tabs):
                if tab == "Customisation":
                    index = _
            try:
                self.notebook.forget(self.notebook.tabs()[index])
            except TypeError:
                pass
        elif tool == "Layout":
            for _, tab in enumerate(tabs):
                if tab == "Layout":
                    index = _
            try:
                self.notebook.forget(self.notebook.tabs()[index])
            except TypeError:
                pass
        else:
            pass

    @property
    def tools(self):
        return [self.notebook.tab(i, option="text") for i in self.notebook.tabs()]

    @property
    def items(self):
        return self.widget.items

    def select(self, Type, data):
        if "Customisation" in self.contents[3]:
            apply = self.customisation.select(Type, data)
        else:
            apply = None
        return apply


class widgetTool:  # this is a class that will contain logos for each of the widgets that can be put on the GUI
    def __init__(self, master, setup):  # this will initialise the position and design of the widget tool
        self.master = master
        self.setup = setup
        colours = self.setup["themes"][self.setup["themes"]["current"]]
        self.background = [colours["clr4"], colours["clrA"]]
        self.foreground = [colours["clr3"], colours["clr1"], colours["clr2"]]
        self.border = colours["light_border"]
        self.test = colours["test"]


class customisationTool:  # this will be used to edit the appearance of the widgets
    def __init__(self, master, setup):  # this will initialise the position and the format of this widget
        self.master = master
        self.setup = setup
        colours = self.setup["themes"][self.setup["themes"]["current"]]
        self.background = [colours["clr4"], colours["clrA"]]
        self.foreground = [colours["clr3"], colours["clr1"], colours["clr2"]]
        self.border = colours["light_border"]
        self.test = colours["test"]


class layoutTool:
    def __init__(self, master, setup):
        self.master = master
        self.setup = setup
        colours = self.setup["themes"][self.setup["themes"]["current"]]
        self.background = [colours["clr4"], colours["clrA"]]
        self.foreground = [colours["clr3"], colours["clr1"], colours["clr2"]]
        self.border = colours["light_border"]
        self.test = colours["test"]


if __name__ == "__main__":
    root = tkinter.Tk()
    root.resizable(False, False)

    with open(SETUP, "r") as f:
        initial_setup = json.load(f)
    left = initial_setup["previous"]["toolbars"]["left"]
    right = initial_setup["previous"]["toolbars"]["right"]
    if left[2] == 0:
        master1 = root
    else:
        master1 = tkinter.Toplevel(root)
        master1.geometry("200x650")
    if right[2] == 0:
        master2 = root
    else:
        master2 = tkinter.Toplevel(root)
        master1.geometry("200x650")
    if left[2] == 0 and right[2] == 1 and left[0] == 1 and right[0] == 1:
        root.geometry("850x650")
    elif left[2] == 1 and right[2] == 0 and left[0] == 1 and right[0] == 1:
        root.geometry("850x650")
    elif left[2] == 1 and right[2] == 1 and left[0] == 1 and right[0] == 1:
        root.geometry("650x650")
    elif left[2] == 0 and right[2] == 1 and left[0] == 0 and right[0] == 1:
        root.geometry("650x650")
    elif left[2] == 1 and right[2] == 0 and left[0] == 0 and right[0] == 1:
        root.geometry("850x650")
    elif left[2] == 1 and right[2] == 1 and left[0] == 0 and right[0] == 1:
        root.geometry("650x650")
    elif left[2] == 0 and right[2] == 1 and left[0] == 1 and right[0] == 0:
        root.geometry("850x650")
    elif left[2] == 1 and right[2] == 0 and left[0] == 1 and right[0] == 0:
        root.geometry("650x650")
    elif left[2] == 1 and right[2] == 1 and left[0] == 1 and right[0] == 0:
        root.geometry("650x650")
    elif left[2] == 0 and right[2] == 0 and left[0] == 1 and right[0] == 1:
        root.geometry("1050x650")
    elif left[2] == 0 and right[2] == 0 and left[0] == 1 and right[0] == 0:
        root.geometry("850x650")
    elif left[2] == 0 and right[2] == 0 and left[0] == 0 and right[0] == 1:
        root.geometry("850x650")
    elif left[0] == 0 and right[0] == 0:
        root.geometry("650x650")
    else:
        pass
    toolbar1_frame = tkinter.Frame(master1, width=200, height=650, bg="brown")
    if left[0] == 1:
        toolbar1_frame.place(x=0, y=0)
    editing_frame = tkinter.Frame(root, width=650, height=650, bg="purple")
    if left[0] == 1:
        editing_frame.place(x=200, y=0)
    else:
        editing_frame.place(x=0, y=0)
    toolbar2_frame = tkinter.Frame(master2, width=200, height=650, bg="red")
    if right[0] == 1 and left[0] == 1:
        toolbar2_frame.place(x=850, y=0)
    elif right[0] == 1 and left[0] == 0:
        toolbar2_frame.place(x=650, y=0)

    main = app(root, initial_setup)
    if left[0] == 1:
        toolbar1 = toolBar(toolbar1_frame, initial_setup, initial_setup["previous"]["toolbars"]["left"])
    else:
        toolbar1 = None
    if right[0] == 1:
        toolbar2 = toolBar(toolbar2_frame, initial_setup, initial_setup["previous"]["toolbars"]["right"])
    else:
        toolbar2 = None
    editing_section = editing(editing_frame, initial_setup)
    main.initiate_objects(toolbar1, editing_section, toolbar2)
    if initial_setup["completed"] == 0:
        to_open = tkinter.Toplevel(root)
        opening(to_open)
        to_open.transient(root)
        to_open.grab_set()
        root.wait_window(to_open)

    root.mainloop()
