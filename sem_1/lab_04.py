# Функции: y1 = x * 2 ** x - 1.05, y2 = x ** 3 * 3 * x ** 2 + 1

# Ввод
from decimal import Decimal

x_first, step, x_last = map(float, input('Введите начальный отрезок, шаг и конечный отрезок через пробел: ').split())
# Вывод таблицы значений

if step == 0:
    print('Шаг не может быть равен 0')
    exit(-1)

amount_of_iterations = int(Decimal(str(x_last)) - Decimal(str(x_first)) / Decimal(str(step))) + 1

print('-------------------------------------------')
print('|{:^13}|{:^13}|{:^13}|'.format('x', 'y1', 'y2'))
print('|-----------------------------------------|')
s = 0
max_y_of_y1 = 0
min_y_of_y1 = 0  # считаем их для построения y1

for i in range(amount_of_iterations):
    x = x_first + step * i
    if x == x_last + step:
        break
    y1 = x * (2 ** x) - 1.05
    if y1 > max_y_of_y1:
        max_y_of_y1 = y1
    elif y1 < min_y_of_y1:
        min_y_of_y1 = y1
    y2 = x ** 3 * 3 * x ** 2 + 1
    if y1 > 0 and y2 > 0:
        s = y1 + y2
        s += s
    print('|{:^13.7g}|{:^13.7g}|{:^13.7g}|'.format(x, y1, y2))
print('-------------------------------------------')
print()

# ввод количества засечек
amount_of_serifs = int(input('Введите количество засечек: '))
while amount_of_serifs < 4 or amount_of_serifs > 8:
    print('Количество засечек должно быть от 4 до 8!: ')
    amount_of_serifs = int(input('Введите количество засечек: '))

# вывод засечек
print('Отрисовка функции y1 = x * 2 ** x - 1.05')
print()
input_of_serifs = ' ' * 13
amplitude_of_y1 = max_y_of_y1 + abs(min_y_of_y1)  # амплитуда y1
step_of_serifs = amplitude_of_y1 / (amount_of_serifs - 1)
# разница в значении между засечками
distance_between_serifs = 80 / (amount_of_serifs - 1)  # расстояние между засечками
infelicity = distance_between_serifs % 1
# погрешность расстояния между засечками
distance_between_serifs = int(distance_between_serifs)
for i in range(amount_of_serifs):
    if i != amount_of_serifs - 1:
        serif = "{:.7g}".format(min_y_of_y1 + step_of_serifs * i)
        # значение засечки
        input_of_serifs += serif + ' ' * (distance_between_serifs +
                                          round(i * infelicity % 1) - len(serif))
    else:
        last_serif = "{:.7g}".format(max_y_of_y1)
        print(input_of_serifs[:93 - len(last_serif)] + last_serif)
        # вывод засечек

# Построение функции
location_of_Ox = 0
if max_y_of_y1 != 0 and min_y_of_y1 != 0:
    location_of_Ox = round(
        80 / (max_y_of_y1 + abs(min_y_of_y1)) * abs(min_y_of_y1))
    # Отношение части графика до нуля и после

for i in range(amount_of_iterations):
    x = x_first + step * i
    y1 = 2 ** x - 4 * x
    if location_of_Ox == 0:
        location_of_y1 = round(80 * abs(y1) / amplitude_of_y1)
        print("{:^11.7g}".format(x) + ' |' + ' ' *
              (location_of_y1 - 1) + '*' + ' ' * (79 - location_of_y1))
        # если график не пересекает ось x, мы её не выводим, значения
        # функции в связи с эти тоже только одного знака
    elif y1 == 0:
        print("{:^11.7g}".format(x) + ' |' + ' ' *
              (location_of_Ox - 1) + '#' + ' ' * (79 - location_of_y1))
        # выводим решётку если точка совпадает с осью x
    else:
        if y1 < 0:
            location_of_y1 = round(80 * abs(min_y_of_y1 - y1) /
                                   amplitude_of_y1)

            location_of_y1 = 1 if location_of_y1 == 0 else location_of_y1
            # при минимальном значении функции её нынешнее значение и
            # минимальное совпадут и выйдет 0, однако номер
            # числа в строке нулём быть не может, иначе сдвинется ось x,
            # очевидно, что при значении 0 реальное
            # местоположение - 1
            print("{:^11.7g}".format(x) + ' |' + ' ' * (location_of_y1 - 1) +
                  '*' + ' ' * (location_of_Ox - location_of_y1 - 1) + '|' +
                  ' ' * (79 - location_of_y1))
            # если значение функции меньше нуля, то её значение выводится
            # раньше оси x, иначе наоборот
        else:
            location_of_y1 = round(80 * (y1 + abs(min_y_of_y1)) /
                                   amplitude_of_y1)
            print("{:^11.7g}".format(x) + ' |' + ' ' * (location_of_Ox - 1) +
                  '|' + ' ' * (location_of_y1 - location_of_Ox - 1) + '*' +
                  ' ' * (79 - location_of_Ox))
print()

# Дополнительное задание
print('Сумма всех положительных значений функции y1, y2: ', s)
