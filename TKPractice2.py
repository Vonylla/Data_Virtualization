from tkinter import * # import everything from tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

#from matplotlib import pyplot as plt

import numpy as np
import csv


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

root.geometry("1280x720") # size of the window

app = Window(root) # create instance

#fig = Figure(figsize=(5, 4), dpi=100)
fig = Figure()
t = np.arange(0, 3, .01)

# Draw CPC
with open('input.txt') as fil:
    reader = csv.reader(fil, delimiter=" ")
    data = list(reader)
print(data)
# Get data into paired coordinate form (x,y) for CPC
x = []
y = []
xHolder = 0
yHolder = 0
for i in range(len(data) - 1):
    if i % 2 == 1:
        continue
    print(i)
    xHolder = int(data[i][2]) + int(xHolder)
    yHolder = int(data[i + 1][2]) + int(yHolder)
    x.append(int(xHolder))
    y.append(int(yHolder))

print(x)
print(y)
a = fig.add_subplot(111) #.plot(x, y) # 1 by 1, graph #1?
a.set_title("CPC")
a.set_xlabel('x1')
a.set_ylabel('x2')
a.grid(color='gray', linestyle='-', linewidth=0.5)
a.plot(x, y)




canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)

#root.mainloop() # show and begin mainloop
while True: # Scrolling on trackpad (Mac) throws error
    try:
        root.mainloop()
        break
    except UnicodeDecodeError:
        pass