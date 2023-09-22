from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

# Создание окна
window = Tk()

window.title('Calculator')
window.geometry('800x250')
window.resizable(False, False)

current_entry = None


# Функции для работы с виджетами

# -------------------------------------------------------------------------------------------------------------- #


# Фокусировка выбранного поля ввода
def on_focus(event):
    global current_entry
    current_entry = event.widget


# Кнопки клавиатуры
def button_click(number):
    if current_entry is not None:
        current_val = current_entry.get()
        current_entry.delete(0, END)
        current_entry.insert(0, str(current_val) + str(number))


# Удаление чисел
def button_delete():
    if current_entry is not None:
        current_entry.delete(current_entry.index("end") - 1)


# Клавиатура
def keyboard():
    new_window = Toplevel(window)
    new_window.title('Клавиатура')
    new_window.geometry('286x256')
    new_window.resizable(False, False)

    button1 = Button(new_window, text='1', padx=40, pady=20, command=lambda: button_click(1))
    button2 = Button(new_window, text='2', padx=40, pady=20, command=lambda: button_click(2))
    button3 = Button(new_window, text='3', padx=40, pady=20, command=lambda: button_click(3))
    button4 = Button(new_window, text='4', padx=40, pady=20, command=lambda: button_click(4))
    button5 = Button(new_window, text='5', padx=40, pady=20, command=lambda: button_click(5))
    button6 = Button(new_window, text='6', padx=40, pady=20, command=lambda: button_click(6))
    button7 = Button(new_window, text='7', padx=40, pady=20, command=lambda: button_click(7))
    button8 = Button(new_window, text='8', padx=40, pady=20, command=lambda: button_click(8))
    button9 = Button(new_window, text='9', padx=40, pady=20, command=lambda: button_click(9))
    button0 = Button(new_window, text='0', padx=40, pady=20, command=lambda: button_click(0))
    button_clear = Button(new_window, text='<---', padx=30, pady=20, command=button_delete)

    button1.grid(row=3, column=0)
    button2.grid(row=3, column=1)
    button3.grid(row=3, column=2)

    button4.grid(row=2, column=0)
    button5.grid(row=2, column=1)
    button6.grid(row=2, column=2)

    button7.grid(row=1, column=0)
    button8.grid(row=1, column=1)
    button9.grid(row=1, column=2)

    button0.grid(row=4, column=0,)
    button_clear.grid(row=4, column=1)


# Информация о программе и пользователе
def about_programme():
    new_window = Toplevel(window)
    new_window.title('About programme')
    new_window.resizable(False, False)
    text_about = Label(new_window,
                       text='Программа предназначена для выполнения операций '
                            'сложения и вычитания целых чисел имитируя восьмиразрядный сумматор.\n'
                            'Автор: Хотамов Умед\n'
                            'Группа: ИУ7-13Б',
                       font=('Arial', 16, 'bold', 'italic'),
                       bg='#99ffff',
                       fg='#808080')
    text_about.pack()


# Функция очистки полей
def clean(*text):
    for i in text:
        i.delete(0, END)


# Перевод отрицательного числа в обратный код
def reversed_code(num):
    arr = num[1:]
    reversed_list = list(map(lambda x: 0 if x == 1 else 1, arr))
    reversed_list = [1] + reversed_list
    return reversed_list


# Функция перевода в двоичную сс
def convert_to_bin(number):
    value = ''
    if number < 0:
        main_num = number * (-1)
    else:
        main_num = number
    while main_num > 0:
        value = str(main_num % 2) + value
        main_num = main_num // 2
    if number < 0:
        size = 7
        value = list(map(int, list(value)))
        value = [0] * (size - len(value)) + value
        print(value)
        return reversed_code([1] + value)
    else:
        size = 8
        value = list(map(int, list(value)))
        value = [0] * (size - len(value)) + value
        return value


# Функция перевод из двоичной сс в десятичную сс
def convert2_to_10(val):
    val_10 = 0
    _pow = len(val) - 1
    for num in val:
        val_10 += int(num) * (2 ** _pow)
        _pow -= 1
    return val_10


