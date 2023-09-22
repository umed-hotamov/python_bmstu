# Меню
def menu():
    print('           Меню             ')
    print('1) Выбрать файл для работы')
    print('2) Инициализировать базу данных')
    print('3) Вывести содержимое базы данных')
    print('4) Добавить запись в базу данных')
    print('5) Поиск по одному полю')
    print('6) Поиск по двум полям')
    print('0) Завершить работу программы')


input_file = None


# Выбор файла для работы
def pick_file():
    while True:
        try:
            filename = input('Введите путь к файлу: ')
            file = open(filename)
            file.close()
            print()
            return filename
        except IOError:
            print('Файл не найден!')
            print()
            break


# Создание и инициализация файла
def record_file():
    flag = 0
    path = input("Введите путь к файлу: ")
    try:
        if os.path.exists(path):
            # print("Перезапись существующего файла...")
            # os.remove(path)
            flag = 1

        # file = open(path, 'w+')
        # file.close()
    except IOError:
        print('Файл не найден')
    if flag == 1:
        os.remove(path)
        print("Перезапись существующего файла...")
        print()
    else:
        try:
            file = open(path, 'w+')
            print('Создание нового файла...')
            file.close()
            print()
        except IOError:
            print('Файл не найден')
            print()


# Вывод содержимого файла
def output_file(f):
    if f is not None:
        if os.path.getsize(f) != 0:

            try:
                file = open(f, 'r')
                file_open = file.read()
                print(file_open)
                print()
                file.close()
            except UnicodeDecodeError:
                print('Невозможно открыть файл')
                print()
        else:
            print('Файл пуст')
            print()
    else:
        print('Выберите файл для работы')
        print()


# Добавление записей
def add_record(f):
    if f is not None:
        try:
            flag = 0
            file = open(f, 'r+')
            for line in file:
                if '№ 11111' in line:
                    flag = 1
            if flag == 1:
                n = input('Введите количество добавляемых клиентов: ')
                while len(n) > 1 or not n.isdigit():
                    print('Количество добавляемых клиентов не должно быть целым числом и больше 9!')
                    n = input('Введите количество добавляемых клиентов: ')
                n = int(n)
                for j in range(n):
                    client_num = input(f'Введите номер {j + 1} - го клиента: ')
                    while len(client_num) != 2 or not client_num.isdigit():
                        print('Номер клиента должен сожержать 2 знака - числа')
                        client_num = input(f'Введите номер {j + 1} - го клиента: ')
                    name = input('Введите имя клиента: ')
                    while len(name) < 2 or len(name) > 6 or name.isdigit():
                        print(
                            'Имя клиента должно содержать от 2 до 6 знаков и не должно содержать числа')
                        name = input('Введите имя клиента: ')
                    if len(name) == 2:
                        name = name + '    '
                    elif len(name) == 3:
                        name = name + '   '
                    elif len(name) == 4:
                        name = name + '  '
                    elif len(name) == 5:
                        name = name + ' '
                    surname = input('Введите фамилию клиента: ')
                    while len(surname) < 3 or len(surname) > 8 or surname.isdigit():
                        surname = input(print(
                            'Фамилия клиента должна содержать от 3 до 8 знаков и не должна содержать числа'))
                        surname = input('Введите фамилию клиента: ')
                    if len(surname) == 3:
                        surname += '     '
                    elif len(surname) == 4:
                        surname += '    '
                    elif len(surname) == 5:
                        surname += '   '
                    elif len(surname) == 6:
                        surname = surname + '  '
                    elif len(surname) == 7:
                        surname = surname + ' '
                    money = input('Введите сумму: ')
                    while len(money) > 4 or len(money) < 2 or not money.isdigit():
                        print('Сумма клиента должна содержать от 2 до 4 знаков ')
                        money = input('Введите сумму: ')
                        print()
                    file.write(f'\n|       {client_num}                   |    {name}      | {surname}       |       {money}            |')
                    file.write('\n|--------------------------------------------------------------------------------------|')
                    print()
            else:
                if os.path.getsize(f) == 0:
                    file.write(f'|--------------------------------------------------------------------------------------|')
                    file.write(f'\n|				                     № 11111				                           |')
                    file.write(f'\n|--------------------------------------------------------------------------------------|')
                    file.write(
                        f'\n|   Номер клиента            |	  Имя         | Фамилия        |         Сумма         |')
                    file.write(
                        f'\n|--------------------------------------------------------------------------------------|')
                    n = input('Введите количество добавляемых клиентов: ')
                    while len(n) > 1 or not n.isdigit():
                        print('Количество добавляемых клиентов не должно быть целым числом и больше 9!')
                        n = input('Введите количество добавляемых клиентов: ')
                    n = int(n)
                    for j in range(n):
                        client_num = input(f'Введите номер {j + 1} - го клиента: ')
                        while len(client_num) != 2 or not client_num.isdigit():
                            print('Номер клиента должен сожержать 2 знака - числа')
                            client_num = input(f'Введите номер {j + 1} - го клиента: ')
                        name = input('Введите имя клиента: ')
                        while len(name) < 2 or len(name) > 6 or name.isdigit():
                            print('Имя клиента должно содержать от 2 до 6 знаков и не должно содержать числа')
                            name = input('Введите имя клиента: ')
                        if len(name) == 2:
                            name = name + '    '
                        elif len(name) == 3:
                            name = name + '   '
                        elif len(name) == 4:
                            name = name + '  '
                        elif len(name) == 5:
                            name = name + ' '
                        surname = input('Введите фамилию клиента: ')
                        while len(surname) < 3 or len(surname) > 8 or surname.isdigit():
                            print('Фамилия клиента должна содержать от 3 до 8 знаков и не должна содержать числа')
                            surname = input('Введите фамилию клиента: ')
                        if len(surname) == 3:
                            surname += '     '
                        elif len(surname) == 4:
                            surname += '    '
                        elif len(surname) == 5:
                            surname += '   '
                        elif len(surname) == 6:
                            surname = surname + '  '
                        elif len(surname) == 7:
                            surname = surname + ' '
                        money = input('Введите сумму: ')
                        while len(money) > 4 or len(money) < 2 or not money.isdigit():
                            print('Сумма клиента должна содержать от 2 до 4 знаков ')
                            money = input('Введите сумму: ')
                        file.write(f'\n|       {client_num}                   |    {name}      | {surname}       |       {money}            |')
                        file.write('\n|--------------------------------------------------------------------------------------|')
                        print()
                    file.close()
                else:
                    print('Инициализируйте файл')
                    print()
        except UnicodeDecodeError:
            print('Невозможно открыть файл')
            print()
    else:
        print('Выберите файл для работы в пункте 1')
        print()


