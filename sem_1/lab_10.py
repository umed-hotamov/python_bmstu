from math import cos, sin


# Проверка на ввод вещественных чисел

def convert_float(str_value):
    if len(str_value) == 0:
        return None
    is_float = True
    num_ended = False
    num_started = False
    e_counter = 0
    e_id = 0
    point_counter = 0
    sign_counter = 0
    for i in range(0, len(str_value)):
        ch = str_value[i]
        if not num_ended:
            if ch.isdigit():
                num_started = True
                if point_counter == 1 and e_counter == 0:
                    is_float = True
                if i == e_id + 1 or i == e_id + 2 and e_counter == 1:
                    is_float = True
            elif i == e_id + 1 and e_counter == 1 and i != len(str_value)-1:
                if ch == '-' or ch == '+':
                    continue
            elif not num_started and (ch == '-' or ch == '+') and \
                    sign_counter == 0 and i != len(str_value)-1:
                sign_counter += 1
            elif ch == '.':
                if not num_started:
                    is_float = False
                if point_counter == 0 and e_counter == 0:
                    point_counter += 1
                else:
                    return None
            elif ch == 'e':
                if e_counter == 0 and num_started and is_float:
                    is_float = False
                    e_id = i
                    e_counter += 1
                else:
                    return None
            elif not ch.isprintable() or ch == ' ':
                if not num_started:
                    if i != len(str_value)-1:
                        continue
                    else:
                        return None
                elif not num_ended:
                    num_ended = True
                else:
                    return None
            else:
                return None
        elif not ch.isprintable() or ch == ' ':
            continue
        else:
            return None

    if is_float:
        if float(str_value) == int(float(str_value)):
            return int(float(str_value))
        return float(str_value)
    return None


a = input('Введите начало отрезка: ')
while not a.isdigit():
    a = input('Введите начало отрезка: ')
else:
    a = int(a)


b = input('Введите конец отрезка: ')
while not b.isdigit():
    b = input('Введите начало отрезка: ')
else:
    b = int(b)

if a >= b:
    print('Начальное значние отрезка не может быть больше конечного значения отрезка')
    exit(-1)

n1 = input('Введите первое значение участков разбиения: ')
while not n1.isdigit():
    n1 = input('Введите первое значение участков разбиения: ')
else:
    n1 = int(n1)

while n1 < 1:
    n1 = input('Введите первое значение участков разбиения: ')
    while not n1.isdigit():
        n1 = input('Введите первое значение участков разбиения: ')
    else:
        n1 = int(n1)

n2 = input('Введите второе значение участков разбиения: ')
while not n2.isdigit():
    n2 = input('Введите второе значение участков разбиения: ')
else:
    n2 = int(n2)
while n2 < 1:
    n2 = input('Введите второе значение участков разбиения: ')
    while not n2.isdigit():
        n2 = input('Введите второе значение участков разбиения: ')
    else:
        n2 = int(n2)

print('----------------------------------------------------------')
print('|               |         N1          |         N2       |')
print('----------------------------------------------------------')


# Функция sin(x)


def f(x):
    return sin(x)


#  Первообразная функции


def F(x, y):
    return cos(y) - cos(x)


# Метод Серединных прямоугольников

def trianmethod(x, y, n):
    result = 0
    h = (y - x) / n
    for j in range(n):
        result += f(x + h * (j + 0.5))
    result *= h
    return result


print(f'|   Метод 1     |   {trianmethod(a, b, n1):^9.4g}         |  {trianmethod(a, b, n2):^9.4g}       |')


# Метод Буля


def boolesrule(x, y, n):
    if n % 4 == 0:

        h = (y - x) / n
        s = 0
        start = x
        for i in range(0, n, 4):
            s += (7 * f(start) + 32 * f(start + h) + 12 * f(start + 2 * h) + 32 * f(start + 3 * h) + 7 * f(start + 4 * h))
            start += 4 * h
        return s * h * 2 / 45
    else:
        s = 0
        return s


print('----------------------------------------------------------')
print(f'|   Метод 2     |   {boolesrule(a, b, n1):^9.4g}         |  {boolesrule(a, b, n2):^9.4g}       |')
print('----------------------------------------------------------')

#  Абсолютная и относительная погрешности метода средних прямоугольников

mid_rect = abs(trianmethod(a, b, n1) - F(a, b))
print('Абсолютная погрешность метода серединных прямоугольников - ', mid_rect)

rel_mid = abs(mid_rect / F(a, b))
print('Относительная погрешность метода серединных прямоугольников - ', rel_mid)
print()

# Абсолютная погрешность метода Буля

if boolesrule(a, b, n1) == 0:
    print('Погрешности равны метода Буля равны 0')
else:
    bul = abs(boolesrule(a, b, n1) - F(a, b))
    print('Абсолютная погрешность метода Буля - ', bul)

    rel_bul = abs(bul / F(a, b))
    print('Относительная погрешность Буля - ', rel_bul)
    print()

# Вычисление количества участков разбиения для менее точного метода, для которого интеграл будет вычислен с заданной
# точностью

    if bul > mid_rect:
        eps = convert_float(input('Введите точность: '))
        if eps < 0:
            print('Точность не может быть меньше 0')
            exit(-1)
        k = 1
        while abs(boolesrule(a, b, k) - boolesrule(a, b, k * 2)) > eps:
            k *= 2
        print('Количество участков разбиения метода Буля: ', k)

eps = convert_float(input('Введите точность: '))
if eps < 0:
    print('Точность не может быть меньше 0')
    exit(-1)
k = 4
while abs(trianmethod(a, b, k) - trianmethod(a, b, k * 2)) > eps:
    k += 4
print('Количество участков разбиения метода Серединных прямоугольников: ', k)
