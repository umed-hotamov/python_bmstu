# Функция проверки на дурака чисел с плавающей точкой
def float_check(a):
    global point_place
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


# Функция ввода слова с проверкой
def clever_input(txt: str):
    while True:
        word = input(txt)
        if len(word) == 0:
            print(' Должно быть быть одно')
            continue
        elif len(word.split()) > 1:
            print(' Должно быть быть одно')
            continue
        else:
            word = ''.join(word.split())
            break
    return word


# Функция по вычислению строки максимальной длины
def max_str(txt):
    max_len = len(txt[0])
    i_max = 0
    for i in range(1, len(txt)):
        if len(txt[i]) > max_len:
            max_len = len(txt[i])
            i_max = i
    return max_len, i_max


# Функция по выравниванию текст по левой стороне
def to_left_side(txt):
    if current_side == 2:
        for i in range(len(txt)):
            counter = 0
            for j in range(len(txt[i])):
                if txt[i][j] == ' ':
                    counter += 1
                else:
                    break
            txt[i] = txt[i].replace(counter * ' ', '', 1)
    if current_side == 3 or current_side == 1:
        for i in range(len(txt)):
            while '  ' in txt[i]:
                txt[i] = txt[i].replace('  ', ' ')
    return txt


# Функция по выравниванию текст по правой стороне
def to_right_side(txt):
    for i in range(len(txt)):
        if i != i_max:
            skips = abs(len(txt[i]) - len(txt[i_max]))
            txt[i] = skips * ' ' + text[i]
    return txt


# Функция по возвращению выравнивания
def return_side(txt):
    # Ищем новую самую длинную строку
    max_len, i_max = max_str(txt)
    # Возвращаем последнее выравнивание
    if current_side == 1:
        to_left_side(txt)
    elif current_side == 2:
        to_right_side(txt)
    else:
        by_width(txt)
    return txt


