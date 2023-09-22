def menu():
    print('|---------------------------------------------------------------------------|')
    print('|                                Меню                                       |')
    print('|---------------------------------------------------------------------------|')
    print('| 1. Очистить список и ввести его с клавиатуры                              |')
    print('| 2. Добавить элемент в произвольное место списка                           |')
    print('| 3. Удалить произвольный элемент из списка (по номеру)                     |')
    print('| 4. Очистить список                                                        |')
    print('| 5. Поиск элемента наибольшей длины, не содержащего цифр                   |')
    print('| 6. Замена всех цифр на пробелы                                            |')
    print('|---------------------------------------------------------------------------|')

# Функци проверяют строки на содержание целых чисел
def input_command():
    x = input('Введите команду меню: ')
    while x.isdigit() != True:
        print('Введена некорректная команда меню')
        x = input('Введите корректную команду меню: ')
    else:
        x = int(x)
        return x

def is_int():
    y = input('Введите количество элементов списка: ')
    while y.isdigit() != True:
        y = input('Введите количество элементов списка: ')
    else:
        y = int(y)
        return y

array = list()


while True:
    menu()
    new_array = []
    numbers = '0123456789'
    menu_command = input_command()
    if menu_command == 1:
        array.clear()
        n = is_int()
        for i in range(n):
            value = input(f'Введите {i + 1} - й элемент списка: ')
            array.append(value)
        print(array)
        print()

    elif menu_command == 2:
        if len(array) != 0:
            index = int(input('Введите индекс добавляемого элемента: '))
            while index not in range(len(array)):
                print('Введен некорректный индекс')
                index = int(input('Введите индекс добавляемого элемента: '))
            num = input('Введите добавляемый элемент: ')
            array.append(num)
            for i in range(len(array) - 1, index, - 1):
                array[i] = array[i - 1]
            array[index] = num
            print(array)
        else:
            print('Массив пустой')

    elif menu_command == 3:
        if len(array) != 0:
            index_del = int(input('Введите индекс удаляемого элемента: '))
            if index_del in range(len(array)):
                for x in range(index_del, len(array) - 1):
                    array[x] = array[x + 1]
                del array[-1]
                print(array)
            else:
                print('Введен некорректный индекс')
        else:
            print('Массив пустой')

    elif menu_command == 4:
        array.clear()

    elif menu_command == 5:
        if len(array) != 0:
            for i in array:
                flag = 0
                if type(i) == str:
                    for c in i:
                        if c in numbers:
                            flag = 1

                if flag == 0:
                    new_array.append(i)
            if len(new_array) != 0:
                max_len = new_array[0]
                for x in new_array:
                    if len(x) > len(max_len):
                        max_len = x
                print(max_len)
            else:
                print('ошибка')
        else:
            print('Массив пустой')

    elif menu_command == 6:
        if len(array) != 0:
            for i in array:
                for digit in i:
                    if digit.isdigit():
                        i = i.replace(digit, ' ')
                new_array.append(i)
            print(new_array)
        else:
            print('Массив пустой')

    elif menu_command == 0:
        exit(-1)
    else:
        print('Введена некорректная команад меню')
