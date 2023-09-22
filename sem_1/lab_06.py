from math import sqrt


def menu():
    print('|---------------------------------------------------------------------------|')
    print('|                                Меню                                       |')
    print('|---------------------------------------------------------------------------|')
    print('| 1. Проинициализировать список первыми N элементами заданного в л/р 5 ряда |')
    print('| 2. Очистить список и ввести его с клавиатуры                              |')
    print('| 3. Добавить элемент в произвольное место списка                           |')
    print('| 4. Удалить произвольный элемент из списка (по номеру)                     |')
    print('| 5. Очистить список                                                        |')
    print('| 6. Найти значение K-го экстремума в списке                                |')
    print('| 7. Найти наиболее длинную последовательность по варианту                  |')
    print('|---------------------------------------------------------------------------|')

# Функци проверяют строки на содержание целых чисел
def input_command():
    x = input('Введите команду меню: ')     # Ввод команды меню
    while x.isdigit() != True:
        print('Введена некорректная команда меню')
        x = input('Введите корректную команду меню: ')
    else:
        x = int(x)
        return x


def is_number(str):
    try:
        if int(str):
            return True
        elif float(str):
            return True
    except ValueError:
        return False


array = list()

while True:
    # Вывод меню
    menu()
    menu_command = input_command()
    max_value = 0
    new_array = []
    temp_array = []

    # Работа с массивом
    # Проверка корректности данных ввода команды меню
    if menu_command == 1:
        k = input('Введите количество элементов ряда: ')
        if is_number(k) == True:
            k = int(k)
            n = 0
            while n < k:
                n = n + 1
                t = ((n + 1) / ((2 * n) - 1)) ** n
                array.append(f'{t:.2f}')
        print(array)

    elif menu_command == 2:
        array.clear()
        n = input('Введите количество элементов списка: ')
        if is_number(n) == True:
            n = int(n)
            for i in range(n):
                value = input(f'Вводите {i + 1} - й элемент списка: ')
                if is_number(value) == True:
                    value = int(value)
                    array.insert(i + 1, value)
            print(array)
            print()

    elif menu_command == 3:
        num = input('Введите добавляемый элемент списка: ')
        index = int(input('Введите индекс добавляемого элемента: '))
        if index == len(array):
            if is_number(num) == True:
                num = int(num)
                index = int(index)
                array.insert(index, num)
            print(array)
        else:
            print('Введен некорректный индекс')


    elif menu_command == 4:
        if len(array) != 0:
            index_del = input('Введите номер удаляемого элемента: ')
            if is_number(index_del) == True:
                if index_del in range(len(array)):
                    index_del = int(index_del)
                    array.pop(index_del)
                    print(array)
                else:
                    print('Введен некорректный индекс')
        else:
            print('Массив пустой')

    elif menu_command == 5:
        array.clear()

    elif menu_command == 6:
        k = input('Введите значение K-го экстремума в списке: ')
        if is_number(k) == True:
            k = int(k)
            count = 0
            for i in range(len(array)):
                if i == 0:
                    if array[i] > array[i + 1]:
                        count += 1
                        if count == k:
                            print(array[i])
                            break

                else:
                    if array[i] > array[i - 1]:
                        if i < len(array) - 1 and array[i] > array[i + 1]:
                            count += 1
                            if count == k:
                                print(array[i])
                                break
                        else:
                            if i == len(array) - 1 and count + 1 == k:
                                print(array[i])

    elif menu_command == 7:
        # Фукнция обрабатывает числа и возвращает простое число
        def is_prime(n):
            if (n - 1 == 0 or n < 0): return False
            d = 2
            while d <= sqrt(n):
                if (n % d == 0): return False
                d += 1
            return True

        for value in array:
            if is_number(value) == True:
                value = int(value)
                if is_prime(value) == True:
                    if len(temp_array) == 0:
                        temp_array.append(value)
                    else:
                        if value > temp_array[len(temp_array) - 1]:
                            temp_array.append(value)

                if is_prime(value) == False or value <= temp_array[len(temp_array) - 1]:
                    if len(temp_array) >= len(new_array):
                        new_array = temp_array.copy()
                    temp_array.clear()
                    if is_prime(value) == True:
                        temp_array.append(value)
        print(new_array)

    elif menu_command == 0:
        exit(-1)
    else:
        print('Введена некорректная команда меню')
