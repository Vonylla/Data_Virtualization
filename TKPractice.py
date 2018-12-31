from tkinter import * # import everything from tkinter

class Window(Frame): # inherit from Frame class from tkinter

    def __init__(self, master=None):
        Frame.__init__(self, master) # define settings upon initialization
        self.master = master # reference to the master widget, the tk window
        self.init_window()


    def init_window(self): # Creation of init_window

        self.master.title("GUI") # changing the title of our master widget

        self.pack(fill=BOTH, expand=1) # allowing the widget to take the full space of the root window

        # create a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu) # create the file object
        file.add_command(label="Exit", command=self.client_exit) # adds a command to the menu option, calling it exit, and the command it runs on event is client_exit
        menu.add_cascade(label="File", menu=file) # add "File" to our menu

        edit = Menu(menu) # create the file object
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)

        quitButton = Button(self, text="Quit", command=self.client_exit) # creating a button instance
        quitButton.place(x=0, y=0) # placing the button on my window

    def client_exit(self):
        exit()

root = Tk() # create root window

root.geometry("800x500") # size of the window

app = Window(root) # create instance

root.mainloop() # show and begin mainloop