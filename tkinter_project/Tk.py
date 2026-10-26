from tkinter import *
from tkinter import ttk

'''
ben you have now done the menu bar
you need to start making what all of the menu items do
then you must make the widget editor
then you make the coder
then you make the widget designer

next:
figure out opening files
make format for file
make template
make the widget editor
make a label widget
save to template
make the moving of widgets
make new templates
do the rest
'''

class maker:
    def __init__(self, master, window_title="Tk Maker", width=1000, height=550, activebackground="Blue",
                 activeborderwidth=1, activeforeground="White", bg="White", bd=1, cursor=None,
                 disabledforeground="Grey", fg="Black", postcommand=None, relief=RAISED, tearoff=0, title=None):
        self._root = master
        self._root.wm_title(window_title)
        self._root.geometry(f"{width}x{height}")
        menubar = Menu(self._root, activebackground=activebackground, activeborderwidth=activeborderwidth,
                       activeforeground=activeforeground, bg=bg, bd=bd, cursor=cursor,
                       disabledforeground=disabledforeground, fg=fg, postcommand=postcommand, relief=relief,
                       tearoff=tearoff, title=title)
        fileMenu = Menu(menubar, activebackground=activebackground, activeforeground=activeforeground, bg=bg, fg=fg,
                        tearoff=0)
        fileMenu.add_command(label="New", accelerator="Ctrl+n", command=self.new)
        fileMenu.add_command(label="Open", accelerator="Ctrl+o", command=self.open)
        fileMenu.add_command(label="Save", accelerator="Ctrl+s", command=self.save)
        fileMenu.add_command(label="Save As", accelerator="Ctrl+Shift+s", command=self.saveAs)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", accelerator="Esc", command=self.exit)
        menubar.add_cascade(label="File", menu=fileMenu, activebackground=activebackground,
                            activeforeground=activeforeground)

        editMenu = Menu(menubar, activebackground=activebackground, activeforeground=activeforeground, bg=bg, fg=fg,
                        tearoff=0)
        editMenu.add_command(label="Background colour", accelerator="Ctrl+b", command=self.bg_change)
        editMenu.add_command(label="Delete Widget", accelerator="Del", command=self.delete)
        editMenu.add_command(label="Paste", accelerator="Ctrl+v", command=self.paste)
        editMenu.add_command(label="Copy", accelerator="Ctrl+c", command=self.copy)
        editMenu.add_command(label="Cut", accelerator="Ctrl+x", command=self.cut)
        menubar.add_cascade(label="Edit", menu=editMenu, activebackground=activebackground,
                            activeforeground=activeforeground)

        viewMenu = Menu(menubar, activebackground=activebackground, activeforeground=activeforeground, bg=bg, fg=fg,
                        tearoff=0)
        viewMenu.add_command(label="Code editor", accelerator="Alt+c", command=self.coder)
        viewMenu.add_command(label="Widget editor", accelerator="Alt+e", command=self.widgets)
        viewMenu.add_command(label="Widget designer", accelerator="Alt+d", command=self.design)
        menubar.add_cascade(label="View", menu=viewMenu, activebackground=activebackground,
                            activeforeground=activeforeground)

        helpMenu = Menu(menubar, activebackground=activebackground, activeforeground=activeforeground, bg=bg, fg=fg,
                        tearoff=0)
        helpMenu.add_command(label="About...", accelerator="Ctrl+a", command=self.about)
        menubar.add_cascade(label="Help", menu=helpMenu)

        self._root.config(menu=menubar)

    def binds(self):
        self._root.bind("<Control-Key-n>", self.new)
        self._root.bind("<Control-Key-o>", self.open)
        self._root.bind("<Control-Key-s>", self.save)
        self._root.bind("<Control-Shift-Key-s>", self.saveAs)
        self._root.bind("<Escape>", self.exit)
        self._root.bind("<Control-Key-b>", self.bg_change)
        self._root.bind("<Delete>", self.delete)
        self._root.bind("<Control-Key-v>", self.paste)
        self._root.bind("<Control-Key-c>", self.copy)
        self._root.bind("<Control-Key-x>", self.cut)
        self._root.bind("<Alt-Key-c>", self.coder)
        self._root.bind("<Alt-Key-e>", self.widgets)
        self._root.bind("<Alt-Key-d>", self.design)
        self._root.bind("<Control-Key-a>", self.about)

    def new(self, event=None):
        pass

    def open(self, event=None):
        pass

    def save(self, event=None):
        pass

    def saveAs(self, event=None):
        pass

    def exit(self, event=None):
        pass

    def bg_change(self, event=None):
        pass

    def delete(self, event=None):
        pass

    def about(self, event=None):
        pass

    def coder(self, event=None):
        pass

    def widgets(self, event=None):
        pass

    def design(self, event=None):
        pass

    def copy(self, event=None):
        pass

    def paste(self, event=None):
        pass

    def cut(self, event=None):
        pass


class elements:
    def __init__(self, *args, **kwargs):
        self._root = Tk()


class coder:
    def __init__(self, *args, **kwargs):
        self._root = Tk()


if __name__ == '__main__':
    root = Tk()
    app = maker(root)
    root.mainloop()
