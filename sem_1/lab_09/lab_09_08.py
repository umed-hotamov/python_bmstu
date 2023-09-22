A = []
B = []
C = []
V = []

# Заполнение матрицы A и B
rows = int(input('Введите количество строк матрицы A и B: '))
while rows < 2:
    rows = int(input('Введите количество строк матрицы A и B: '))

cols = int(input('Введите количество столбцов матрицы A и B: '))
while cols < 2:
    cols = int(input('Введите количество столбцов матрицы A и B: '))

for i in range(rows):
    A.append([])
    for j in range(cols):
        a = int(input(f'Введите {j + 1} элемент {i + 1} строки матрицы A: '))
        A[i].append(a)

print('-'*50)

for x in range(rows):
    B.append([])
    for y in range(cols):
        b = int(input(f'Введите {y + 1} элемент {x + 1} строки матрицы B: '))
        B[x].append(b)

# Формирование матрицы C путем перемножения 'i - x' элементов матрицы А и B
for i in range(len(A)):
    C.append([])
    for j in range(len(A[i])):
        c = A[i][j] * B[i][j]
        C[i].append(c)

# Сложение столбцов матрицы C и заполнение массива V
for x in range(len(C)):
    sum_v = 0
    for y in range(len(C[x])):
        sum_v += C[y][x]
    V.append(sum_v)

print('Матрица C')
for i in range(len(C)):
    for j in range(len(C[0])):
        print(f'{C[i][j]: ^10.4g}', sep='', end=' ')
    print()
print()
print('Массив V')
print(V)
