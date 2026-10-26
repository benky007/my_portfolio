import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import json
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
        # image = Image.open(r"C:\Users\ben\JetBrains\PycharmProjects\NEA\img\folder.png")
        # image = image.resize((50, 50))
        # image = ImageTk.PhotoImage(image)
        file_explorer = tkinter.Button(path_entry_frame, text="Browse", command=lambda: self.browseFiles())
        file_explorer.pack(side=tkinter.LEFT)

        apply_button_frame = tkinter.Frame(options, bg=self.background[0], height=30, borderwidth=5)
        apply_button_frame.pack(fill="x", expand=True)
        apply_button_frame.pack_propagate(False)
        apply_button = tkinter.Button(apply_button_frame, text="Apply", command=lambda: self.apply())
        apply_button.pack(fill="x", expand=True)
        # sort out layout
        # thinking big title in top left then description to the right then path underneath and language underneath
        # then ok apply and cancel buttons
        # functions of buttons

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


class app:  # this is the main class of the program
    def __init__(self):  # this will initialise this main window
        pass

    def menu(self):  # this will initialise the menu at the top
        pass

    def handleMenu(self):  # this will handle any commands attached to the menu bar
        pass

    def save(self):  # this will save the file as its own directory with different files to store the attributes of each widget and their position to load it again
        pass

    def new(self):  # this will create a new GUI that will be a blank template
        pass

    def open(self):  # this will open a file explorer to choose a directory in the correct format to load
        pass

    def export(self):  # this will read each section of the JSON file with all the details and create an exact copy of it in python
        pass

    def view(self):  # this will handle all view requests as viewing different tools can be selected
        pass

    def screenLayout(self):  # this will handle the layout of the screen as the user can choose between 1, 2 or 3 tool bars in different locations on the scren
        pass

    def applicationStyle(self):  # this will be where a pre-designed style can be selected to be applied to the whole window
        pass

    def about(self):  # this will open a small window to explain the program
        pass

    def guides(self):  # this will open a new window to have a catalouge of guides to help teach the user hwo to use the tool
        pass

    def move(self):  # this will be ran once a widget is attempted to be placed to help it move across the screen
        pass

    def place(self):  # this will handle for when the widget is dropped
        pass


class editing:  # this is the class that runs and handles the editing part of the screen
    def __init__(self):  # this will initialise the ediitng suite
        pass

    def resize(self):  # this will handle any trys to change the size of the editing suite and the eventually exported GUI
        pass

    def add(self):  # this will add a new widget and its position to a list
        pass

    def ammend(self):  # this will handle any situations when a widget is moved after being placed
        pass

    def write(self):  # this will check the contents of the JSON file and write any new widgets
        pass

    @property
    def contents(self):  # this will return the list with every widget and their positions
        pass

    @contents.setter
    def contents(self):  # this will set the list of every widget to overwrite the contents
        pass

    @property
    def details(self):  # this wil return a full run down of every widget and all fo their attributes
        pass

    @details.setter
    def details(self):  # this will allow you to edit their attributes directly
        pass


class newWidget:  # this creates an object for each new widget added
    def __init__(self):  # this initialises the position and basic template of each widget
        self.bind("<Button-1>", self.choose)
        self.bind("<B1-Motion>", self.move)

    def move(self, event):  # this will handle the movement by binding the key and then calculating x and y positions before running the move method in app
        widget = event.widget
        x = widget.winfo_x() - widget._drag_start_x + event.x
        y = widget.winfo_y() - widget._drag_start_y + event.y
        return x, y

    @property
    def attributes(self):  # this will return all of the atributes attribuuted to this widget
        pass

    @attributes.setter
    def attributes(self):  # this will be used to edit the attributes of the widget
        pass

    @property
    def pos(self):  # this will return the position of the widget
        pass

    def choose(self, event):  # this will initialise the movement of the widget
        widget = event.widget
        widget._drag_start_x = event.x
        widget._drag_start_y = event.y


class toolBar:  # this is a class that handles the frames on the screen in which the tools are kept in
    def __init__(self):  # this will initialise the position and size of the toolbar
        pass

    def layout(self):  # this will be used to edit the position of the toolbar
        pass

    def organise(self):  # this will be used to edit the number of tools in the toolbar and the organisation of it
        pass

    @property
    def contents(self):  # this will return the contents of the toolbar
        pass


class widgetTool:  # this is a class that will contain logos for each of the widgets that can be put on the GUI
    def __init__(self):  # this will initalise the poisiton and design of the widget tool
        pass

    @property
    def selected(self):  # this will return any selected widget from the list of potential widgets
        pass

    @selected.setter
    def selected(self):  # this will manually select a widget
        pass

    def new(self):  # this will create a new widget to be put on the screen
        pass

    def imported(self):  # this will be a file icon that the user can import an external widget
        pass

    def create(self):  # this will be a plus icon that can be clicked to open up the widget creator but as that is a limitation if it is not complete this button will be disabled
        pass


class customisationTool:  # this will be used to edit the appearence of the widgets
    def __init__(self):  # this will initialise the position and the format of this widget
        pass

    @property
    def selected(self):  # this will return any selected fields
        pass

    @selected.setter
    def selected(self):  # this will set any of the fields to selected
        pass

    def activate(self):  # this will set certain attributes of the widgets to be able to be changed or not
        pass

    def deactivate(self):  # this will disable certain attributes that can change
        pass

    def update(self):  # this will be in the form of a apply button that will update all selected widgets
        pass


class apperancePreview:  # this will be another tool that will show any temporary changes to the appearence of the selected widgets
    def __init__(self):  # this will initialise the position and size of the tool
        pass

    def show(self):  # this will show the tool if it is selected to be shown
        pass

    def hide(self):  # this will hide the tool
        pass

    def update(self):  # this will apply all the changes that have been made to the appearence of the widget
        pass

    def error(self):
        pass

    @property
    def shown(self):
        pass


class layoutTool:
    def __init__(self):
        pass

    def update(self):
        pass

    @property
    def shown(self):
        pass


class tool:
    pass

class error:
    pass

