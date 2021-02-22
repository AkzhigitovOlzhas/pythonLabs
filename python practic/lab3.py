# def f1(s):
#     for i in s.split():
#         print(i, '-',len(i))
#
# f1(input('Введите строку: '))

def f2(*args):
    n = [args[i] ** args[i - 1] for i in range(1, len(args))]
    n.insert(0, args[0])
    return n


print(f2(1, 2, 3, 4))
