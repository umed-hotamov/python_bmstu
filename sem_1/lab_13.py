import struct


# Функция проверки на дурака чисел с плавающей точкой
def float_check(a):
    right_float = False
    if len(a) == 0:
        return None
    # Проверка чисел вида (-)1
    elif a.isdigit() or (a[0] == '-' and a[1:].isdigit()):
        right_float = True
    elif a == '-' or a == '+' or (a[0] == '-' and a[1].isdigit() == False):
        return None
    else:
        # Счёт нужных и не очень символов
        counter_e = points = minus = plus = others = 0
        e_place = plus_place = minus_place = float('inf')
        for i in range(len(a)):
            # Проверка, для того чтобы переменная others не учитывала числа
            if a[i].isdigit():
                pass
            # Счётчик символов e
            elif a[i] == 'e':
                counter_e += 1
                e_place = i
            # Счётчик плюсов
            elif a[i] == '+':
                plus += 1
                plus_place = i
            # Счётчик минусов
            elif a[i] == '-':
                minus += 1
                minus_place = i
            # Счётчик точек
            elif a[i] == '.':
                points += 1
                point_place = i
            # Счётчик посторонних символов
            else:
                others += 1
        # Проверка на посторонние символы
        if others > 0:
            return None
        # Проверки чисел вида (-)1e(+/-)(0)6
        elif counter_e == 1 and plus <= 1 and minus <= 2 and points <= 1:
            if points == 1:
                if plus == 1 and e_place + 1 == plus_place:
                    return None
                elif plus == 1 and minus == 1 and a[0] != '-':
                    return None
                elif minus == 2 and a[0] != '-':
                    return None
                elif e_place + 1 == minus_place or e_place + 1 == plus_place:
                    right_float = True
                elif a[0] == '-' and minus == 1:
                    right_float = True
                elif a[e_place + 1].isdigit():
                    if (minus == 1 and a[0] == '-') or (minus == 0):
                        right_float = True
                else:
                    return None
            elif plus == 1 and e_place + 1 != plus_place:
                return None
            elif (plus == 1 and minus == 1 and a[0] != '-') or (minus == 2 and a[0] != '-'):
                return None
            elif e_place + 1 == plus_place or e_place + 1 == minus_place:
                right_float = True
            elif minus == 1 and a[0] == '-':
                right_float = True
            elif a[e_place + 1].isdigit():
                if (minus == 1 and a[0] == '-') or (minus == 0):
                    right_float = True
            elif point_place > e_place:
                return None
        # Проверки чисел вида (-)1.2
        elif points == 1 and plus == 0 and minus <= 1:
            b = a.replace('.', '0', 1)
            if minus == 1 and a[0] != '-':
                return None
            elif minus == 1:
                b = b.replace('-', '0', 1)
                if b.isdigit():
                    right_float = True
                else:
                    return None
            elif b.isdigit():
                right_float = True
            else:
                return None
        else:
            return None

    # Вывод числа в виде float или inf
    if right_float:
        if float(a) == int(float(a)):
            return int(float(a))
        return float(a)
    return None


# Функция проверки на дурака целых чисел
def int_check(a):
    int_a = float_check(a)
    if (int_a is not None) and (int_a % 1 == 0):
        return int_a
    else:
        return None


note_len = 66
byte_format = '<30s30slh'


# Функция проверки на нашу базу данных
def if_data_base(name):
    try:
        file = open(name, 'rb')
    except UnicodeDecodeError:
        return False
    else:
        string = file.readline()
        file.seek(0, 2)
        file_size = file.tell()
        if file_size % note_len == 0:
            file.close()
            return True
        else:
            file.close()
            return False


# Функция по вводу названия мебели с проверкой
def furn_name(s: str):
    while True:
        furn = input(s)
        if len(furn) > 15:
            print('Слишком длинное название')
            continue
        else:
            if furn[0].isupper():
                return furn


# Функция по вводу названия цвета с проверкой
def color_name(s: str):
    while True:
        color = input(s)
        if len(color) > 15:
            print('Слишком длинное название')
            continue
        else:
            if color[0].isupper():
                return color


# Функция по вводу цены с проверкой
def price_name(s: str):
    while True:
        price = input(s)
        if len(price) > 15:
            print('Слишком длинное название')
            continue
        else:
            if price.isdigit():
                return int(price)


# Функция по кол-во отзывов с проверкой
def review_name(s: str):
    while True:
        reviews = input(s)
        if len(reviews) > 15:
            print('Слишком большое значение')
            continue
        else:
            if reviews.isdigit() and reviews != 0:
                return int(reviews)


