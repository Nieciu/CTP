import tkinter
import pandas as pd
import numpy as np
from tkinter import filedialog as fd

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = tkinter.Tk()
root.wm_title("CTP")

fig = Figure(figsize=(6, 4), dpi=200)
t = np.arange(0, 3, .01)
filename = fd.askopenfilename()
df = pd.read_csv(filename, sep='\t', header=0, index_col=0, decimal=',')
fig.add_subplot(222).plot(df)


canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()
    root.destroy()


quit = tkinter.Button(master=root, text="Quit", command=_quit)
quit.pack(side=tkinter.BOTTOM)


def menu_callback():
    print("I'm in the menu callback!")


def submenu_callback():
    print("I'm in the submenu callback!")


menu_widget = tkinter.Menu(root)
submenu_widget = tkinter.Menu(menu_widget, tearoff=False)
submenu_widget.add_command(label="Submenu Item1", command=submenu_callback)
submenu_widget.add_command(label="Submenu Item2", command=submenu_callback)
menu_widget.add_cascade(label="Item1", menu=submenu_widget)
menu_widget.add_command(label="Item2", command=menu_callback)
menu_widget.add_command(label="Item3", command=menu_callback)
root.config(menu=menu_widget)

tkinter.mainloop()
