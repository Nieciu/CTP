import tkinter
import pandas as pd
import numpy as np
from tkinter import filedialog as fd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = tkinter.Tk()
fig = Figure(figsize=(6, 4), dpi=200)
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
toolbar = NavigationToolbar2Tk(canvas, root)
photo = tkinter.PhotoImage(file=r"C:\Users\pati\PycharmProjects\CTP2\upload.png")
toolbar.update()


def init():
    root.wm_title("CTP")
    t = np.arange(0, 3, .01)
    filename = fd.askopenfilename()
    df = pd.read_csv(filename, sep='\t', header=0, index_col=0, decimal=',')
    fig.add_subplot(111).plot(df)
    draw()


def draw():
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


init()


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()
    root.destroy()


quit = tkinter.Button(master=root, text="Quit", command=_quit)
quit.pack(side=tkinter.BOTTOM)


def load():
    fig.clear()
    init()


def menu_callback():
    print("I'm in the submenu callback!")


def submenu_callback():
    print("I'm in the submenu callback!")


def antyaliasing():
    print("antyaliasing")


def open_calc_widnow():
    new = tkinter.Toplevel()
    new.title("calc")
    new.geometry("200x100")
    button_new = tkinter.Button(master=new, text="oblicz")
    button_new.pack(side=tkinter.LEFT)
    e = tkinter.Entry(master=new, width=50, )
    e.pack()


def calc():
    print("")


button = tkinter.Button(master=toolbar,
                        image=photo, command=load)
button.pack(side="left")
menu_widget = tkinter.Menu(root)
submenu_widget = tkinter.Menu(menu_widget, tearoff=False)
menu_widget.add_command(label="Calc", command=open_calc_widnow)
menu_widget.add_command(label="Antyaliasing", command=antyaliasing)
menu_widget.add_command(label="Item3", command=menu_callback)
root.config(menu=menu_widget)

tkinter.mainloop()
