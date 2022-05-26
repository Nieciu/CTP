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

# def pow():
#     I = 10
#
#     def Power(things, I):
#         Pow = {'T [s]': [things.at[0, 'T [s]']], 'Px [W]': [things.at[0, 'Ux [V]'] * I],
#                'Py [W]': [things.at[0, 'Uy [V]'] * I]}
#         Pow = pd.DataFrame(data=Pow)
#
#         for i in range(1, things['T [s]'].size):
#             var = {'T [s]': [things.at[i, 'T [s]']], 'Px [W]': [things.at[i, 'Ux [V]'] * I],
#                    'Py [W]': [things.at[i, 'Uy [V]'] * I]}
#             var = pd.DataFrame(data=var)
#             Pow = pd.concat([Pow, var], ignore_index=True)
#         Pow = Pow.set_index(['T [s]'])
#         return print(Pow)
#
#     Power(things, I)
#
# def antyaliasing():
#     raw = pd.read_csv(r"C:\Users\pati\PycharmProjects\CTPApp\dane1.csv", sep='\t', header=0,
#                       decimal=',')  # wczytuje dane
#     things = raw
#     things['T [s]'] = things['T [s]'] - things.at[0, 'T [s]']
#
#     AA = {'T [s]': [things.at[0, 'T [s]']], 'Ux [V]': [things.at[0, 'Ux [V]']], 'Uy [V]': [things.at[0, 'Uy [V]']]}
#     AA = pd.DataFrame(data=AA)
#
#     for i in range(1, things['T [s]'].size):
#         var = {'T [s]': [(things.at[i - 1, 'T [s]'] + things.at[i, 'T [s]']) / 2, things.at[i, 'T [s]']],
#                'Ux [V]': [((things.at[i - 1, 'Ux [V]']) + (things.at[i, 'Ux [V]'])) / 2, things.at[i, 'Ux [V]']],
#                'Uy [V]': [((things.at[i - 1, 'Uy [V]']) + (things.at[i, 'Uy [V]'])) / 2, things.at[i, 'Uy [V]']]}
#         var = pd.DataFrame(data=var)
#         AA = pd.concat([AA, var], ignore_index=True)
#     df = AA
#     fig.clear()
#     init()


def open_calc_window():
    filename = fd.askopenfilename()
    df = pd.read_csv(filename, sep='\t', header=0, index_col=0, decimal=',')
    new = tkinter.Toplevel()
    new.title("calc")
    new.geometry("300x100")
    label = tkinter.Label(new, text="Podaj wartość U[V]", font=20, fg="black",anchor = 'w')
    label.pack(side=tkinter.RIGHT)

    def calc():
        val = float(e.get())
        v_max = 200.0
        f_max = 400.0
        max_from_df = df['Ux [V]'].max()
        min_from_df = df['Ux [V]'].min()
        max = max_from_df
        if (abs(min_from_df) > max_from_df):
            max = abs(min_from_df)

        value_to_calc_v = (v_max / max)*0.28
        value_to_calc_f = f_max / max
        res_v = value_to_calc_v * val
        res_f = value_to_calc_f * val
        new2 = tkinter.Toplevel(new)
        new2.title("Result")
        new2.geometry("1000x50")
        label2 = tkinter.Label(new2, text=" Wartość V[m/s] = " + str(res_v) + " Wartość F[kN] = " + str(res_f), font=20,
                               fg="black")
        label2.pack(side=tkinter.TOP)

    button_new = tkinter.Button(master=new, text="oblicz", command=calc)
    button_new.pack(side=tkinter.BOTTOM)
    e = tkinter.Entry(master=new, width=20)
    e.pack(side=tkinter.LEFT)




button = tkinter.Button(master=toolbar, image=photo, command=load)
button.pack(side="left")
menu_widget = tkinter.Menu(root)
submenu_widget = tkinter.Menu(menu_widget, tearoff=False)
menu_widget.add_command(label="Calc", command=open_calc_window)
# menu_widget.add_command(label="Antyaliasing", command=antyaliasing)
menu_widget.add_command(label="Item3", command=menu_callback)
root.config(menu=menu_widget)

tkinter.mainloop()
