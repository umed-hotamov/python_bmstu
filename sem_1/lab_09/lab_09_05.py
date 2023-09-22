G = []
matrix_d = []
matrix_z = []
# Заполнение матрицы D и Z
rows = int(input('Введите количество строк матрицы D и Z: '))
while rows < 2:
    rows = int(input('Введите количество строк матрицы D и Z: '))

cols = int(input('Введите количество столбцов матрицы D и Z: '))
while cols < 2:
    cols = int(input('Введите количество столбцов матрицы D и Z : '))

for i in range(rows):
    matrix_d.append([])
    for j in range(cols):
        a = int(input(f'Введите {j + 1} элемент {i + 1} строки матрицы D: '))
        matrix_d[i].append(a)

print('-'*50)

for x in range(rows):
    matrix_z.append([])
    for y in range(cols):
        b = int(input(f'Введите {y + 1} элемент {x + 1} строки матрицы Z: '))
        matrix_z[x].append(b)
print('-'*50)

# Подсчет количества элементов строки матриы D превышающих сумму элементов строки матрицы Z
# и заполнение этого количества в массив G

for i in range(len(matrix_d)):
    counter = 0
    sum_z = 0
    for j in range(len(matrix_d[i])):
        if matrix_z[i][j]:
            sum_z += matrix_z[i][j]
    for n in range(len(matrix_d[i])):
        if matrix_d[i][n] > sum_z:
            counter += 1

    G.append(counter)

max_value = G[0]
for i in range(len(G)):
    if G[i] > max_value:
        max_value = G[i]

print('Матрица D до преобразования')
for i in range(len(matrix_d)):
    for j in range(len(matrix_d[0])):
        print(f'{matrix_d[i][j]:^10.4g}', sep='', end=' ')
    print()
print()

# Умножение максимального элемента массива G на матрицу D
for i in range(len(matrix_d)):
    for j in range(len(matrix_d[i])):
        matrix_d[i][j] = max_value * matrix_d[i][j]


print('Матрица D после преобразования')
for i in range(len(matrix_d)):
    for j in range(len(matrix_d[0])):
        print(f'{matrix_d[i][j]:^10.4g}', sep='', end=' ')
    print()
print()

print('Матрица Z')
for i in range(len(matrix_z)):
    for j in range(len(matrix_z[0])):
        print(f'{matrix_z[i][j]:^10.4g}', sep='', end=' ')
    print()
print()

print('Матрица G')
print(G)
