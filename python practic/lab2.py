print(len(input('Введите предложение: ').split()))

str = input('Введите строку: ')
word = input('Введите слово которое нужно найти: ')
isFind = True
for i in str.split():
    if i == word:
        print('Введенное слово найденно: ' + i)
        isFind = False
        break
if isFind:
    print('Слово не удалось найти')

str = input('Введите строку: ')
str_array = str.split()
max_word = str_array[0]
for i in str_array:
    if len(i) < len(max_word):
        max_word = i

print(str_array)
print (max_word)

str = input('Введите строку: ')
str_array = str.split(';')
max_word = str_array[0]
for i in str_array:
    if len(i) > len(max_word):
        max_word = i

print(str_array)
print (max_word)

str = input('Введите строку: ')
str_array = str.split()
max_word = 0
for i in str_array:
    if len(i) > len(max_word):
        max_word = i
print(str_array)
print (max_word)