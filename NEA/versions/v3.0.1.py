import tkinter
from tkinter import ttk
import json
from tkinter import messagebox
from tkinter import filedialog
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

    def initiate_objects(self, tool_bar1, main_canvas, tool_bar2):
        self.toolbar1 = tool_bar1
        self.main_canvas = main_canvas
        self.toolbar2 = tool_bar2


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
    if initial_setup["completed"] == 0:
        to_open = tkinter.Toplevel(root)
        opening(to_open)
        to_open.transient(root)
        to_open.grab_set()
        root.wait_window(to_open)
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

    root.mainloop()
