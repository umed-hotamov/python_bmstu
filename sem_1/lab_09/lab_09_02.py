arr = []
# Заполнение матрицы
size = int(input('Введите размер матрицы: '))
while size < 2:
    size = int(input('Введите размер матрицы: '))
for i in range(size):
    arr.append([])
    for j in range(size):
        a = int(input(f'Введите {j + 1} элемент {i + 1} строки: '))
        arr[i].append(a)

# Нахождение максимального элемента над главной диагональю
max_value = float('-inf')
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i][j] > max_value:
            max_value = arr[i][j]
print(max_value)
print()

# Нахождение минимального элемента под побочной диагональю
min_value = float('+inf')
for x in range(len(arr)):
    for y in range(len(arr) - x, len(arr)):
        if arr[x][y] < min_value:
            min_value = arr[x][y]
print(min_value)
print()

# Вывод матрицы
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], sep='', end=' ')
    print()
