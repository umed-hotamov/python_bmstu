# Задаём размерность трёхмерной матрицы
X = int(input('Введите высоту матрицы: '))
Y = int(input('Введите ширину матрицы: '))
Z = int(input('Введите глубину матрицы: '))

# Создаём и заполняем матрицу
matrix = []
for i in range(X):
    matrix += [[]]
    for j in range(Y):
        matrix[i] += [[]]
        for k in range(Z):
            x = int(input('Введите элемент матрицы - {}.{}.{}: '.format(i+1, j+1, k+1)))
            matrix[i][j] += [x]

for i in range(len(matrix)):
    print(matrix[i])
# Выводим i-ый срез по второму индексу
while True:
    index = int(input('Введите i-ый срез: '))
    if index > len(matrix[0]):
        print('Срез выходит за предел массива')
    else:
        break
    
for i in range(len(matrix)):
    print(matrix[i][index-1])