# Функция выбора файла
def choose_file():
    while True:
        name = input('Введите название файла: ')
        if name is None:
            print('Неподдерживаемый тип файлов\n')
            continue
        else:
            break
    try:
        file = open(name, 'rb')
    except FileNotFoundError:
        try:
            file = open(name, 'wb')
        except PermissionError:
            print('Ошибка доступа')
        else:
            file.close()
            right_data_base = if_data_base(name)
            existence = True
            return name, existence, right_data_base
    except PermissionError:
        print('Ошибка доступа')
    else:
        file.close()
        right_data_base = if_data_base(name)
        existence = True
        return name, existence, right_data_base
    return '', False, False


# Функция инициализации файла
def initialize_file(name):
    try:
        file = open(name, 'wb')
    except:
        print('Ошибка инициализации файла')
    file.close()


# Функция считывания файла
def read_file(name):
    print()
    file = open(name, 'rb')
    file.seek(0, 2)
    file_size = file.tell()
    file.seek(0)
    string_size = file_size / note_len
    if string_size > 0:
        print('-' * 65)
        print('|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Название', 'Цвет', 'Цена, руб', 'Кол-во отзывов'))
        print('-' * 65)
        string = file.read(note_len)
        note = [0, 0, 0, 0]
        while string != b'':
            allnote = struct.unpack(byte_format, string)
            note[0] = allnote[0].decode('utf-8').strip().replace('\x00', '')
            note[1] = allnote[1].decode('utf-8').strip().replace('\x00', '')
            note[2], note[3] = allnote[2], allnote[3]
            print(('|{:^15}|{:^15}|{:^15}|{:^15}|').format(note[0], note[1], note[2], note[3]))
            string = file.read(note_len)
        print('-' * 65)
    else:
        print('Файл пуст')
    file.close()


# Функция добавления новой записи
def new_note(name):
    file = open(name, 'ab')
    note = [0, 0, 0, 0]
    note[0] = furn_name('Введите название мебели с большой буквы: ')
    note[1] = color_name('Введите цвет мебели с большой буквы: ')
    note[2] = price_name('Введите цену мебели: ')
    note[3] = review_name('Введите кол-во отзывов: ')
    note[0] = note[0].strip().encode('utf-8')
    note[1] = note[1].strip().encode('utf-8')
    bytes_note = struct.pack(byte_format, note[0], note[1], note[2], note[3])
    file.write(bytes_note)
    file.close()


# Функция по выбору поля
def choose_field():
    print(
        'Выберите по какому(-им) полю(-ям) вы хотите найти запись:',
        ' 1 - Название мебели',
        ' 2 - Цвет',
        ' 3 - Цена',
        ' 4 - Кол-во отзывов',
        sep='\n'
    )
    while True:
        field = int_check(input('Введите пункт: '))
        if field is None or field > 4 or field < 1:
            print('>> Вы не выбрали пункт из списка')
            print()
            continue

        if field == 1:
            return furn_name('Введите название мебели с большой буквы: '), 0
        if field == 2:
            return color_name('Введите цвет мебели с большой буквы: '), 1
        if field == 3:
            return price_name('Введите цену мебели: '), 2
        if field == 4:
            return review_name('Введите кол-во отзывов: '), 3


# Функция получения номера удаляемой записи
def get_number():
    file = open(name, 'rb')
    file.seek(0, 2)
    file_size = file.tell()
    string_size = file_size / note_len
    if string_size == 0:
        return False
    while True:
        number = int_check(input('Введите номер удаляемой строки: '))
        if number is None:
            continue
        if number <= 0 or number > string_size:
            print('Номер выходит за пределы базы данных\n')
            continue
        else:
            file.close()
            return number


# Функция удаления записи
def delete_note(name):
    file = open(name, 'r+b')
    number = get_number()
    if number == False:
        print('Файл пуст')
        file.close()
    else:
        file.seek(number * note_len)
        stay = file.read()
        file.seek((number - 1) * note_len)
        file.write(stay)
        file.truncate()
        file.close()


