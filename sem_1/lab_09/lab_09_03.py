arr = []
# Заполнение матрицы
size = int(input('Введите размер матрицы: '))
while size < 2:
    print('Размер квадратной матрица не может быть меньше 2')
    size = int(input('Введите размер матрицы: '))
for i in range(size):
    arr.append([])
    for j in range(size):
        a = int(input(f'Введите {j + 1} элемент {i + 1} строки: '))
        arr[i].append(a)


# Транспонирование матрицы
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr[i])):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], sep='', end=' ')
    print()
