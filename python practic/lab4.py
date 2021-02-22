import os
import time
import random


def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def task1():
    path = input("Введите путь к папкам: ")
    file = input("Введите название папки/файла: ")
    if os.path.exists(path + '\\' + file):
        print(os.path.abspath(path + '\\' + file))
        if os.path.isdir(path + '\\' + file):
            print('-', get_size(path + '\\' + file), 'байт')
            print('-', get_size(path + '\\' + file) / (1024 * 1024), 'мегабайт')
        else:
            print('-', os.path.getsize(path + '\\' + file), 'байт')
            print('-', os.path.getsize(path + '\\' + file) / (1024 * 1024), 'мегабайт')
    print("- Директория" if os.path.isdir(path + '\\' + file) else "- Файл")
    print('- Дата создания: ', time.ctime(os.path.getctime(path + '\\' + file)))
    print('- Дата последнего изменения: ', time.ctime(os.path.getmtime(path + '\\' + file)))


print(input('Введите свой вопрос: '), '-',
      random.choice(['да', 'нет', 'возможно', 'незнаю', 'правильно', 'неправильно']))
