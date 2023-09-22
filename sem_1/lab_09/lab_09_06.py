matrix_d = []
array_i = []
array_r = []
rows = int(input('Введите количество строк : '))
while rows < 2:
    rows = int(input('Введите количество строк : '))

cols = int(input('Введите количество столбцов : '))
while cols < 2:
    cols = int(input('Введите количество столбцов : '))

# Заполнение матрицы

for i in range(rows):
    matrix_d.append([])
    for j in range(cols):
        a = int(input(f'Введите {j + 1} элемент {i + 1} строки матрицы D: '))
        matrix_d[i].append(a)

n = int(input('Введите количество строк, для которых надо определить максимальный элемент: '))
if n == 0:
    print('Количество строк должно быть больше 0')
    exit(-1)
while n not in range(len(matrix_d) + 1):
    n = int(input('Введите количество строк, для которых надо определить максимальный элемент: '))

# Заполнение массива номерами строк, для которых надо определить максимальный элемент
for i in range(n):
    value = int(input(f'Введите индекс {i + 1} - й строки: '))
    while value not in range(len(matrix_d)):
        value = int(input(f'Введите индекс {i + 1} - й строки: '))
    array_i.append(value)

# Заполнение массива R максимальными элементами
for i in range(len(matrix_d)):
    max_value = float('-inf')
    for j in array_i:
        for x in range(len(matrix_d[i])):
            if matrix_d[i][x] > max_value:
                max_value = matrix_d[i][x]
        array_r.append(max_value)

# Вычисление среднего арифметического массива R
counter = 0
b = 0
for i in range(len(array_r)):
    b += array_r[i]
    counter += 1
av = b / counter

print('Матрица D')
for i in range(len(matrix_d)):
    for j in range(len(matrix_d[0])):
        print(f'{matrix_d[i][j]:^10.4g}', sep='', end=' ')
    print()
print()

print('Массив I')
print(array_i)
print()
print('Массив R')
print(array_r)
print()
print('Среднее арифметическое значение массива R')
print(av)
