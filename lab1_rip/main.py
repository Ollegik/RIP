import math
import sys

print('Козинов Олег ИУ5-55Б')


def read():
    while 1:
        try:
            z = float(input())
            break
        except:
            print('Некорректный ввод')
    return z


if len(sys.argv) == 4:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except:
        print('Некорректный ввод в cmd')
        exit()
elif len(sys.argv) == 3:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print('Введите C: ')
    c = read()
elif len(sys.argv) == 2:
    a = float(sys.argv[1])
    print('Введите B: ')
    b = read()
    print('Введите C: ')
    c = read()
else:
    print('Введите A: ')
    a = read()
    print('Введите B: ')
    b = read()
    print('Введите C: ')
    c = read()
Disc = b**2 - 4 * a * c
if (Disc > 0) and (a != 0):
    x1 = (-b + math.sqrt(Disc)) / (2 * a)
    x2 = (-b - math.sqrt(Disc)) / (2 * a)
    if x1 > 0:
        print(math.sqrt(x1), -math.sqrt(x1), end=' ')
    elif x1 == 0:
        print(x1)
    if x2 > 0:
     print(math.sqrt(x2), -math.sqrt(x2))
    elif x2 == 0:
        print(x2)
    if (x1 < 0) and (x2 < 0):
        print('Корней нет')
elif (Disc > 0) and (a == 0):
    x = -c / b
    if x > 0:
        print(math.sqrt(x), -math.sqrt(x))
    elif x == 0:
        print(-x)
elif (Disc == 0) and (a == 0) and (c == 0):
    print('Корней бесконечно много')
else:
    print('Корней нет')