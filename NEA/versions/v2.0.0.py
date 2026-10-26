import tkinter
from tkinter import ttk
import json

SETUP = "setup.json"


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
