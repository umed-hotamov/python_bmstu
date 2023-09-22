matrix = []
# Заполнение матрицы
rows = int(input('Введите количество строк : '))
while rows < 2:
    rows = int(input('Введите количество строк : '))

cols = int(input('Введите количество столбцов : '))
while cols < 2:
    cols = int(input('Введите количество столбцов : '))

for i in range(rows):
    matrix.append([])
    for j in range(cols):
        value = input(f'Введите {j + 1} элемент {i + 1} строки матрицы D: ')
        matrix[i].append(value)

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'B', 'E' 'I', 'O', 'U', 'Y']

# Замена гласных английских букв на точки
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        for c in matrix[i][j]:
            if c in vowels:
                matrix[i][j] = matrix[i][j].replace(c, '.')

for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        print(matrix[x][y].rjust(20), sep='', end=' ')
    print()
