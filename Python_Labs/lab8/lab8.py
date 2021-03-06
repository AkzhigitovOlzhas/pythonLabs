# Найдите индексы первого вхождения максимального элемента. Выведите два
# числа: номер строки и номер столбца, в которых стоит наибольший элемент в
# двумерном массиве. Если таких элементов несколько, то выводится тот, у которого
# меньше номер строки, а если номера строк равны то тот, у которого меньше номер
# столбца.
# Программа получает на вход размеры массива n и m, затем n строк по m чисел в
# каждой.
n1 = int(input('Введите кол-во строк в массиве: '))
n2 = int(input('Введите кол-во столбцов в массиве: '))
a = [[input() for i in range(n2)] for j in range(n1)]

print('List: ')
for i in a:
    for j in i:
        print(j, end=' ')
    print()

max_num = a[0][0]
max_index = [0, 0]
for i in range(0, n1):
    for j in range(0, n2):
        if max_num < a[i][j]:
            max_index[0] = i
            max_index[1] = j
            max_num = a[i][j]

print('Max:', max_num)
print('Max-index:', max_index)

# Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив
# его символами "." (каждый элемент массива является строкой из одного символа).
# Затем заполните символами "*" среднюю строку массива, средний столбец
# массива, главную диагональ и побочную диагональ. В результате единицы в
# массиве должны образовывать изображение звездочки. Выведите полученный
# массив на экран, разделяя элементы массива пробелами.
n = int(input('Введите число n: '))
a = [['.' for i in range(n)] for j in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[i][-i - 1] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'

for i in a:
    for j in i:
        print(j, end=' ')
    print()

# Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его
# символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять
# точка.
n = int(input('Введите n: '))
m = int(input('Введите m: '))
a = [['*' for i in range(n)] for j in range(m)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i][j] = '.'
for i in a:
    print(' '.join(i))

# # Дано число n. Создайте массив размером n×n и заполните его по следующему
# # правилу. На главной диагонали должны быть записаны числа 0. На двух
# # диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях
# # числа 2, и т.д.
n = int(input())
a = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))

# # Дано число n. Создайте массив размером n×n и заполните его по следующему
# # правилу:
# # • Числа на диагонали, идущей из правого верхнего в левый нижний угол равны
# # • Числа, стоящие выше этой диагонали, равны 0.
# # • Числа, стоящие ниже этой диагонали, равны 2.
# # Полученный массив выведите на экран. Числа в строке разделяйте одним
# # пробелом.
n = int(input())
a = [['0' if j < n - 1 - i else '2' for i in range(n)] for j in range(n)]

for i in range(n):
    a[i][-i - 1] = '1'

for i in a:
    print(' '.join(i))

