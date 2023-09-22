import random
import timeit


# Проверка на целое число
def check_int(x: str):
    if not x:
        return False
    x = x.replace('_', '')
    if x[0] == '-' or x[0] == '+':
        x = x[1:]
    return x.isdigit()


print('Часть 1')
print()

# Заполнение массива
array = []
n = input('Введите количество добавляемых элементов: ')
while not n.isdigit():
    n = input('Введите количество добавляемых элементов: ')
n = int(n)

for i in range(n):
    value = input(f'Введиите {i + 1} - й добавляемый элемент: ')
    while not check_int(value):
        value = input(f'Введиите {i + 1} - й добавляемый элемент: ')
    value = int(value)
    array.append(value)
print()


# Функция сортировки методом ставки бинарным поиском
def sort_bin_search(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        low = 0
        high = k
        if low == high:
            low += 1
        else:
            while low < high:
                mid = (low + high) // 2
                if cur < arr[mid]:
                    high = mid
                else:
                    low = mid + 1
        j = k
        while j > low and j > 0:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[low] = cur
    return arr


print(sort_bin_search(array))

print()
print('Часть 2')
print()


# Функция замера времени для сортировки методом ставки бинарным поиском
def sort_bin_time(arr):
    start = timeit.default_timer()
    sort_bin_search(arr)
    end = timeit.default_timer()
    seconds = end - start
    return seconds

# Размерности для упорядоченных списков
n1_arr1 = input('Введите размерность для первого списка: ')
while not n1_arr1.isdigit():
    n1_arr1 = input('Введите размерность для первого списка: ')
n1_arr1 = int(n1_arr1)

n2_arr2 = input('Введите размерность для второго списка: ')
while not n2_arr2.isdigit():
    n2_arr2 = input('Введите размерность для второго списка: ')
n2_arr2 = int(n2_arr2)

n3_arr3 = input('Введите размерность для третьего списка: ')
while not n3_arr3.isdigit():
    n3_arr3 = input('Введите размерность для третьего списка: ')
n3_arr3 = int(n3_arr3)


def generate_sorted_list(n1):
    list = []
    for i in range(1, n1 + 1):
        list.append(i)
    return list

sorted_arr1 = generate_sorted_list(n1_arr1)
sorted_arr2 = generate_sorted_list(n2_arr2)
sorted_arr3 = generate_sorted_list(n3_arr3)

print()


# Генерация случайных списков
def generate_random_list(n1):
    list = []
    for i in range(n1):
        list.append(i)
    return list

random_arr1 = generate_random_list(n1_arr1)
random_arr2 = generate_random_list(n2_arr2)
random_arr3 = generate_random_list(n3_arr3)


def generate_sorted_reversed_list(n1):
    list = []
    for i in range(n1, 0, -1):
        list.append(i)
    random.shuffle(list)
    return list

sort_arr1_reversed = generate_sorted_reversed_list(n1_arr1)
sort_arr2_reversed = generate_sorted_reversed_list(n2_arr2)
sort_arr3_reversed = generate_sorted_reversed_list(n3_arr3)
print()


# Вывод таблицы с замером времени
print('|------------------------------------------------------------------------------------------------------------------------|')
print('|                                                    |          N1          |           N2         |          N3         |')
print('|------------------------------------------------------------------------------------------------------------------------|')
print(f'| Упорядоченный список                               |         {sort_bin_time(sorted_arr1):^9.4g}    |         {sort_bin_time(sorted_arr2):^9.4g}    |         {sort_bin_time(sorted_arr3):^9.4g}   |')
print('|------------------------------------------------------------------------------------------------------------------------|')
print(f'| Случайный список                                   |         {sort_bin_time(random_arr1):^9.4g}    |         {sort_bin_time(random_arr2):^9.4g}    |         {sort_bin_time(random_arr3):^9.4g}   |')
print('|------------------------------------------------------------------------------------------------------------------------|')
print(f'| Упорядоченный список в обратном порядке            |         {sort_bin_time(sort_arr1_reversed):^9.4g}    |         {sort_bin_time(sort_arr2_reversed):^9.4g}    |         {sort_bin_time(sort_arr3_reversed):^9.4g}   |')
print('|------------------------------------------------------------------------------------------------------------------------|')