# Функция осуществляет реализацию восьмиразрядного сумматора
def add(a, b):
    H = a & b  # 4 for AND
    L = a | b  # 1
    NX = H | (~L)  # 2
    K = NX

    H = H | ~(K | ~(H << 1))  # 5
    K = K | (K << 1)  # 2

    H = H | ~(K | ~(H << 2))  # 5
    K = K | (K << 2)  # 2

    H = H | ~(K | ~(H << 4))  # 5

    carry = H << 1  # 1

    neg_res = NX ^ carry  # 7 for XOR
    res_mod_256 = ~(neg_res | -256)  # 2
    if convert_to_bin(res_mod_256)[0] == 1:
        return convert2_to_10(reversed_code(convert_to_bin(res_mod_256 - 1))[1::]) * (-1)
    else:
        return res_mod_256


# Функция выполняет сложение или вычитание в двух целых чиспел в зависимости от выбраной операции
def main_operator():
    res_entry.delete(0, END)
    operator = selector.get()
    try:
        x = is_valid(value1.get())
        y = is_valid(value2.get())
        if operator == 'Минус':
            y = y * (-1)
        else:
            pass
        res_entry.config(state='normal')
        res_entry.insert(0, add(x, y))
    except ValueError:
        messagebox.showerror('Ошибка ввода данных', 'Данные введены неверно\n'
                                                    'Проверьте корректность введеных данных!\n')
    except TypeError:
        pass


def operator_plus_menu():
    res_entry.delete(0, END)
    try:
        x = is_valid(value1.get())
        y = is_valid(value2.get())
        res_entry.config(state='normal')
        res_entry.insert(0, add(x, y))
    except ValueError:
        messagebox.showerror('Ошибка ввода данных', 'Данные введены неверно\n'
                                                    'Проверьте корректность введеных данных!\n')
    except TypeError:
        pass


def operator_minus_menu():
    res_entry.delete(0, END)
    try:
        x = is_valid(value1.get())
        y = is_valid(value2.get())
        y = y * (-1)
        res_entry.config(state='normal')
        res_entry.insert(0, add(x, y))
    except ValueError:
        messagebox.showerror('Ошибка ввода данных', 'Данные введены неверно\n'
                                                    'Проверьте корректность введеных данных!\n')
    except TypeError:
        pass


# -------------------------------------------------------------------------------------------------------------- #


def is_valid(value):
    value = int(value)
    try:
        if value not in range(-128, 128):
            raise ValueError
        return value
    except ValueError:
        messagebox.showinfo('Ввод данных', 'Проверьте корректность введеных данных\n'
                                           '(Введите целое число в диапазоне от -128 - 127)')


# Создание меню
menu_bar = Menu(window)
window.config(menu=menu_bar)

actions_menu = Menu(menu_bar, tearoff=0)
clean_menu = Menu(menu_bar, tearoff=0)
about_me = Menu(menu_bar, tearoff=0)

actions_menu.add_command(label='Плюс', command=lambda: operator_plus_menu())
actions_menu.add_command(label='Минус', command=lambda: operator_minus_menu())

clean_menu.add_command(label='Очистака первого поля', command=lambda: clean(value1))
clean_menu.add_command(label='Очистка второго поля', command=lambda: clean(value2))
clean_menu.add_command(label='Очистка всех полей', command=lambda: clean(value1, value2))

about_me.add_command(label='Информация об авторе', command=lambda: about_programme())

menu_bar.add_cascade(label='Заданные действия', menu=actions_menu)
menu_bar.add_cascade(label='Очистка полей', menu=clean_menu)
menu_bar.add_cascade(label='Помощь', menu=about_me)

# Заголовок
header = Label(window, text='Сложение и вычитание целых чисел с использованием восьмиразрядного сумматора',
               font=('Arial Bold', 15))

# Ввод чисел
value1_text = Label(window, text='Введите первое число:', font=('Arial Bold', 10))
value2_text = Label(window, text='Введите второе число:', font=('Arial Bold', 10))

value1 = Entry(window)
value1.bind('<FocusIn>', on_focus)
value2 = Entry(window)
value2.bind('<FocusIn>', on_focus)

# Кнопка вычисления
button_op = Button(window, text='Вычислить', width=15, height=2, command=main_operator)

# Кнопка для вызова клавиатуры
button_kb = Button(window, text='Клавиатура', width=15, height=1, command=keyboard)

# Выбор операции
selector = Combobox(window, values=['Плюс', 'Минус'], state='readonly')
selector.current(0)
