from math import sin
# Зполнение массива D
D = []
d = int(input('Введите количество элементов массива F: '))
while d < 2:
    d = int(input('Введите количество элементов массива F: '))
for i in range(d):
    value_d = int(input(f'Введите {i + 1} - й элемент массива: '))
    D.append(value_d)

# Заполнение массива F
F = []
f = int(input('Введите количество элементов массива F: '))
while f < 2:
    f = int(input('Введите количество элементов массива F: '))
for i in range(f):
    value_f = int(input(f'Введите {i + 1} - й элемент массива: '))
    F.append(value_f)

# Формирование матрица А и массивов AV, L
A = []
AV = []
L = []
for i in range(len(D)):
    A.append([])
    for j in range(len(F)):
        a = sin(D[i] + F[j])
        A[i].append(a)
b = 0
for x in range(len(A)):
    counter = 0
    av = 0
    for y in range(len(A[x])):
        if A[x][y] > 0:
            av += A[x][y]
            counter += 1
        if counter == 0:
            continue
        b = av / counter
    AV.append(b)
    for n in range(len(A[x])):
        if A[x][n] < b:
            L.append(A[x][n])

# for i in range(len(AV)):
#     A[i].append(AV[i])
#
# for x in range(len(A)):
#     for w in range(len(L)):
#         A[x].append(L[w])

for y in range(len(A)):
    for z in range(len(A[y])):
        print(f'{A[y][z]: ^10.4g}', sep='', end='')
    print()