# Функция нахождения записи по одному полю
def find_note_by_1(name, field, index):
    pass
    print()
    file = open(name, 'rb')
    file.seek(0, 2)
    file_size = file.tell()
    file.seek(0)
    string_size = file_size / note_len
    if string_size > 0:
        field_exist = False
        print('-' * 65)
        print('|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Название', 'Цвет', 'Цена, руб', 'Кол-во отзывов'))
        print('-' * 65)
        string = file.read(note_len)
        note = [0, 0, 0, 0]
        while string != b'':
            allnote = struct.unpack(byte_format, string)
            note[0] = allnote[0].decode('utf-8').strip().replace('\x00', '')
            note[1] = allnote[1].decode('utf-8').strip().replace('\x00', '')
            note[2], note[3] = allnote[2], allnote[3]
            if note[index] == field:
                print(('|{:^15}|{:^15}|{:^15}|{:^15}|').format(note[0], note[1], note[2], note[3]))
                field_exist = True
            string = file.read(note_len)
        print('-' * 65)
        if not field_exist:
            print('Поля не были найдены')
    else:
        print('Файл пуст')
    file.close()


# Функция нахождения записи по двум полям
def find_note_by_2(name, field_1, field_2, index_1, index_2):
    print()
    file = open(name, 'rb')
    file.seek(0, 2)
    file_size = file.tell()
    file.seek(0)
    string_size = file_size / note_len
    if string_size > 0:
        field_exist = False
        print('-' * 65)
        print('|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Название', 'Цвет', 'Цена, руб', 'Кол-во отзывов'))
        print('-' * 65)
        string = file.read(note_len)
        note = [0, 0, 0, 0]
        while string != b'':
            allnote = struct.unpack(byte_format, string)
            note[0] = allnote[0].decode('utf-8').strip().replace('\x00', '')
            note[1] = allnote[1].decode('utf-8').strip().replace('\x00', '')
            note[2], note[3] = allnote[2], allnote[3]
            if note[index_1] == field_1 and note[index_2] == field_2:
                print(('|{:^15}|{:^15}|{:^15}|{:^15}|').format(note[0], note[1], note[2], note[3]))
                field_exist = True
            string = file.read(note_len)
        print('-' * 65)
        if not field_exist:
            print('Поля не были найдены')
    else:
        print('Файл пуст')
    file.close()


existence = False
# Выводим на экран все доступные команды
while True:
    print()
    print(
        ' 1) Выбрать файл для работы',
        ' 2) Инициализировать базу данных',
        ' 3) Вывести содержимое базы данных',
        ' 4) Добавить запись в базу данных',
        ' 5) Удалить запись из базы данных (по номеру в файле)',
        ' 6) Поиск по одному полю',
        ' 7) Поиск по двум полям',
        ' 0) Прекратить работу программы',
        sep='\n'
    )
    print()

    # Просим пользователя ввести номер команды и проверяем ввёл ли пользователь нужное число
    command = int_check(input('Введите номер команды: '))
    if command is None or command > 7 or command < 0:
        print('Вы не выбрали номер команды из списка')
        print('Повторите попытку')
        print()
        continue

    if not existence and command != 1 and command != 0:
        print('Выберите файл для работы')
        print()
        continue

    # Выполняем команду по выбору файла
    if command == 1:
        name, existence, right_data_base = choose_file()
        # name, existence = 'Мебель тест.txt', True
        if existence:
            print('Файл был выбран')

    # Выполняем команду по инициализации базы данных
    if command == 2:
        initialize_file(name)
        right_data_base = True
        print('База данных была инициализирована')
    # Выполняем команду по выводу содержимого файла
    if command == 3:
        if right_data_base:
            read_file(name)
        else:
            print('Файл не является базой данных, пожалуйста инициализируйте его')
    # Выполняем команду по добавление новой записи
    if command == 4:
        if right_data_base:
            new_note(name)
        else:
            print('Файл не является базой данных, пожалуйста инициализируйте его')
    if command == 5:
        if right_data_base:
            delete_note(name)
        else:
            print('Файл не является базой данных, пожалуйста инициализируйте его')
    # Выполняем команду по поиску записи по одному полю
    if command == 6:
        if right_data_base:
            # Вводим поле
            field, index = choose_field()
            # Ищем строки с данными значениями поля
            find_note_by_1(name, field, index)
        else:
            print('Файл не является базой данных, пожалуйста инициализируйте его')
    # Выполняем команду по поиску записи по двум полям
    if command == 7:
        if right_data_base:
            # Вводим первое поле
            field_1, index_1 = choose_field()
            # Вводим второе поле
            while True:
                field_2, index_2 = choose_field()
                if index_2 == index_1:
                    print('Выберите пожалуйста разные поля')
                    continue
                else:
                    break
            # Ищем строки с данными значениями полей
            find_note_by_2(name, field_1, field_2, index_1, index_2)
        else:
            print('Файл не является базой данных, пожалуйста инициализируйте его')

    # Выполняем комманду по заершению работы программы
    if command == 0:
        exit(-1)

