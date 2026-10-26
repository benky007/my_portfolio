import tkinter
from tkinter import ttk
import json
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
import os
import glob

SETUP = "setup.json"


def bubble(list1, element=None):
    if type(list1[0]) is str or type(list1[0]) is int:
        for i in range(len(list1) - 1):
            for j in range(len(list1) - i - 1):
                if list1[j] > list1[j + 1]:
                    temp = list1[j]
                    list1[j] = list1[j + 1]
                    list1[j + 1] = temp
        return list1
    elif type(list1[0]) is dict:
        if element is None:
            element = list1[0][list(list1[0].keys())[0]]
        for i in range(len(list1) - 1):
            for j in range(len(list1) - i - 1):
                if list1[j][element] > list1[j + 1][element]:
                    temp = list1[j]
                    list1[j] = list1[j + 1]
                    list1[j + 1] = temp
        return list1
    else:
        return None


def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)


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
        self.left = tkinter.Frame(self.master, bg=self.background[0], width=250, highlightbackground=self.border,
                                  highlightthickness=0)
        self.left.pack(side=tkinter.LEFT, fill="y", expand=True, anchor=tkinter.W)
        self.left.pack_propagate(False)
        self.right = tkinter.Frame(self.master, bg=self.background[0], width=250, highlightbackground=self.border,
                                   highlightthickness=1)
        self.right.pack(side=tkinter.RIGHT, fill="y", expand=True, anchor=tkinter.NW)
        self.right.pack_propagate(False)

        description_frame = tkinter.Frame(self.right, bg=self.background[0], height=130)
        description_frame.pack(side=tkinter.TOP, fill="x", expand=True, anchor=tkinter.N)
        description_frame.pack_propagate(False)
        options = tkinter.Frame(self.right, bg=self.background[0], height=120)
        options.pack(side=tkinter.BOTTOM, fill="x", expand=True, anchor=tkinter.S)
        options.pack_propagate(False)

        title = tkinter.Label(self.left, text="GUI\nBuilder", font=("Helvetica", 40), bg=self.background[1],
                              fg=self.foreground[2])
        title.pack(fill="x", expand=True)
        description1 = tkinter.Label(self.left, text="This is a tool to help\n"
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

    def delete(self):
        self.left.pack_forget()
        self.right.pack_forget()

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
        try:
            self.toolbar1.items[0][0].bind("<Button-1>",
                                           lambda event: self.create_moveable_widget(event, self.toolbar1.items[0][1]))
            self.toolbar1.items[1][0].bind("<Button-1>",
                                           lambda event: self.create_moveable_widget(event, self.toolbar1.items[1][1]))
            self.toolbar1.items[2][0].bind("<Button-1>",
                                           lambda event: self.create_moveable_widget(event, self.toolbar1.items[2][1]))
            self.toolbar1.items[3][0].bind("<Button-1>",
                                           lambda event: self.create_moveable_widget(event, self.toolbar1.items[3][1]))
            self.toolbar1.items[4][0].bind("<Button-1>",
                                           lambda event: self.create_moveable_widget(event, self.toolbar1.items[4][1]))
            self.toolbar1.items[5][0].bind("<Button-1>",
                                           lambda event: self.create_moveable_widget(event, self.toolbar1.items[5][1]))
            self.toolbar1.items[0][0].bind("<B1-Motion>", lambda event: self.move_moveable_widget(event))
            self.toolbar1.items[1][0].bind("<B1-Motion>", lambda event: self.move_moveable_widget(event))
            self.toolbar1.items[2][0].bind("<B1-Motion>", lambda event: self.move_moveable_widget(event))
            self.toolbar1.items[3][0].bind("<B1-Motion>", lambda event: self.move_moveable_widget(event))
            self.toolbar1.items[4][0].bind("<B1-Motion>", lambda event: self.move_moveable_widget(event))
            self.toolbar1.items[5][0].bind("<B1-Motion>", lambda event: self.move_moveable_widget(event))
            self.toolbar1.items[0][0].bind("<ButtonRelease-1>", lambda event: self.check_drop(event, "Frame"))
            self.toolbar1.items[1][0].bind("<ButtonRelease-1>", lambda event: self.check_drop(event, "Label"))
            self.toolbar1.items[2][0].bind("<ButtonRelease-1>", lambda event: self.check_drop(event, "Button"))
            self.toolbar1.items[3][0].bind("<ButtonRelease-1>", lambda event: self.check_drop(event, "Entry"))
            self.toolbar1.items[4][0].bind("<ButtonRelease-1>", lambda event: self.check_drop(event, "Checkbutton"))
            self.toolbar1.items[5][0].bind("<ButtonRelease-1>", lambda event: self.check_drop(event, "Radiobutton"))
        except AttributeError:
            try:
                self.toolbar2.items[0][0].bind("<Button-1>",
                                               lambda event: self.create_moveable_widget(event,
                                                                                         self.toolbar2.items[0][1]))
                self.toolbar2.items[1][0].bind("<Button-1>",
                                               lambda event: self.create_moveable_widget(event,
                                                                                         self.toolbar2.items[1][1]))
                self.toolbar2.items[2][0].bind("<Button-1>",
                                               lambda event: self.create_moveable_widget(event,
                                                                                         self.toolbar2.items[2][1]))
                self.toolbar2.items[3][0].bind("<Button-1>",
                                               lambda event: self.create_moveable_widget(event,
                                                                                         self.toolbar2.items[3][1]))
                self.toolbar2.items[4][0].bind("<Button-1>",
                                               lambda event: self.create_moveable_widget(event,
                                                                                         self.toolbar2.items[4][1]))
                self.toolbar2.items[5][0].bind("<Button-1>",
                                               lambda event: self.create_moveable_widget(event,
                                                                                         self.toolbar2.items[5][1]))
                self.toolbar2.items[0][0].bind("<B1-Motion>", lambda event: self.move_moveable_widget(event))
                self.toolbar2.items[1][0].bind("<B1-Motion>", lambda event: self.move_moveable_widget(event))
                self.toolbar2.items[2][0].bind("<B1-Motion>", lambda event: self.move_moveable_widget(event))
                self.toolbar2.items[3][0].bind("<B1-Motion>", lambda event: self.move_moveable_widget(event))
                self.toolbar2.items[4][0].bind("<B1-Motion>", lambda event: self.move_moveable_widget(event))
                self.toolbar2.items[5][0].bind("<B1-Motion>", lambda event: self.move_moveable_widget(event))
                self.toolbar2.items[0][0].bind("<ButtonRelease-1>", lambda event: self.check_drop(event, "Frame"))
                self.toolbar2.items[1][0].bind("<ButtonRelease-1>", lambda event: self.check_drop(event, "Label"))
                self.toolbar2.items[2][0].bind("<ButtonRelease-1>", lambda event: self.check_drop(event, "Button"))
                self.toolbar2.items[3][0].bind("<ButtonRelease-1>", lambda event: self.check_drop(event, "Entry"))
                self.toolbar2.items[4][0].bind("<ButtonRelease-1>", lambda event: self.check_drop(event, "Checkbutton"))
                self.toolbar2.items[5][0].bind("<ButtonRelease-1>", lambda event: self.check_drop(event, "Radiobutton"))
            except AttributeError:
                pass

    def create_moveable_widget(self, event, item):
        if len(self.main_canvas.projects) > 0:
            self.click = (event.x, event.y)
            if item == "frame":
                self.moving = tkinter.Frame(self.master, width=100, height=40, highlightbackground="black",
                                            highlightthickness=1)
                self.coords = (879, 79)
            elif item == "label":
                self.moving = tkinter.Label(self.master, text="Label", width=13, height=2, highlightbackground="black",
                                            highlightthickness=1)
                self.coords = (879, 179)
            elif item == "button":
                self.moving = tkinter.Button(self.master, text="Button", width=13, height=2, state="disabled",
                                             highlightbackground="black", highlightthickness=1)
                self.coords = (879, 279)
            elif item == "entry":
                self.moving = tkinter.Entry(self.master, width=13, highlightbackground="black", highlightthickness=1)
                self.moving.config(state="disabled")
                self.coords = (879, 379)
            elif item == "checkbutton":
                self.moving = tkinter.Checkbutton(self.master, text="Check Button", width=13, height=2,
                                                  state="disabled", highlightbackground="black", highlightthickness=1)
                self.coords = (879, 479)
            elif item == "radiobutton":
                self.moving = tkinter.Radiobutton(self.master, text="Radio Button", width=13, height=2,
                                                  highlightbackground="black", highlightthickness=1)
                self.coords = (879, 579)
            else:
                pass
            self.moving.place(x=self.coords[0], y=self.coords[1])
        else:
            pass

    def move_moveable_widget(self, event):
        if len(self.main_canvas.projects) > 0:
            self.moving.place(x=self.coords[0] - self.click[0] + event.x, y=self.coords[1] - self.click[1] + event.y)
        else:
            pass

    def check_drop(self, event, widget):
        self.moving.place_forget()
        if widget == "Frame" and self.main_canvas.size[0] >= event.x + 600 >= 0 and self.main_canvas.size[1] >= event.y - 30 >= 0:
            self.open_projects[-1].add_widget(widget, (event.x + 600 - self.click[0]) / self.main_canvas.ratio_get,
                                              (event.y - 30 - self.click[1]) / self.main_canvas.ratio_get)
            new = self.main_canvas.add(self.open_projects[-1].data["Widgets"][-1])
            new.bind("<Button-1>", lambda event: self.select(event, new))
            self.select(event, self.open_projects[-1].data["Widgets"][-1]["ID"])
        elif widget == "Label" and self.main_canvas.size[0] >= event.x + 600 >= 0 and self.main_canvas.size[1] >= event.y + 70 >= 0:
            self.open_projects[-1].add_widget(widget, (event.x + 600 - self.click[0]) / self.main_canvas.ratio_get,
                                              (event.y + 70 - self.click[1]) / self.main_canvas.ratio_get)
            new = self.main_canvas.add(self.open_projects[-1].data["Widgets"][-1])
            new.bind("<Button-1>", lambda event: self.select(event, new))
            self.select(event, self.open_projects[-1].data["Widgets"][-1]["ID"])
        elif widget == "Button" and self.main_canvas.size[0] >= event.x + 600 >= 0 and self.main_canvas.size[1] >= event.y + 170 >= 0:
            self.open_projects[-1].add_widget(widget, (event.x + 600 - self.click[0]) / self.main_canvas.ratio_get,
                                              (event.y + 170 - self.click[1]) / self.main_canvas.ratio_get)
            new = self.main_canvas.add(self.open_projects[-1].data["Widgets"][-1])
            new.bind("<Button-1>", lambda event: self.select(event, new))
            self.select(event, self.open_projects[-1].data["Widgets"][-1]["ID"])
        elif widget == "Entry" and self.main_canvas.size[0] >= event.x + 600 >= 0 and self.main_canvas.size[1] >= event.y + 270 >= 0:
            self.open_projects[-1].add_widget(widget, (event.x + 600 - self.click[0]) / self.main_canvas.ratio_get,
                                              (event.y + 270 - self.click[1]) / self.main_canvas.ratio_get)
            new = self.main_canvas.add(self.open_projects[-1].data["Widgets"][-1])
            new.bind("<Button-1>", lambda event: self.select(event, new))
            self.select(event, self.open_projects[-1].data["Widgets"][-1]["ID"])
        elif widget == "Checkbutton" and self.main_canvas.size[0] >= event.x + 600 >= 0 and self.main_canvas.size[1] >= event.y + 370 >= 0:
            self.open_projects[-1].add_widget(widget, (event.x + 600 - self.click[0]) / self.main_canvas.ratio_get,
                                              (event.y + 370 - self.click[1]) / self.main_canvas.ratio_get)
            new = self.main_canvas.add(self.open_projects[-1].data["Widgets"][-1])
            new.bind("<Button-1>", lambda event: self.select(event, new))
            self.select(event, self.open_projects[-1].data["Widgets"][-1]["ID"])
        elif widget == "Radiobutton" and self.main_canvas.size[0] >= event.x + 600 >= 0 and self.main_canvas.size[1] >= event.y + 470 >= 0:
            self.open_projects[-1].add_widget(widget, (event.x + 600 - self.click[0]) / self.main_canvas.ratio_get,
                                              (event.y + 470 - self.click[1]) / self.main_canvas.ratio_get)
            new = self.main_canvas.add(self.open_projects[-1].data["Widgets"][-1])
            new.bind("<Button-1>", lambda event: self.select(event, new))
            self.select(event, self.open_projects[-1].data["Widgets"][-1]["ID"])
        else:
            pass

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
        fileMenu.add_command(label="Save", command=lambda: self.save())
        fileMenu.add_command(label="Export", command=lambda: self.export())
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

    def save(self):  # this will save the file as its own directory with different files to store the attributes of
        # each widget and their position to load it again
        self.open_projects[-1].save()

    def export(self):
        main_data = self.open_projects[-1].data["root"]
        widgets = bubble(self.open_projects[-1].data["Widgets"], "ID")
        file = (f"import tkinter\nfrom tkinter import font\n\n"
                f"def window(master):\n"
                f"    main = tkinter.Canvas(master, width={main_data['width']},height={main_data['height']}, "
                f"bg='{main_data['bg']}')\n"
                f"    main.place(x=0, y=0)\n")
        for widget in widgets:
            if widget["Type"] == "Frame":
                file = file + (f"    widget{widget['ID']} = tkinter.Frame(main, width={widget['attr']['width']}, "
                               f"height={widget['attr']['height']}, bd={widget['attr']['bd']}, "
                               f"relief='{widget['attr']['relief']}', cursor='{widget['attr']['cursor']}', "
                               f"highlightthickness={widget['attr']['ht']}, highlightcolor='{widget['attr']['hc']}', "
                               f"highlightbackground='{widget['attr']['hb']}', bg='{widget['attr']['bg']}')\n    "
                               f"widget{widget['ID']}.place(x={widget['attr']['x']}, y={widget['attr']['y']})\n")
            elif widget["Type"] == "Button":
                file = file + (f"    widget{widget['ID']} = tkinter.Button(main, width={widget['attr']['width']}, "
                               f"height={widget['attr']['height']}, activebackground='{widget['attr']['ab']}', "
                               f"activeforeground='{widget['attr']['af']}', bd={widget['attr']['bd']}, "
                               f"bg='{widget['attr']['bg']}', fg='{widget['attr']['fg']}', font=font.Font(family="
                               f"'{widget['attr']['font'][0]}', size={int(widget['attr']['font'][1])}, weight="
                               f"'{widget['attr']['font'][2]}'), highlightcolor='{widget['attr']['hc']}', "
                               f"justify='{widget['attr']['justify']}', padx={widget['attr']['padx']}, "
                               f"pady={widget['attr']['pady']}, relief='{widget['attr']['relief']}', "
                               f"state='{widget['attr']['state']}', underline={widget['attr']['uline']}, "
                               f"wraplength={widget['attr']['wl']}, highlightbackground='{widget['attr']['hb']}', "
                               f"highlightthickness={widget['attr']['ht']}, text='{widget['attr']['text']}')\n    "
                               f"widget{widget['ID']}.place(x={widget['attr']['x']}, y={widget['attr']['y']})\n")
            elif widget["Type"] == "Label":
                file = file + (f"    widget{widget['ID']} = tkinter.Label(main, width={widget['attr']['width']}, "
                               f"height={widget['attr']['height']}, anchor='{widget['attr']['anchor']}', "
                               f"bg='{widget['attr']['bg']}', bd={widget['attr']['bd']}, "
                               f"cursor='{widget['attr']['cursor']}', font=font.Font(family="
                               f"'{widget['attr']['font'][0]}', size={int(widget['attr']['font'][1])}, "
                               f"weight='{widget['attr']['font'][2]}'), fg='{widget['attr']['fg']}', "
                               f"justify='{widget['attr']['justify']}', padx={widget['attr']['padx']}, "
                               f"pady={widget['attr']['pady']}, relief='{widget['attr']['relief']}', "
                               f"text='{widget['attr']['text']}', underline={widget['attr']['uline']}, "
                               f"wraplength={widget['attr']['wl']}, highlightbackground='{widget['attr']['hb']}', "
                               f"highlightthickness={widget['attr']['ht']})\n    widget{widget['ID']}.place(x="
                               f"{widget['attr']['x']}, y={widget['attr']['y']})\n")
            elif widget["Type"] == "Entry":
                file = file + (f'    widget{widget["ID"]} = tkinter.Entry(main, width={widget["attr"]["width"]}, '
                               f'bg="{widget["attr"]["bg"]}", bd={widget["attr"]["bd"]}, '
                               f'cursor="{widget["attr"]["cursor"]}", '
                               f'font=font.Font(family="{widget["attr"]["font"][0]}", '
                               f'size={int(widget["attr"]["font"][1])}, weight="{widget["attr"]["font"][2]}"), '
                               f'show="{widget["attr"]["show"]}", exportselection={widget["attr"]["es"]}, '
                               f'fg="{widget["attr"]["fg"]}", highlightcolor="{widget["attr"]["hc"]}", '
                               f'justify="{widget["attr"]["justify"]}", relief="{widget["attr"]["relief"]}", '
                               f'selectbackground="{widget["attr"]["sb"]}", selectborderwidth={widget["attr"]["sbw"]}, '
                               f'selectforeground="{widget["attr"]["sf"]}", state="{widget["attr"]["state"]}", '
                               f'highlightbackground="{widget["attr"]["hb"]}", '
                               f'highlightthickness={widget["attr"]["ht"]})\n    widget{widget["ID"]}.place(x='
                               f'{widget["attr"]["x"]}, y={widget["attr"]["y"]})\n')
            elif widget["Type"] == "Checkbutton":
                file = file + (f'    widget{widget["ID"]} = tkinter.Checkbutton(main, width={widget["attr"]["width"]}, '
                               f'height={widget["attr"]["height"]}, activebackground="{widget["attr"]["ab"]}", '
                               f'activeforeground="{widget["attr"]["af"]}", bg="{widget["attr"]["bg"]}", bd='
                               f'{widget["attr"]["bd"]}, cursor="{widget["attr"]["cursor"]}", disabledforeground="'
                               f'{widget["attr"]["df"]}", font=font.Font(family="{widget["attr"]["font"][0]}", '
                               f'size={int(widget["attr"]["font"][1])}, weight="{widget["attr"]["font"][2]}"),'
                               f'fg="{widget["attr"]["fg"]}", highlightcolor="{widget["attr"]["hc"]}", '
                               f'justify="{widget["attr"]["justify"]}", offvalue={widget["attr"]["ofv"]}, '
                               f'onvalue={widget["attr"]["onv"]}, padx={widget["attr"]["padx"]}, pady='
                               f'{widget["attr"]["pady"]}, relief="{widget["attr"]["relief"]}", selectcolor="'
                               f'{widget["attr"]["sc"]}", state="{widget["attr"]["state"]}", underline='
                               f'{widget["attr"]["uline"]}, text="{widget["attr"]["text"]}", wraplength='
                               f'{widget["attr"]["wl"]}, highlightbackground="{widget["attr"]["hb"]}", '
                               f'highlightthickness={widget["attr"]["ht"]})\n    widget{widget["ID"]}.place(x='
                               f'{widget["attr"]["x"]}, y={widget["attr"]["y"]})\n')
            elif widget["Type"] == "Radiobutton":
                file = file + (f'    widget{widget["ID"]} = tkinter.Radiobutton(main, width={widget["attr"]["width"]}, '
                               f'height={widget["attr"]["height"]}, activebackground="{widget["attr"]["ab"]}", '
                               f'activeforeground="{widget["attr"]["af"]}", anchor="{widget["attr"]["anchor"]}", '
                               f'bg="{widget["attr"]["bg"]}", borderwidth={widget["attr"]["bd"]}, cursor="'
                               f'{widget["attr"]["cursor"]}", font=font.Font(family="{widget["attr"]["font"][0]}", '
                               f'size={int(widget["attr"]["font"][1])}, weight="{widget["attr"]["font"][2]}"), '
                               f'fg="{widget["attr"]["fg"]}", highlightcolor="{widget["attr"]["hc"]}", '
                               f'highlightbackground="{widget["attr"]["hb"]}", highlightthickness='
                               f'{widget["attr"]["ht"]}, justify="{widget["attr"]["justify"]}", padx='
                               f'{widget["attr"]["padx"]}, pady={widget["attr"]["pady"]}, relief="'
                               f'{widget["attr"]["relief"]}", selectcolor="{widget["attr"]["sc"]}", state="'
                               f'{widget["attr"]["state"]}", text="{widget["attr"]["text"]}", underline='
                               f'{widget["attr"]["uline"]}, value={widget["attr"]["value"]}, wraplength='
                               f'{widget["attr"]["wl"]})\n    widget{widget["ID"]}.place(x={widget["attr"]["x"]}, '
                               f'y={widget["attr"]["y"]})\n')
            else:
                pass
        file = file + (f"\nif __name__ == '__main__':\n"
                       f"    root = tkinter.Tk()\n"
                       f"    root.resizable(False, False)\n"
                       f"    root.geometry('{int(main_data['width'])}x{int(main_data['height'])}')\n"
                       f"    root.configure(bg='{main_data['bg']}')\n    root.title('{main_data['title']}')\n\n"
                       f"    app=window(root)\n\n"
                       f"    root.mainloop()\n")
        if os.path.isfile(f"{self.open_projects[-1].path}/{main_data['title']}.py"):
            if messagebox.askquestion(title="Confirm Save As", message=f"{main_data['title']}.py already exists.\nDo "
                                                                       f"you want to replace it?",
                                      icon=messagebox.WARNING) == "no":
                files = glob.glob(f"{self.open_projects[-1].path}/{main_data['title']}(*).py")
                with open(f"{self.open_projects[-1].path}/{main_data['title']}({len(files) + 1}).py", "w") as f_exp:
                    f_exp.write(file)
            else:
                with open(f"{self.open_projects[-1].path}/{main_data['title']}.py", "w") as f_exp:
                    f_exp.write(file)
        else:
            with open(f"{self.open_projects[-1].path}/{main_data['title']}.py", "w") as f_exp:
                f_exp.write(file)

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

    @property
    def selected(self):
        chosen = None
        for index, widget in enumerate(self._data["Widgets"]):
            if widget["ID"] == self.focussed:
                chosen = index
            else:
                pass
        if chosen is not None:
            return self._data["Widgets"][chosen]
        else:
            return None

    @selected.setter
    def selected(self, value):
        self.focussed = value

    @property
    def Widgets(self):
        return self.widgets

    @property
    def data(self):
        return self._data

    def select_id(self, identification):
        self.selected = identification

    def select_object(self, object1):
        self.selected = self.Widgets.index(object1)

    @property
    def projects(self):
        return [self.notebook.tab(i, option="text") for i in self.notebook.tabs()]

    @property
    def size(self):
        return self.ratio * self._data["root"]["width"], self.ratio * self._data["root"]["height"]

    @property
    def ratio_get(self):
        return self.ratio


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

        frame1 = tkinter.Frame(self.master, width=180, height=90, bg="#ff0000")
        frame1.place(x=10, y=10)
        canvas1 = tkinter.Canvas(frame1, width=180, height=90, bg=colours["clr8"])
        canvas1.place(x=-2, y=-2)
        round_rectangle(canvas1, 5, 5, 180, 90, fill=self.background[0], outline="black")
        canvas1.create_text(33, 20, text="Frame", fill=self.foreground[0])
        canvas1.create_line(15, 30, 170, 30, fill="black", smooth=True, width=2)
        clickable_frame = tkinter.Frame(canvas1, width=100, height=40, bg="white", highlightbackground="black",
                                        highlightthickness=1)
        clickable_frame.place(x=20, y=40)

        frame2 = tkinter.Frame(self.master, width=180, height=90, bg="#df0000")
        frame2.place(x=10, y=110)
        canvas2 = tkinter.Canvas(frame2, width=180, height=90, bg=colours["clr8"])
        canvas2.place(x=-2, y=-2)
        round_rectangle(canvas2, 5, 5, 180, 90, fill=self.background[0], outline="black")
        canvas2.create_text(31, 20, text="Label", fill=self.foreground[0])
        canvas2.create_line(15, 30, 170, 30, fill="black", smooth=True, width=2)
        clickable_label = tkinter.Label(canvas2, text="Label", width=13, height=2, highlightbackground="black",
                                        highlightthickness=1)
        clickable_label.place(x=20, y=40)

        frame3 = tkinter.Frame(self.master, width=180, height=90, bg="#bf0000")
        frame3.place(x=10, y=210)
        canvas3 = tkinter.Canvas(frame3, width=180, height=90, bg=colours["clr8"])
        canvas3.place(x=-2, y=-2)
        round_rectangle(canvas3, 5, 5, 180, 90, fill=self.background[0], outline="black")
        canvas3.create_text(34, 20, text="Button", fill=self.foreground[0])
        canvas3.create_line(15, 30, 170, 30, fill="black", smooth=True, width=2)
        clickable_button = tkinter.Button(canvas3, text="Button", width=13, height=2, state="disabled",
                                          highlightbackground="black", highlightthickness=1)
        clickable_button.place(x=20, y=40)

        frame4 = tkinter.Frame(self.master, width=180, height=90, bg="#9f0000")
        frame4.place(x=10, y=310)
        canvas4 = tkinter.Canvas(frame4, width=180, height=90, bg=colours["clr8"])
        canvas4.place(x=-2, y=-2)
        round_rectangle(canvas4, 5, 5, 180, 90, fill=self.background[0], outline="black")
        canvas4.create_text(30, 20, text="Entry", fill=self.foreground[0])
        canvas4.create_line(15, 30, 170, 30, fill="black", smooth=True, width=2)
        clickable_entry = tkinter.Entry(canvas4, width=13, highlightbackground="black", highlightthickness=1)
        clickable_entry.config(state="disabled")
        clickable_entry.place(x=20, y=40)

        frame5 = tkinter.Frame(self.master, width=180, height=90, bg="#7f0000")
        frame5.place(x=10, y=410)
        canvas5 = tkinter.Canvas(frame5, width=180, height=90, bg=colours["clr8"])
        canvas5.place(x=-2, y=-2)
        round_rectangle(canvas5, 5, 5, 180, 90, fill=self.background[0], outline="black")
        canvas5.create_text(53, 20, text="Check Button", fill=self.foreground[0])
        canvas5.create_line(15, 30, 170, 30, fill="black", smooth=True, width=2)
        clickable_checkbutton = tkinter.Checkbutton(canvas5, text="Check Button", width=13, height=2, state="disabled",
                                                    highlightbackground="black", highlightthickness=1)
        clickable_checkbutton.place(x=20, y=40)

        frame6 = tkinter.Frame(self.master, width=180, height=90, bg="#5f0000")
        frame6.place(x=10, y=510)
        canvas6 = tkinter.Canvas(frame6, width=180, height=90, bg=colours["clr8"])
        canvas6.place(x=-2, y=-2)
        round_rectangle(canvas6, 5, 5, 180, 90, fill=self.background[0], outline="black")
        canvas6.create_text(52, 20, text="Radio Button", fill=self.foreground[0])
        canvas6.create_line(15, 30, 170, 30, fill="black", smooth=True, width=2)
        clickable_radiobutton = tkinter.Radiobutton(canvas6, text="Radio Button", width=13, height=2,
                                                    highlightbackground="black", highlightthickness=1)
        clickable_radiobutton.place(x=20, y=40)

        self.clickables = [(clickable_frame, "frame"), (clickable_label, "label"), (clickable_button, "button"),
                           (clickable_entry, "entry"), (clickable_checkbutton, "checkbutton"),
                           (clickable_radiobutton, "radiobutton")]

    @property
    def items(self):
        return self.clickables


class customisationTool:  # this will be used to edit the appearance of the widgets
    def __init__(self, master, setup):  # this will initialise the position and the format of this widget
        self.master = master
        self.setup = setup
        colours = self.setup["themes"][self.setup["themes"]["current"]]
        self.background = [colours["clr4"], colours["clrA"]]
        self.foreground = [colours["clr3"], colours["clr1"], colours["clr2"]]
        self.border = colours["light_border"]
        self.test = colours["test"]

        container = tkinter.Frame(self.master, width=200, height=650, bg=colours["clr8"])
        canvas = tkinter.Canvas(container, width=180, height=617, bg=colours["clr8"])
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tkinter.Frame(canvas, bg=colours["clr8"])
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.frame1A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame1A.pack(padx=10, pady=10)
        canvas1A = tkinter.Canvas(self.frame1A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas1A.place(x=-2, y=-2)
        round_rectangle(canvas1A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas1A.create_text(45, 20, text="X-Position", fill=self.foreground[0])
        canvas1A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame1B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame1B.pack(padx=10, pady=10)
        canvas1B = tkinter.Canvas(self.frame1B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas1B.place(x=-2, y=-2)
        round_rectangle(canvas1B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas1B.create_text(45, 20, text="X-Position", fill=self.foreground[0])
        canvas1B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry1 = tkinter.Entry(canvas1B, width=18)
        self.entry1.place(x=20, y=40)

        self.frame2A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame2A.pack(padx=10, pady=10)
        canvas2A = tkinter.Canvas(self.frame2A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas2A.place(x=-2, y=-2)
        round_rectangle(canvas2A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas2A.create_text(45, 20, text="Y-Position", fill=self.foreground[0])
        canvas2A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame2B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame2B.pack(padx=10, pady=10)
        canvas2B = tkinter.Canvas(self.frame2B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas2B.place(x=-2, y=-2)
        round_rectangle(canvas2B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas2B.create_text(45, 20, text="Y-Position", fill=self.foreground[0])
        canvas2B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry2 = tkinter.Entry(canvas2B, width=18)
        self.entry2.place(x=20, y=40)

        self.frame3A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame3A.pack(padx=10, pady=10)
        canvas3A = tkinter.Canvas(self.frame3A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas3A.place(x=-2, y=-2)
        round_rectangle(canvas3A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas3A.create_text(32, 20, text="Width", fill=self.foreground[0])
        canvas3A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame3B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame3B.pack(padx=10, pady=10)
        canvas3B = tkinter.Canvas(self.frame3B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas3B.place(x=-2, y=-2)
        round_rectangle(canvas3B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas3B.create_text(32, 20, text="Width", fill=self.foreground[0])
        canvas3B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry3 = tkinter.Entry(canvas3B, width=18)
        self.entry3.place(x=20, y=40)

        self.frame4A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame4A.pack(padx=10, pady=10)
        canvas4A = tkinter.Canvas(self.frame4A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas4A.place(x=-2, y=-2)
        round_rectangle(canvas4A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas4A.create_text(34, 20, text="Height", fill=self.foreground[0])
        canvas4A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame4B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame4B.pack(padx=10, pady=10)
        canvas4B = tkinter.Canvas(self.frame4B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas4B.place(x=-2, y=-2)
        round_rectangle(canvas4B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas4B.create_text(34, 20, text="Height", fill=self.foreground[0])
        canvas4B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry4 = tkinter.Entry(canvas4B, width=18)
        self.entry4.place(x=20, y=40)

        self.frame5A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame5A.pack(padx=10, pady=10)
        canvas5A = tkinter.Canvas(self.frame5A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas5A.place(x=-2, y=-2)
        round_rectangle(canvas5A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas5A.create_text(67, 20, text="Background colour", fill=self.foreground[0])
        canvas5A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame5B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame5B.pack(padx=10, pady=10)
        canvas5B = tkinter.Canvas(self.frame5B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas5B.place(x=-2, y=-2)
        round_rectangle(canvas5B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas5B.create_text(67, 20, text="Background colour", fill=self.foreground[0])
        canvas5B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry5 = tkinter.Entry(canvas5B, width=18)
        self.entry5.place(x=20, y=40)

        self.frame6A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame6A.pack(padx=10, pady=10)
        canvas6A = tkinter.Canvas(self.frame6A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas6A.place(x=-2, y=-2)
        round_rectangle(canvas6A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas6A.create_text(50, 20, text="Border width", fill=self.foreground[0])
        canvas6A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame6B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame6B.pack(padx=10, pady=10)
        canvas6B = tkinter.Canvas(self.frame6B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas6B.place(x=-2, y=-2)
        round_rectangle(canvas6B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas6B.create_text(50, 20, text="Border width", fill=self.foreground[0])
        canvas6B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry6 = tkinter.Entry(canvas6B, width=18)
        self.entry6.place(x=20, y=40)

        self.frame7A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame7A.pack(padx=10, pady=10)
        canvas7A = tkinter.Canvas(self.frame7A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas7A.place(x=-2, y=-2)
        round_rectangle(canvas7A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas7A.create_text(51, 20, text="Highlight BG", fill=self.foreground[0])
        canvas7A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame7B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame7B.pack(padx=10, pady=10)
        canvas7B = tkinter.Canvas(self.frame7B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas7B.place(x=-2, y=-2)
        round_rectangle(canvas7B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas7B.create_text(51, 20, text="Highlight BG", fill=self.foreground[0])
        canvas7B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry7 = tkinter.Entry(canvas7B, width=18)
        self.entry7.place(x=20, y=40)

        self.frame8A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame8A.pack(padx=10, pady=10)
        canvas8A = tkinter.Canvas(self.frame8A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas8A.place(x=-2, y=-2)
        round_rectangle(canvas8A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas8A.create_text(58, 20, text="Highlight width", fill=self.foreground[0])
        canvas8A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame8B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame8B.pack(padx=10, pady=10)
        canvas8B = tkinter.Canvas(self.frame8B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas8B.place(x=-2, y=-2)
        round_rectangle(canvas8B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas8B.create_text(58, 20, text="Highlight width", fill=self.foreground[0])
        canvas8B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry8 = tkinter.Entry(canvas8B, width=18)
        self.entry8.place(x=20, y=40)

        self.frame9A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame9A.pack(padx=10, pady=10)
        canvas9A = tkinter.Canvas(self.frame9A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas9A.place(x=-2, y=-2)
        round_rectangle(canvas9A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas9A.create_text(59, 20, text="Highlight colour", fill=self.foreground[0])
        canvas9A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame9B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame9B.pack(padx=10, pady=10)
        canvas9B = tkinter.Canvas(self.frame9B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                  borderwidth=0)
        canvas9B.place(x=-2, y=-2)
        round_rectangle(canvas9B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas9B.create_text(59, 20, text="Highlight colour", fill=self.foreground[0])
        canvas9B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry9 = tkinter.Entry(canvas9B, width=18)
        self.entry9.place(x=20, y=40)

        self.frame10A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame10A.pack(padx=10, pady=10)
        canvas10A = tkinter.Canvas(self.frame10A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas10A.place(x=-2, y=-2)
        round_rectangle(canvas10A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas10A.create_text(30, 20, text="Relief", fill=self.foreground[0])
        canvas10A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame10B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame10B.pack(padx=10, pady=10)
        canvas10B = tkinter.Canvas(self.frame10B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas10B.place(x=-2, y=-2)
        round_rectangle(canvas10B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas10B.create_text(30, 20, text="Relief", fill=self.foreground[0])
        canvas10B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry10 = tkinter.Entry(canvas10B, width=18)
        self.entry10.place(x=20, y=40)

        self.frame11A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame11A.pack(padx=10, pady=10)
        canvas11A = tkinter.Canvas(self.frame11A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas11A.place(x=-2, y=-2)
        round_rectangle(canvas11A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas11A.create_text(67, 20, text="Active Background", fill=self.foreground[0])
        canvas11A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame11B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame11B.pack(padx=10, pady=10)
        canvas11B = tkinter.Canvas(self.frame11B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas11B.place(x=-2, y=-2)
        round_rectangle(canvas11B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas11B.create_text(67, 20, text="Active Background", fill=self.foreground[0])
        canvas11B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry11 = tkinter.Entry(canvas11B, width=18)
        self.entry11.place(x=20, y=40)

        self.frame12A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame12A.pack(padx=10, pady=10)
        canvas12A = tkinter.Canvas(self.frame12A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas12A.place(x=-2, y=-2)
        round_rectangle(canvas12A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas12A.create_text(67, 20, text="Active Foreground", fill=self.foreground[0])
        canvas12A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame12B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame12B.pack(padx=10, pady=10)
        canvas12B = tkinter.Canvas(self.frame12B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas12B.place(x=-2, y=-2)
        round_rectangle(canvas12B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas12B.create_text(67, 20, text="Active Foreground", fill=self.foreground[0])
        canvas12B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry12 = tkinter.Entry(canvas12B, width=18)
        self.entry12.place(x=20, y=40)

        self.frame13A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame13A.pack(padx=10, pady=10)
        canvas13A = tkinter.Canvas(self.frame13A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas13A.place(x=-2, y=-2)
        round_rectangle(canvas13A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas13A.create_text(67, 20, text="Foreground colour", fill=self.foreground[0])
        canvas13A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame13B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame13B.pack(padx=10, pady=10)
        canvas13B = tkinter.Canvas(self.frame13B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas13B.place(x=-2, y=-2)
        round_rectangle(canvas13B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas13B.create_text(67, 20, text="Foreground colour", fill=self.foreground[0])
        canvas13B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry13 = tkinter.Entry(canvas13B, width=18)
        self.entry13.place(x=20, y=40)

        self.frame14A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame14A.pack(padx=10, pady=10)
        canvas14A = tkinter.Canvas(self.frame14A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas14A.place(x=-2, y=-2)
        round_rectangle(canvas14A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas14A.create_text(33, 20, text="Justify", fill=self.foreground[0])
        canvas14A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame14B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame14B.pack(padx=10, pady=10)
        canvas14B = tkinter.Canvas(self.frame14B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas14B.place(x=-2, y=-2)
        round_rectangle(canvas14B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas14B.create_text(33, 20, text="Justify", fill=self.foreground[0])
        canvas14B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry14 = tkinter.Entry(canvas14B, width=18)
        self.entry14.place(x=20, y=40)

        self.frame15A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame15A.pack(padx=10, pady=10)
        canvas15A = tkinter.Canvas(self.frame15A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas15A.place(x=-2, y=-2)
        round_rectangle(canvas15A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas15A.create_text(31, 20, text="State", fill=self.foreground[0])
        canvas15A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame15B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame15B.pack(padx=10, pady=10)
        canvas15B = tkinter.Canvas(self.frame15B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas15B.place(x=-2, y=-2)
        round_rectangle(canvas15B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas15B.create_text(31, 20, text="State", fill=self.foreground[0])
        canvas15B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry15 = tkinter.Entry(canvas15B, width=18)
        self.entry15.place(x=20, y=40)

        self.frame16A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame16A.pack(padx=10, pady=10)
        canvas16A = tkinter.Canvas(self.frame16A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas16A.place(x=-2, y=-2)
        round_rectangle(canvas16A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas16A.create_text(42, 20, text="Underline", fill=self.foreground[0])
        canvas16A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame16B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame16B.pack(padx=10, pady=10)
        canvas16B = tkinter.Canvas(self.frame16B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas16B.place(x=-2, y=-2)
        round_rectangle(canvas16B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas16B.create_text(42, 20, text="Underline", fill=self.foreground[0])
        canvas16B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry16 = tkinter.Entry(canvas16B, width=18)
        self.entry16.place(x=20, y=40)

        self.frame17A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame17A.pack(padx=10, pady=10)
        canvas17A = tkinter.Canvas(self.frame17A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas17A.place(x=-2, y=-2)
        round_rectangle(canvas17A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas17A.create_text(28, 20, text="Text", fill=self.foreground[0])
        canvas17A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame17B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame17B.pack(padx=10, pady=10)
        canvas17B = tkinter.Canvas(self.frame17B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas17B.place(x=-2, y=-2)
        round_rectangle(canvas17B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas17B.create_text(28, 20, text="Text", fill=self.foreground[0])
        canvas17B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry17 = tkinter.Entry(canvas17B, width=18)
        self.entry17.place(x=20, y=40)

        self.frame18A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame18A.pack(padx=10, pady=10)
        canvas18A = tkinter.Canvas(self.frame18A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas18A.place(x=-2, y=-2)
        round_rectangle(canvas18A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas18A.create_text(30, 20, text="Padx", fill=self.foreground[0])
        canvas18A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame18B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame18B.pack(padx=10, pady=10)
        canvas18B = tkinter.Canvas(self.frame18B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas18B.place(x=-2, y=-2)
        round_rectangle(canvas18B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas18B.create_text(30, 20, text="Padx", fill=self.foreground[0])
        canvas18B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry18 = tkinter.Entry(canvas18B, width=18)
        self.entry18.place(x=20, y=40)

        self.frame19A = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frame19A.pack(padx=10, pady=10)
        canvas19A = tkinter.Canvas(self.frame19A, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas19A.place(x=-2, y=-2)
        round_rectangle(canvas19A, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvas19A.create_text(30, 20, text="Pady", fill=self.foreground[0])
        canvas19A.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.frame19B = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frame19B.pack(padx=10, pady=10)
        canvas19B = tkinter.Canvas(self.frame19B, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                   borderwidth=0)
        canvas19B.place(x=-2, y=-2)
        round_rectangle(canvas19B, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvas19B.create_text(30, 20, text="Pady", fill=self.foreground[0])
        canvas19B.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)
        self.entry19 = tkinter.Entry(canvas19B, width=18)
        self.entry19.place(x=20, y=40)

        self.apply = tkinter.Button(scrollable_frame, width=6, height=2, fg=self.foreground[0], bg=self.background[0],
                                    text="Apply")
        self.apply.pack(side="bottom", anchor="s")

        container.place(x=0, y=0)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.frame1B.pack_forget()
        self.frame2B.pack_forget()
        self.frame3B.pack_forget()
        self.frame4B.pack_forget()
        self.frame5B.pack_forget()
        self.frame6B.pack_forget()
        self.frame7B.pack_forget()
        self.frame8B.pack_forget()
        self.frame9B.pack_forget()
        self.frame10B.pack_forget()
        self.frame11B.pack_forget()
        self.frame12B.pack_forget()
        self.frame13B.pack_forget()
        self.frame14B.pack_forget()
        self.frame15B.pack_forget()
        self.frame16B.pack_forget()
        self.frame17B.pack_forget()
        self.frame18B.pack_forget()
        self.frame19B.pack_forget()

    def delete(self, which):
        self.entry1.delete(0, tkinter.END)
        self.entry2.delete(0, tkinter.END)
        self.entry3.delete(0, tkinter.END)
        self.entry4.delete(0, tkinter.END)
        self.entry5.delete(0, tkinter.END)
        self.entry6.delete(0, tkinter.END)
        self.entry7.delete(0, tkinter.END)
        self.entry8.delete(0, tkinter.END)
        self.entry9.delete(0, tkinter.END)
        self.entry10.delete(0, tkinter.END)
        self.entry11.delete(0, tkinter.END)
        self.entry12.delete(0, tkinter.END)
        self.entry13.delete(0, tkinter.END)
        self.entry14.delete(0, tkinter.END)
        self.entry15.delete(0, tkinter.END)
        self.entry16.delete(0, tkinter.END)
        self.entry17.delete(0, tkinter.END)
        self.entry18.delete(0, tkinter.END)
        self.entry19.delete(0, tkinter.END)
        if which == "A":
            self.frame1A.pack_forget()
            self.frame2A.pack_forget()
            self.frame3A.pack_forget()
            self.frame4A.pack_forget()
            self.frame5A.pack_forget()
            self.frame6A.pack_forget()
            self.frame7A.pack_forget()
            self.frame8A.pack_forget()
            self.frame9A.pack_forget()
            self.frame10A.pack_forget()
            self.frame11A.pack_forget()
            self.frame12A.pack_forget()
            self.frame13A.pack_forget()
            self.frame14A.pack_forget()
            self.frame15A.pack_forget()
            self.frame16A.pack_forget()
            self.frame17A.pack_forget()
            self.frame18A.pack_forget()
            self.frame19A.pack_forget()
        elif which == "B":
            self.frame1B.pack_forget()
            self.frame2B.pack_forget()
            self.frame3B.pack_forget()
            self.frame4B.pack_forget()
            self.frame5B.pack_forget()
            self.frame6B.pack_forget()
            self.frame7B.pack_forget()
            self.frame8B.pack_forget()
            self.frame9B.pack_forget()
            self.frame10B.pack_forget()
            self.frame11B.pack_forget()
            self.frame12B.pack_forget()
            self.frame13B.pack_forget()
            self.frame14B.pack_forget()
            self.frame15B.pack_forget()
            self.frame16B.pack_forget()
            self.frame17B.pack_forget()
            self.frame18B.pack_forget()
            self.frame19B.pack_forget()
        else:
            self.delete("A")
            self.delete("B")

    def select(self, widget):
        if widget == "Frame":
            self.delete("both")
            self.frame1B.pack(padx=10, pady=10)
            self.frame2B.pack(padx=10, pady=10)
            self.frame3B.pack(padx=10, pady=10)
            self.frame4B.pack(padx=10, pady=10)
            self.frame5B.pack(padx=10, pady=10)
            self.frame6B.pack(padx=10, pady=10)
            self.frame7B.pack(padx=10, pady=10)
            self.frame8B.pack(padx=10, pady=10)
            self.frame9B.pack(padx=10, pady=10)
            self.frame10A.pack(padx=10, pady=10)
            self.frame11A.pack(padx=10, pady=10)
            self.frame12A.pack(padx=10, pady=10)
            self.frame13A.pack(padx=10, pady=10)
            self.frame14A.pack(padx=10, pady=10)
            self.frame15A.pack(padx=10, pady=10)
            self.frame16A.pack(padx=10, pady=10)
            self.frame17A.pack(padx=10, pady=10)
            self.frame18A.pack(padx=10, pady=10)
            self.frame19A.pack(padx=10, pady=10)
        elif widget == "Label":
            self.delete("both")
            self.frame1B.pack(padx=10, pady=10)
            self.frame2B.pack(padx=10, pady=10)
            self.frame3B.pack(padx=10, pady=10)
            self.frame4B.pack(padx=10, pady=10)
            self.frame5B.pack(padx=10, pady=10)
            self.frame6B.pack(padx=10, pady=10)
            self.frame7B.pack(padx=10, pady=10)
            self.frame8B.pack(padx=10, pady=10)
            self.frame9B.pack(padx=10, pady=10)
            self.frame10B.pack(padx=10, pady=10)
            self.frame13B.pack(padx=10, pady=10)
            self.frame14B.pack(padx=10, pady=10)
            self.frame16B.pack(padx=10, pady=10)
            self.frame17B.pack(padx=10, pady=10)
            self.frame18B.pack(padx=10, pady=10)
            self.frame19B.pack(padx=10, pady=10)
            self.frame11A.pack(padx=10, pady=10)
            self.frame12A.pack(padx=10, pady=10)
            self.frame15A.pack(padx=10, pady=10)
        elif widget == "Button":
            self.delete("both")
            self.frame1B.pack(padx=10, pady=10)
            self.frame2B.pack(padx=10, pady=10)
            self.frame3B.pack(padx=10, pady=10)
            self.frame4B.pack(padx=10, pady=10)
            self.frame5B.pack(padx=10, pady=10)
            self.frame6B.pack(padx=10, pady=10)
            self.frame7B.pack(padx=10, pady=10)
            self.frame8B.pack(padx=10, pady=10)
            self.frame9B.pack(padx=10, pady=10)
            self.frame10B.pack(padx=10, pady=10)
            self.frame11B.pack(padx=10, pady=10)
            self.frame12B.pack(padx=10, pady=10)
            self.frame13B.pack(padx=10, pady=10)
            self.frame14B.pack(padx=10, pady=10)
            self.frame15B.pack(padx=10, pady=10)
            self.frame16B.pack(padx=10, pady=10)
            self.frame17B.pack(padx=10, pady=10)
            self.frame18B.pack(padx=10, pady=10)
            self.frame19B.pack(padx=10, pady=10)
        elif widget == "Entry":
            self.delete("both")
            self.frame1B.pack(padx=10, pady=10)
            self.frame2B.pack(padx=10, pady=10)
            self.frame3B.pack(padx=10, pady=10)
            self.frame5B.pack(padx=10, pady=10)
            self.frame6B.pack(padx=10, pady=10)
            self.frame7B.pack(padx=10, pady=10)
            self.frame8B.pack(padx=10, pady=10)
            self.frame9B.pack(padx=10, pady=10)
            self.frame10B.pack(padx=10, pady=10)
            self.frame13B.pack(padx=10, pady=10)
            self.frame14B.pack(padx=10, pady=10)
            self.frame15B.pack(padx=10, pady=10)
            self.frame4A.pack(padx=10, pady=10)
            self.frame11A.pack(padx=10, pady=10)
            self.frame12A.pack(padx=10, pady=10)
            self.frame16A.pack(padx=10, pady=10)
            self.frame17A.pack(padx=10, pady=10)
            self.frame18A.pack(padx=10, pady=10)
            self.frame19A.pack(padx=10, pady=10)
        elif widget == "Checkbutton":
            self.delete("both")
            self.frame1B.pack(padx=10, pady=10)
            self.frame2B.pack(padx=10, pady=10)
            self.frame3B.pack(padx=10, pady=10)
            self.frame4B.pack(padx=10, pady=10)
            self.frame5B.pack(padx=10, pady=10)
            self.frame6B.pack(padx=10, pady=10)
            self.frame7B.pack(padx=10, pady=10)
            self.frame8B.pack(padx=10, pady=10)
            self.frame9B.pack(padx=10, pady=10)
            self.frame10B.pack(padx=10, pady=10)
            self.frame11B.pack(padx=10, pady=10)
            self.frame12B.pack(padx=10, pady=10)
            self.frame13B.pack(padx=10, pady=10)
            self.frame14B.pack(padx=10, pady=10)
            self.frame15B.pack(padx=10, pady=10)
            self.frame16B.pack(padx=10, pady=10)
            self.frame17B.pack(padx=10, pady=10)
            self.frame18B.pack(padx=10, pady=10)
            self.frame19B.pack(padx=10, pady=10)
        elif widget == "Radiobutton":
            self.delete("both")
            self.frame1B.pack(padx=10, pady=10)
            self.frame2B.pack(padx=10, pady=10)
            self.frame3B.pack(padx=10, pady=10)
            self.frame4B.pack(padx=10, pady=10)
            self.frame5B.pack(padx=10, pady=10)
            self.frame6B.pack(padx=10, pady=10)
            self.frame7B.pack(padx=10, pady=10)
            self.frame8B.pack(padx=10, pady=10)
            self.frame9B.pack(padx=10, pady=10)
            self.frame10B.pack(padx=10, pady=10)
            self.frame11B.pack(padx=10, pady=10)
            self.frame12B.pack(padx=10, pady=10)
            self.frame14B.pack(padx=10, pady=10)
            self.frame15B.pack(padx=10, pady=10)
            self.frame16B.pack(padx=10, pady=10)
            self.frame17B.pack(padx=10, pady=10)
            self.frame18B.pack(padx=10, pady=10)
            self.frame19B.pack(padx=10, pady=10)
            self.frame13A.pack(padx=10, pady=10)
        else:
            pass
        return self.apply, self.data

    @property
    def data(self):
        storage = {"x": self.entry1.get(), "y": self.entry2.get(), "width": self.entry3.get(),
                   "height": self.entry4.get(), "bg": self.entry5.get(), "bd": self.entry6.get(),
                   "hb": self.entry7.get(), "ht": self.entry8.get(), "hc": self.entry9.get(),
                   "relief": self.entry10.get(), "ab": self.entry11.get(), "af": self.entry12.get(),
                   "fg": self.entry13.get(), "justify": self.entry14.get(), "state": self.entry15.get(),
                   "uline": self.entry16.get(), "text": self.entry17.get(), "padx": self.entry18.get(),
                   "pady": self.entry19.get()}
        return storage


class layoutTool:
    def __init__(self, master, setup):
        self.master = master
        self.setup = setup
        colours = self.setup["themes"][self.setup["themes"]["current"]]
        self.background = [colours["clr4"], colours["clrA"]]
        self.foreground = [colours["clr3"], colours["clr1"], colours["clr2"]]
        self.border = colours["light_border"]
        self.test = colours["test"]

        container = tkinter.Frame(self.master, width=200, height=650, bg=colours["clr8"])
        canvas = tkinter.Canvas(container, width=180, height=617, bg=colours["clr8"])
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tkinter.Frame(canvas, bg=colours["clr8"])
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.frameA = tkinter.Frame(scrollable_frame, width=180, height=40, bg=colours["clr8"])
        self.frameA.pack(padx=10, pady=10)
        canvasA = tkinter.Canvas(self.frameA, width=165, height=42, bg=colours["clr8"], highlightthickness=0,
                                 borderwidth=0)
        canvasA.place(x=-2, y=-2)
        shape = round_rectangle(canvasA, 5, 5, 160, 40, fill=self.background[0], outline="black")
        canvasA.tag_bind(shape, "<Button-1>", lambda e: self.toggle(e, 0))
        canvasA.create_text(20, 20, text="root", fill=self.foreground[0], anchor="w")

        self.frameB = tkinter.Frame(scrollable_frame, width=180, height=90, bg=colours["clr8"])
        self.frameB.pack(padx=10, pady=10)
        canvasB = tkinter.Canvas(self.frameB, width=165, height=92, bg=colours["clr8"], highlightthickness=0,
                                 borderwidth=0)
        canvasB.place(x=-2, y=-2)
        shape = round_rectangle(canvasB, 5, 5, 160, 90, fill=self.background[0], outline="black")
        canvasB.tag_bind(shape, "<Button-1>", lambda e: self.toggle(e, 1))
        canvasB.create_text(20, 20, text="root", fill=self.foreground[0], anchor="w")
        canvasB.create_line(15, 30, 150, 30, fill="black", smooth=True, width=2)

        self.toggle(None, 1)

        container.place(x=0, y=0)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def toggle(self, event, to_toggle):
        if to_toggle == 0:
            self.frameA.pack_forget()
            self.frameB.pack(padx=10, pady=10)
        elif to_toggle == 1:
            self.frameB.pack_forget()
            self.frameA.pack(padx=10, pady=10)
        else:
            self.frameA.pack_forget()
            self.frameB.pack_forget()


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
