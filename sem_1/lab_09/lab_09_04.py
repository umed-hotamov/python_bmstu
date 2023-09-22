matrix = []
# Заполнение матрицы
size = int(input('Введите размер матрицы: '))
while size < 2:
    print('Размер квадратной матрица не может быть меньше 2')
    size = int(input('Введите размер матрицы: '))
for i in range(size):
    matrix.append([])
    for j in range(size):
        a = int(input(f'Введите {j + 1} элемент {i + 1} строки: '))
        matrix[i].append(a)

print('Исходная матрица')
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f'{matrix[i][j]:^10.4g}', sep='', end=' ')
    print()


# Команда меню
def command_mode():
    print('1. Поворот на 90 градусов по часовой стрелке')
    print('2. Поворот на 90 градусов против часовой стрелки')


# Поворот матрицы на 90 градусов по часовой стрелке и на 90 градусов против часовой стрелки


while True:
    command_mode()
    mode = int(input('Введите команду: '))
    if mode == 1:
        for i in range(len(matrix) // 2):
            for j in range(i, len(matrix[i]) - i - 1):
                matrix[j][len(matrix) - i - 1], matrix[len(matrix) - i - 1][len(matrix) - 1 - j], \
                matrix[len(matrix) - 1 - j][i], matrix[i][j] = \
                matrix[i][j], matrix[j][len(matrix) - i - 1], matrix[len(matrix) - i - 1][len(matrix) - 1 - j], \
                matrix[len(matrix) - 1 - j][i]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(f'{matrix[i][j]: ^10.4g}', sep='', end=' ')
            print()
        print()

    elif mode == 2:
        for i in range(len(matrix) // 2):
            for j in range(i, len(matrix[i]) - i - 1):
                matrix[i][j], matrix[j][len(matrix) - i - 1], matrix[len(matrix) - i - 1][len(matrix) - 1 - j], matrix[len(matrix) - 1 - j][i],=\
                    matrix[j][len(matrix) - i - 1], matrix[len(matrix) - i - 1][len(matrix) - 1 - j], matrix[len(matrix) - 1 - j][i], matrix[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(f'{matrix[i][j]: ^10.4g}', sep='', end=' ')
            print()
        print()
    elif mode == 0:
        exit(-1)
    else:
        print('Введена некорректная команда')