# Поиск по одному полю
def field_1(f):
    if f is not None:
        file = open(f, 'r')
        flag = 0
        for line in file:
            if '№ 11111' in line:
                flag = 1
        file.close()
        if flag:
            print('"Поиск по номеру клиента"')
            print()
            file = open(f, 'r')
            v = 0
            flag1 = 0
            client_num = input(f'Введите номер клиента: ')
            while len(client_num) != 2 or not client_num.isdigit():
                print('Номер клиента должен сожержать 2 знака')
                client_num = input(f'Введите номер клиента: ')
            for line in file:
                i = line.split()
                if client_num in i:
                    v = line
                    print(v)
                    flag1 = 1

            if flag1 == 0:
                print(f'Клиента с номером {client_num} нет в базе данных')
                print()
            file.close()
        else:
            print('Выберите базу данных')
            print()
    else:
        print('Выберите файл для работы в пункте 1')
        print()


# Поиск по двум полям
def field_2(f):
    if f is not None:
        file = open(f, 'r')
        flag = 0
        for line in file:
            if '№ 11111' in line:
                flag = 1
        file.close()
        if flag:
            print('"Поиск по номеру и имени клиента"')
            print()
            file = open(f, 'r')
            client_num = input(f'Введите номер клиента: ')
            while len(client_num) != 2 or not client_num.isdigit():
                print('Номер клиента должен сожержать 2 знака')
                client_num = input(f'Введите номер клиента: ')
            name = input('Введите имя клиента: ')
            while len(name) < 1 or len(name) > 6 or name.isdigit():
                print('Имя клиента должно содержать от 2 до 6 знаков и не должно содержать числа и специальные символы')
                name = input('Введите имя клиента: ')
            print()
            v = 0
            flag1 = 0
            for line in file:
                i = line.split()
                if client_num in i and name in i:
                    v = line
                    print(v)
                    flag1 = 1

            if flag1 == 0:
                print(f'Клиента нет в базе данных')
                print()
            file.close()
        else:
            print('Выберите базу данных')
            print()
    else:
        print('Выберите файл для работы в пункте 1')
        print()


while True:
    menu()
    print()
    menu_command = input('Введите команду меню: ')
    while not menu_command.isdigit():
        menu_command = input('Введите команду меню: ')
    else:
        menu_command = int(menu_command)

    if menu_command == 1:
        input_file = pick_file()

    elif menu_command == 2:
        record_file()

    elif menu_command == 3:
        output_file(input_file)

    elif menu_command == 4:
        add_record(input_file)

    elif menu_command == 5:
        field_1(input_file)

    elif menu_command == 6:
        field_2(input_file)

    elif menu_command == 0:
        exit(-1)
