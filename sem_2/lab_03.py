
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image


window = Tk()
window.geometry('240x100')
window.resizable(False, False)


global image_path


# -------------------------------------------------------------------------------------------------------------- #


# Функция для получения пути к файлу
def get_image_path():
    global image_path
    image_path = filedialog.askopenfilename(title='Select image',
                                            filetypes=(('png files', '*.png'), ('bmp files', '*.bmp')))


# Функция кодирует сообщения в изображение
def encode():
    global image_path

    message_bin = text_to_binary(message_entry.get() + '@')

    try:
        img = Image.open(image_path)
        width, height = img.size
        # required_pixels = (width * height) / 3
        # if len(message_bin) > required_pixels:
        #     messagebox.showerror('Error', 'Not enough space')
        index = 0
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0, 3):
                    if index < len(message_bin):
                        pixel_bin = list(bin(pixel[n]))[2:]
                        while len(pixel_bin) < 8:
                            pixel_bin += ['0']
                        pixel_bin[-1] = message_bin[index]
                        pixel_bin = ''.join(pixel_bin)
                        pixel[n] = int(pixel_bin, 2)
                        index += 1
                img.putpixel((x, y), tuple(pixel))
        if 'png' in image_path.split('/')[-1].lower():
            img.save('source_secret.png', 'PNG')
        else:
            img.save('source_secret.bmp', 'BMP')

    except NameError:
        messagebox.showerror('Error', 'Choose file')


# Функция раскодировывает сообщения из изображения
def extract():
    new_window = Toplevel(window)
    new_window.grab_set()
    new_window.focus_set()
    new_window.geometry('200x50')
    new_window['bg'] = '#000000'

    global image_path

    flag = 0
    stop = '@'
    message = ''

    try:
        img = Image.open(image_path)
        width, height = img.size
        last_bits = ''
        secret_message = []

        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0, 3):
                    last_bits += bin(pixel[n])[-1]
                    secret_bits = [last_bits[i:i+8] for i in range(0, len(last_bits), 8)]
                    secret_message = [chr(int(secret_bits[i], 2)) for i in range(len(secret_bits))]

                    if stop in secret_message:
                        flag = 1
            if flag:
                message = Label(new_window, text=''.join(secret_message[:secret_message.index(stop)]),
                                bg='#000000', fg='#ffffff', font=('Arial', 16, 'bold', 'italic'))
                message.pack()
                break
            else:
                new_window.destroy()
                messagebox.showinfo('Oops', 'No secret message')
                break

    except NameError:
        new_window.destroy()
        messagebox.showerror('Error', 'Choose file')


# Фукнция перевод строку в последовательность битов
def text_to_binary(value):
    return ''.join(f'{ord(i):08b}' for i in value)


# -------------------------------------------------------------------------------------------------------------- #


input_message = Label(window, text='Input message')
input_message.grid(row=0, column=0)

message_entry = Entry(window, width=15)
message_entry.grid(row=0, column=1)

encode_button = Button(window, text='Encode message', command=lambda: encode())
encode_button.grid(row=3, column=0, rowspan=2, padx=10, pady=10)

extract_button = Button(window, text='Extract message', command=lambda: extract())
extract_button.grid(row=3, column=1, rowspan=2, padx=10, pady=10)

choose_image = Button(window, text='Choose file', command=lambda: get_image_path())
choose_image.place(relx=0.5, rely=0.8, anchor=CENTER)

window.mainloop()