# Выравнивание по ширине
def by_width(txt):
    for i in range(len(txt)):
            skips = abs(len(txt[i]) - len(txt[i_max]))
            words = txt[i].split()
            spaces = len(words) - 1
            new_spaces = (skips // spaces) + 1
            dop_spaces = skips % spaces
            for j in range(len(words)):
                if dop_spaces == 0:
                    break
                else:
                    words[j] += ' '
                    dop_spaces -= 1
            txt[i] = (new_spaces * ' ').join(words)
    return txt


# Функция по замене слова
def word_replace(text, old_word, new_word):
    text = to_left_side(text)
    for i in range(len(text)):
        words = text[i].split()
        for j in range(len(words)):
            # Проверка на наличие какого-либо знака препинания
            if words[j][-1] not in letters:
                if words[j][:-1] == old_word:
                    words[j] = words[j].replace(old_word, new_word, 1)
            else:
                if words[j] == old_word:
                    words[j] = words[j].replace(old_word, new_word, 1)
        text[i] = ' '.join(words)
    text = return_side(text)
    return text


def expressions(text):
    text = to_left_side(text)
    for i in range(len(text)):
        # Если в строке нет знаков умножения или деления, даже не рассматриваем их
        if '*' in text[i] or '/' in text[i]:
            words = text[i].split()
            for j in range(1, len(words)):
                # Работаем с умножением
                if '*' in words[j] and not '/' in words[j]:
                    # Работаем с выражением вида 5 * 7
                    if len(words[j]) == 1:
                        if int_check(words[j - 1]) is not None and int_check(words[j + 1]) is not None:
                            a = int(words[j - 1]) * int(words[j + 1])
                            words[j - 1] = words[j - 1].replace(words[j - 1], '', 1)
                            words[j + 1] = words[j + 1].replace(words[j + 1], '', 1)
                            words[j] = words[j].replace(words[j], str(a), 1)
                    else:
                        # Работаем с выражением вида 5* 7
                        if words[j][-1:] == '*':
                            if '*' not in words[j][:-1]:
                                if int_check(words[j][:-1]) is not None and int_check(words[j + 1]) is not None:
                                    a = int(words[j][:-1]) * int(words[j + 1])
                                    words[j] = words[j].replace(words[j], str(a), 1)
                                    words[j + 1] = words[j + 1].replace(words[j + 1], '', 1)
                        # Работаем с выражением вида 5 *7
                        elif words[j][:1] == '*':
                            if '*' not in words[j][1:]:
                                if int_check(words[j][1:]) is not None and int_check(words[j - 1]) is not None:
                                    a = int(words[j][1:]) * int(words[j - 1])
                                    words[j] = words[j].replace(words[j], str(a), 1)
                                    words[j - 1] = words[j - 1].replace(words[j - 1], '', 1)
                        # Работаем с выражением вида 5*7
                        else:
                            ex = words[j]
                            ex = ex.replace('*', ' ', 1)
                            ex = ex.split()
                            if len(ex) == 2 and int_check(ex[0]) is not None and int_check(ex[1]) is not None:
                                a = int(ex[0]) * int(ex[1])
                                words[j] = words[j].replace(words[j], str(a), 1)
                # Работаем с делением
                elif '/' in words[j] and not '*' in words[j]:
                    # Работаем с выражением вида 4 / 2
                    if len(words[j]) == 1:
                        if int_check(words[j - 1]) is not None and int_check(words[j + 1]) is not None and int(
                                words[j + 1]) != 0:
                            a = int(words[j - 1]) / int(words[j + 1])
                            if a % 1 == 0:
                                a = int(a)
                            words[j - 1] = words[j - 1].replace(words[j - 1], '', 1)
                            words[j + 1] = words[j + 1].replace(words[j + 1], '', 1)
                            words[j] = words[j].replace(words[j], str(a), 1)
                    else:
                        # Работаем с выражением вида 4/ 2
                        if words[j][-1:] == '/':
                            if '/' not in words[j][:-1]:
                                if int_check(words[j][:-1]) is not None and int_check(words[j + 1]) is not None:
                                    a = int(words[j][:-1]) / int(words[j + 1])
                                    if a % 1 == 0:
                                        a = int(a)
                                    words[j] = words[j].replace(words[j], str(a), 1)
                                    words[j + 1] = words[j + 1].replace(words[j + 1], '', 1)
                        # Работаем с выражением вида 4 /2
                        elif words[j][:1] == '/':
                            if '/' not in words[j][1:]:
                                if int_check(words[j][1:]) is not None and int_check(words[j - 1]) is not None:
                                    a = int(words[j - 1]) / int(words[j][1:])
                                    if a % 1 == 0:
                                        a = int(a)
                                    words[j] = words[j].replace(words[j], str(a), 1)
                                    words[j - 1] = words[j - 1].replace(words[j - 1], '', 1)
                        # Работаем с выражением вида 4/2
                        else:
                            ex = words[j]
                            ex = ex.replace('/', ' ', 1)
                            ex = ex.split()
                            if len(ex) == 2 and int_check(ex[0]) is not None and int_check(
                                    ex[1]) is not None and int_check(ex[1]) != '0':
                                a = int(ex[0]) / int(ex[1])
                                if a % 1 == 0:
                                    a = int(a)
                                words[j] = words[j].replace(words[j], str(a), 1)
            text[i] = ' '.join(words)
    text = return_side(text)
    return text


# Функция по нахождению предложения с самым большим кол-вом символов
def count_word(text):
    n = 0
    flag = False
    c = ''
    arr = []
    for i in range(len(text)):
        arr.append(text[i])

    find_s = []
    max_value = float('-inf')
    word = input('Задайте букву: ')
    while len(word) != 1 and word.isdigit():
        print('Задайте букву!')
        word = input('Задайте букву: ')
    for z in range(len(arr)):
        for y in range(len(arr[z])):
            if arr[z][y] != '.':
                c += arr[z][y]
            else:
                c += arr[z][y]
                find_s.append(c)
                c = ''

        for i in range(len(find_s)):
            counter = 0
            for j in range(len(find_s[i])):
                k = find_s[i][j].title()
                if k == word.upper():
                    counter += 1
                    flag = True
            if counter > max_value:
                max_value = counter
                n = i
    if flag:
        print(find_s[n])
    else:
        print('Заданной буквы нет в тексте')


text = ['Он убрал 6 * 5 инструменты, напился     воды из починенного водопровода и сел на скамью перед открытой ',
        'дверью в кухню. 5 * 2 Там хозяйничала Дид, и он с огромным 10 / 2 облегчением прислушивался к ',
        'ее шагам. Он жадно глотал душистый горный воздух, словно водолаз, только что поднявшийся со дна морского. Он впивался  ',
        'взглядом в облака, в синеву неба, в зелень долины, как будто все это он вдыхал вместе с воздухом.']

# print(*text)
current_side = 1
letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
if len(text) != 0:
    max_len, i_max = max_str(text)
# Выводим на экран все доступные команды
while True:
    print(
        '',
        'Команды:',
        ' 1) Выровнять текст по левому краю',
        ' 2) Выровнять текст по правому краю',
        ' 3) Выровнять текст по ширине',
        ' 4) Удаление всех вхождений заданного слова',
        ' 5) Замена одного слова другим во всём тексте',
        ' 6) Вычисление арифметических действий (умножение и деление)',
        ' 7) Найти предложение с максимальным количеством слов начинающихся на заданную букву',
        ' 8) Вывести текст',
        ' 0) Завершение программы',
        '',
        sep='\n'
    )
    # Просим пользователя ввести номер команды и проверяем ввёл ли пользователь нужное число
    command = int_check(input('Введите номер команды: '))
    if command is None or command < 0 or command > 8:
        print('Вы не выбрали номер команды из списка')
        print('Повторите попытку')
        print()
        continue
    if len(text) == 0:
        if command != 0:
            print('Текст не введён, вам доступны только команда № 0')
            continue

    if command == 1:
        text = to_left_side(text)
        current_side = 1
        print('Текст был выравнен по левому краю')

    if command == 2:
        text = to_left_side(text)
        text = to_right_side(text)
        current_side = 2
        print('Текст был выравнен по правому краю')

    if command == 3:
        text = to_left_side(text)
        text = by_width(text)
        current_side = 3
        print('Текст был выравнен ширине')

    if command == 4:
        word_del = clever_input('Введите удаляемое слово: ')
        new_word = ''
        word_replace(text, word_del, new_word)
        print('Слово было удалено')
    if command == 5:
        old_word = clever_input('Введите заменяемое слово: ')
        new_word = clever_input('Введите новое слово: ')
        word_replace(text, old_word, new_word)
        print('Слова были заменены')

    if command == 6:
        expressions(text)
    if command == 7:
        text = to_left_side(text)
        count_word(text)
    if command == 8:
        for i in range(len(text)):
            print(text[i])

    # Завершение программы
    if command == 0:
        exit(-1)
