import tkinter as tk

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import random

from tkinter import *
from tkinter import ttk

from math import *


window = Tk()

window.title('Chord method')
window.geometry('600x300')
window['bg'] = '#33ffcc'
window.resizable(False, False)

matplotlib.use('TkAgg')


# --------------------------------------------------------------------------------------------- #


def about_programme():
    new_window = Toplevel(window)
    new_window.title('About programme')
    new_window.resizable(False, False)
    text_about = Label(new_window,
                       text='Программа предназначена для вычисления корней функции '
                            'методом Хорд.\n'
                       font=('Arial', 16, 'bold', 'italic'),
                       bg='#99ffff',
                       fg='#808080')
    text_about.pack()


def f(func: str, x):
    return eval(func)


def make_table():
    new_window = Toplevel(window)
    new_window.title('Построение таблицы')
    new_window.grab_set()
    new_window.focus_set()

    try:
        func = func_entry.get()
        f(func, random.random())
        a = float(start.get())
        b = float(end.get())
        h = float(step.get())
        eps = float(tolerable_error.get())
        max_iterations = int(max_iter.get())
    except:
        tk.messagebox.showinfo(message='Invalid field values, try again')
        new_window.destroy()

    scroll = Scrollbar(new_window)
    table = ttk.Treeview(new_window, yscrollcommand=scroll.set, xscrollcommand=scroll.set)
    figure = plt.figure()
    canvas = FigureCanvasTkAgg(figure, new_window)
    canvas.get_tk_widget().pack_forget()
    figure.clear()

    scroll.pack_forget()
    table.pack_forget()


    for i in table.get_children():
        table.delete(i)
    new_window.update()

    scroll.pack(side=RIGHT, fill=Y)
    table.pack(fill=BOTH)

    scroll.config(command=table.xview)
    scroll.config(command=table.yview)

    table['columns'] = ('n', 'interval', 'x', 'f', 'iterations', 'error')

    table.column("#0", width=0, stretch=NO)
    table.column("n", width=50, anchor=CENTER)
    table.column("interval", anchor=CENTER, width=250)
    table.column("x", anchor=CENTER, width=120)
    table.column("f", anchor=CENTER, width=120)
    table.column("iterations", anchor=CENTER, width=80)
    table.column("error", anchor=CENTER, width=50)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("n", text="n", anchor=CENTER)
    table.heading("interval", text="[xi, xi+1]", anchor=CENTER)
    table.heading("x", text="x'", anchor=CENTER)
    table.heading("f", text="f(x')", anchor=CENTER)
    table.heading("iterations", text="iterations", anchor=CENTER)
    table.heading("error", text="error", anchor=CENTER)

    axis1 = figure.add_subplot(1, 1, 1)

    x = np.linspace(a, b, 100)
    y = []
    for xi in x:
        y.append(f(func, xi))
    y = np.array(y)

    axis1.plot(x, y)

    increase = y[1] >= y[0]
    extremum = []
    for i, point in enumerate(y[1:]):
        if point >= y[i] and not increase:
            extremum.append((x[i], y[i]))
            increase = True
        elif point <= y[i] and increase:
            extremum.append((x[i], y[i]))
            increase = False

    extremum = np.array(extremum)
    if len(extremum) != 0:
        axis1.scatter(extremum[:, 0], extremum[:, 1], marker='o', color='red', label='extremum')

    flag = None
    inflection = []
    for i, point in enumerate(list(zip(x, y))[2:]):
        v = (x[i + 1] - x[i]) * (y[i + 1] - point[1]) - (y[i + 1] - y[i]) * (x[i + 1] - point[0])
        if flag is None or (v > 0 and flag):
            if flag is not None:
                inflection.append((x[i + 1], y[i + 1]))
            flag = v < 0

        if flag is None or (v < 0 and not flag):
            if flag is not None:
                inflection.append((x[i + 1], y[i + 1]))
            flag = v < 0

    inflection = np.array(inflection)
    if len(inflection) != 0:
        axis1.scatter(inflection[:, 0], inflection[:, 1], marker=',', color='green', label='inflection')

    i = 0
    roots = []
    count = 0
    while a + h * (i + 1) <= b + h:
        left = a + h * i
        right = a + h * (i + 1)

        prev_x = right
        current_x = left
        if f(func, right) * f(func, left) > 0:
            i += 1
            continue

        iterations = 0
        no_roots = False
        error_code = 0
        while abs(current_x - prev_x) > eps:
            current_y = f(func, current_x)
            prev_y = f(func, prev_x)
            if abs(current_y - prev_y) == 0:
                no_roots = True
                error_code = 1
                break

            next_x = current_x - ((current_x - prev_x) / (current_y - prev_y)) * f(func, current_x)

            prev_x = current_x
            current_x = next_x

            iterations += 1
            if iterations > max_iterations:
                no_roots = True
                error_code = 2
                break

        if not left <= current_x <= right:
            error_code = 3
            no_roots = True

        if not no_roots:
            if len(roots) != 0 and current_x - roots[-1] < eps:
                count += 1
                error_code = 4
                values = (count, f'[{left:.3f}, {right:.1g}]', '', '', iterations, error_code)
                table.insert(parent='', index='end', iid=str(i), values=values)
            else:
                count += 1
                roots.append(current_x)
                values = (count, f'[{left:.3f}, {right:.3f}]',
                          f'{current_x:.7f}',
                          f'{f(func, current_x):.1g}',
                          iterations,
                          error_code)
                table.insert(parent='', index='end', iid=str(i), values=values)
        else:
            values = (count, f'[{left:.3f}, {right:.1g}]', '', '', iterations, error_code)
            table.insert(parent='', index='end', iid=str(i), values=values)

        i += 1

        roots = np.array(roots)
        values = []
        for root in roots:
            values.append(f(func, root))
        values = np.array(values)

        if len(roots) != 0:
            axis1.scatter(roots, values, marker='^', color='black', label='roots')
        axis1.legend()

        canvas.draw()
        canvas.get_tk_widget().pack(padx=100)


# --------------------------------------------------------------------------------------------- #


main_menu = Menu(window)
about_me = Menu(main_menu, tearoff=0)

about_me.add_command(label='Информация об авторе', command=about_programme)
main_menu.add_cascade(label='Справка', menu=about_me)

window.config(menu=main_menu)

func_txt = Label(window, text='Функция f(x):', font=('Arial Bold', 12))
start_txt = Label(window, text='Левая граница отрезка:', font=('Arial Bold', 12))
end_txt = Label(window, text='Правая граница отрезка:', font=('Arial Bold', 12))
step_txt = Label(window, text='Шаг:', font=('Arial Bold', 12))
max_iter_txt = Label(window, text='Макс. количество итераций:', font=('Arial Bold', 12))
tolerable_error_txt = Label(window, text='Введите точность:', font=('Arial Bold', 12))

button_calc = Button(window, text='Вычислить', width=15, height=1, command=make_table)

func_entry = Entry(window)
start = Entry(window)
end = Entry(window)
step = Entry(window)
max_iter = Entry(window)
tolerable_error = Entry(window)

func_txt.place(x=40, y=50)
func_entry.place(x=300, y=54)

start_txt.place(x=40, y=80)
start.place(x=300, y=85)

end_txt.place(x=40, y=111)
end.place(x=300, y=116)

step_txt.place(x=40, y=139)
step.place(x=300, y=143)

tolerable_error_txt.place(x=40, y=165)
tolerable_error.place(x=300, y=170)

max_iter_txt.place(x=40, y=194)
max_iter.place(x=300, y=199)

button_calc.place(x=40, y=240)

window.mainloop()

