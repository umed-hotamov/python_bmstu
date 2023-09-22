from tkinter import *
from tkinter import messagebox

window = Tk()
window.resizable(False, False)


point_x_coordinates = []
point_y_coordinates = []
circle_centre_x_coordinates = []
circle_centre_y_coordinates = []
circle_radius = []


def bind_paint_dot():
    canvas.bind('<Button-1>', draw_dot)


def bind_paint_circle():
    R = radius_entry.get()
    canvas.bind('<Button-1>', draw_circle)


def insert_dot():
    try:
        x = int(dot_x_entry.get())
        y = int(dot_y_entry.get())
        point_x_coordinates.append(x)
        point_y_coordinates.append(y)
        x0 = x - 0.5
        y0 = y - 0.5
        x1 = x + 0.5
        y1 = y + 0.5
        canvas.create_oval(x0, y0, x1, y1, fill="black", width=5)
    except ValueError:
        messagebox.showerror('Value Error', 'Please, input int values!')


def insert_circle():
    try:
        x = int(circle_x_entry.get())
        y = int(circle_y_entry.get())
        R = int(radius_entry.get())
        circle_centre_x_coordinates.append(x)
        circle_centre_y_coordinates.append(y)
        circle_radius.append(R)
        R = int(radius_entry.get())
        x0 = x - R
        y0 = y - R
        x1 = x + R
        y1 = y + R
        canvas.create_oval(x0, y0, x1, y1)
    except ValueError:
        messagebox.showerror('Value error', 'Please, input int values!')


def draw_dot(event):
    point_x_coordinates.append(event.x)
    point_y_coordinates.append(event.y)
    x0 = event.x - 0.5
    y0 = event.y - 0.5
    x1 = event.x + 0.5
    y1 = event.y + 0.5
    canvas.create_oval(x0, y0, x1, y1, fill="black", width=6)


def draw_circle(event):
    try:
        R = int(radius_entry.get())
        circle_radius.append(R)
        circle_centre_x_coordinates.append(event.x)
        circle_centre_y_coordinates.append(event.y)
        x0 = event.x - R
        y0 = event.y - R
        x1 = event.x + R
        y1 = event.y + R
        canvas.create_oval(x0, y0, x1, y1)
    except ValueError:
        messagebox.showinfo('Help', 'Input radius (int type), before painting circle')


def find_circle():
    min_value = float('+inf')
    number_of_dot = (len(point_x_coordinates) + len(point_y_coordinates)) // 2
    dots_out_of_circle = number_of_dot
    index = 0
    for i in range(0, len(circle_radius)):
        counter = 0
        for j in range(number_of_dot):
            if (point_x_coordinates[j] - circle_centre_x_coordinates[i])**2 + (point_y_coordinates[j] - circle_centre_y_coordinates[i])**2 <= circle_radius[i]**2:
                counter += 1
                dots_out_of_circle -= 1
        if counter < min_value:
            min_value = counter
            index = i

    return circle_centre_x_coordinates[index], circle_centre_y_coordinates[index], circle_radius[index], dots_out_of_circle


def main():
    x, y, R, dots_out_of_circle = find_circle()
    if dots_out_of_circle == 0:
        messagebox.showerror('Error', 'No points out of circle')
    else:
        canvas.delete('all')
        x0 = x - R
        y0 = y - R
        x1 = x + R
        y1 = y + R
        canvas.create_oval(x0, y0, x1, y1)
        point_x_coordinates.clear()
        point_y_coordinates.clear()


leftFrame = Frame()
rightFrame = Frame()
bottomFrame = Frame()

dotLabel = Label(leftFrame, text='Point coordinates')
dot_x_label = Label(leftFrame, text='x')
dot_y_label = Label(leftFrame, text='y')
dot_x_entry = Entry(leftFrame, width=4)
dot_y_entry = Entry(leftFrame, width=4)
paint_dot_button = Button(leftFrame, text='Paint point', command=bind_paint_dot)

dotLabel.grid(row=0, column=0, columnspan=4)
dot_x_label.grid(row=1, column=0)
dot_y_label.grid(row=2, column=0)
dot_x_entry.grid(row=1, column=1)
dot_y_entry.grid(row=2, column=1)
paint_dot_button.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

leftFrame.pack(side=LEFT)

circleLabel = Label(rightFrame, text='Circle coordinates')
circle_x_label = Label(rightFrame, text='x')
circle_y_label = Label(rightFrame, text='y')
circle_x_entry = Entry(rightFrame, width=4)
circle_y_entry = Entry(rightFrame, width=4)
radius_label = Label(rightFrame, text='R')
radius_entry = Entry(rightFrame, width=4)
paint_circle_button = Button(rightFrame, text='Paint circle', command=bind_paint_circle)


circleLabel.grid(row=0, column=0, columnspan=4)
circle_x_label.grid(row=1, column=0)
circle_y_label.grid(row=2, column=0)
circle_x_entry.grid(row=1, column=1)
circle_y_entry.grid(row=2, column=1)
radius_label.grid(row=3, column=0)
radius_entry.grid(row=3, column=1)
paint_circle_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

rightFrame.pack(side=RIGHT)

canvas = Canvas(bottomFrame, width=700, height=350, background="white")
canvas.grid(row=0, column=0)


dotButton = Button(bottomFrame, text='Insert point', command=insert_dot)
circleButton = Button(bottomFrame, text='Insert circle', command=insert_circle)
get_result = Button(bottomFrame, text='Find circle', command=main)
dotButton.grid(row=1, column=0)
circleButton.grid(row=2, column=0)
get_result.grid(row=3, column=0)

bottomFrame.pack()

window.mainloop()
