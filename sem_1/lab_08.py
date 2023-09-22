def menu():
    print('|---------------------------------------------------------------------------------------------|')
    print('|                                            Меню                                             |')
    print('|---------------------------------------------------------------------------------------------|')
    print('| 1.  Ввести матрицу                                                                          |')
    print('| 2.  Добавить строку                                                                         |')
    print('| 3.  Удалить строку                                                                          |')
    print('| 4.  Добавить столбец                                                                        |')
    print('| 5.  Удалить столбец                                                                         |')
    print('| 6.  Найти строку, c наибольшим количеством повторяющихся элементов                          |')
    print('| 7.  Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов|')
    print('| 8.  Найти столбец, в котором разница между модулями полож - х и отриц - х эл - ов минимальна|')
    print('| 9.  Переставить местами столбцы с максимальной и минимальной суммой элементов               |')
    print('| 10. Вывести текующую матрицу                                                                |')
    print('|---------------------------------------------------------------------------------------------|')


matrix = []


while True:
    # Вывод меню
    menu()
    array = []

    # Ввод команды меню
    menu_command = int(input('Введите команду меню: '))

    # Ввод матрицы
    if menu_command == 1:
        rows = int(input('Введите количество строк: '))
        cols = int(input('Введите количество столбцов: '))
        matrix = []
        for i in range(rows):
            matrix.append([])
            for j in range(cols):
                a = int(input(f'Введите {j + 1} элемент {i + 1} строки: '))
                matrix[i].append(a)
        print(matrix)

    # Добавление строки
    elif menu_command == 2:
        if len(matrix) != 0:
            if len(matrix[0]) != 0:
                for i in range(len(matrix[0])):
                    value = int(input(f'Введите {i + 1} элемент строки: '))
                    array.append(value)
                matrix.append(array)
                print(matrix)
            else:
                print('Матрица не заполнена')

    # elif menu_command == 21:
    #     if len(matrix) != 0:
    #         index = int(input('Введите индекс добавляемого элемента: '))
    #         while index not in range(len(matrix)):
    #             print('Введен некорректный индекс')
    #             index = int(input('Введите индекс добавляемого элемента: '))
    #         for i in range(len(matrix[0])):
    #             value = int(input(f'Введите {i + 1} элемент строки: '))
    #             array.append(value)
    #         matrix.append(array)
    #         for i in range(len(matrix) - 1, index, - 1):
    #             matrix[i] = matrix[i - 1]
    #         matrix[index] = array
    #         print(matrix)
    #     else:
    #         print('Матрица не заполнена')

    # Удаление строки
    elif menu_command == 3:
        if len(matrix) != 0:
            if len(matrix[0]) != 0:
                index_del = int(input('Введите индекс удаляемой строки: '))
                matrix.pop(index_del)
                print(matrix)
            else:
                print('Матрица не заполнена')
        else:
            print('Матрица не заполнена')

    elif menu_command == 31:
        if len(matrix) != 0:
            if len(matrix[0]) != 0:
                index_del = int(input('Введите индекс удаляемой строки: '))
                while index_del not in range(len(matrix)):
                    print('Введен некорректный индекс')
                    index = int(input('Введите индекс добавляемого элемента: '))
                for i in range(index_del, len(matrix) - 1):
                    matrix[i] = matrix[i + 1]
                del matrix[-1]
                print(matrix)
            else:
                print('Матрица не заполнена')
        else:
            print('Матрица не заполнена')

    # Добавление столбца
    elif menu_command == 4:
        if len(matrix) != 0:
            if len(matrix[0]) != 0:
                for i in range(len(matrix)):
                    matrix[i].append(int(input(f'Введите {i + 1} элемет добавляемого столбца: ')))
                print(matrix)
            else:
                print('Матрица не заполнена')
        else:
            print('Матрица не заполнена')

    # Удалиние столбца
    elif menu_command == 5:
        if len(matrix) != 0:
            if len(matrix[0]) != 0:
                index_del = int(input('Введите индекс удаляемого столбца: '))
                while index_del not in range(len(matrix[0])):
                    index_del = int(input('Введите индекс удаляемого столбца: '))
                for i in range(len(matrix)):
                    for j in range(index_del, len(matrix[i]) - 1):
                        matrix[i][j] = matrix[i][j + 1]
                    del matrix[i][-1]
                print(matrix)
            else:
                print('Матрица не заполнена')
        else:
            print('Матрица не заполнена')

    # Нахождение строки с наибольшим количесвтом повторяющихся элементов
    elif menu_command == 6:
        max_len = 1
        num_len = 0
        flag = False
        if len(matrix) != 0:
            for x in range(len(matrix)):
                for y in range(len(matrix[x])):
                    str_len = matrix[x].count(matrix[x][y])
                    if str_len > max_len:
                        max_len = str_len
                        num_len = matrix[x]
                        flag = True
            if flag:
                print(num_len)
            else:
                print('Повторяющихся элементов нет')
        else:
            print('Матрица не заполнена')

    # Перестановка местами строк с наибольшим и наименьшим количеством отрицательных элементов
    elif menu_command == 7:
        x = 0
        y = 0
        max_value = float('-inf')
        min_value = float('+inf')
        if len(matrix) != 0:
            if len(matrix[0]) != 0:
                for i in range(len(matrix)):
                    counter = 0
                    for j in range(len(matrix[i])):
                        if matrix[i][j] < 0:
                            counter += 1
                    if counter != 0:
                        if counter > max_value:
                            max_value = counter
                            x = i
                        if counter < min_value:
                            min_value = counter
                            y = i

                if min_value == max_value:
                    print('Перестановки не было')

                matrix[x], matrix[y] = matrix[y], matrix[x]
                print(matrix)
            else:
                print('Матрица не заполнена')

    # Нахождение столбца в котом разница между модулями сумми отрицательных и положительных элементов минимальна
    elif menu_command == 8:
        a = 0
        min_abs = float('+inf')
        if len(matrix) != 0:
            if len(matrix[0]) != 0:
                for i in range(len(matrix[0])):
                    d = 0
                    for j in range(len(matrix)):
                        d += matrix[j][i]
                    if d < min_abs:
                        min_abs = d
                        a = i
                for x in range(len(matrix)):
                    print(matrix[x][a])
            else:
                print('Матрица не заполнена')
        else:
            print('Матрица не заполнена')

    # Перестановка местами столбцов с максимальной и минимальной суммой
    elif menu_command == 9:
        minimum = float('+inf')
        maximum = float('-inf')
        a = 0
        b = 0
        if len(matrix) != 0:
            if len(matrix[0]) != 0:
                for i in range(len(matrix[0])):
                    total = 0
                    for j in range(len(matrix)):
                        total += matrix[j][i]
                    if maximum < total:
                        maximum = total
                        a = i
                    if minimum > total:
                        minimum = total
                        b = i
                if maximum == minimum:
                    print('Перестановки не было')

                for x in range(len(matrix)):
                    matrix[x][a], matrix[x][b] = matrix[x][b], matrix[x][a]
                print(matrix)
            else:
                print('Матрица не заппонена')
        else:
            print('Матрица не заполнена')

    # Вывод матрицы
    elif menu_command == 10:
        if len(matrix) != 0:
            if len(matrix[0]) != 0:
                for y in range(len(matrix)):
                    for z in range(len(matrix[y])):
                        print(str(matrix[y][z]).ljust(6), end='')
                    print()
            else:
                print('Матрица не заполнена')
        else:
            print('Матрица не заполнена')

    elif menu_command == 0:
        exit(-1)
    else:
        print('Введена некорректная команда меню')
