# coding=utf-8
__author__ = 'Дегтянников Михаил Александрович'

import math

task = ""
answer = ["нет", "Нет", "No", "no"]
while task != answer:
    print("Домашнее задание")
    print("Задача №1 - вывести самую большую цифру введеного числа")
    print("Задача №2 - Поменять местами переменные и вывести на экран")
    print("Задача №3 - Вычислить корни квадратного уравнения вида ax² + bx + c = 0")
    task = input('Выберите задачу для проверки ДЗ - 1/2/3  ')
    if task == '1':
        print('Задача №1')
        while True:
            try:
                number = int(input("Введите число:  "))
                break
            except ValueError:
                print("Вы ввели не число")
        ls = []
        while number > 10:
            ls.append(number % 10)
            number //= 10
        m = max(ls)
        input("Максимальное число " + str(m))
        qws1 = input("хотите продолжить?")
        if qws1 in answer:
            print('Goodbye')
            break

    elif task == '2':
        while True:
            try:
                let1 = int(input('Введите первое число:  '))
                break
            except ValueError:
                print("Вы ввели не число")
        while True:
            try:
                let2 = int(input('Введите второе число:  '))
                break
            except ValueError:
                print("Вы ввели не число")
        let1, let2 = let2, let1
        print("Первое число  ", let1)
        print("Второе число  ", let2)
        qws2 = input("хотите продолжить?")
        if qws2 in answer:
            print('Goodbye')
            break
    elif task == '3':
        a = float(input("Введите а - "))
        b = float(input("Введите b - "))
        c = float(input("Введите c - "))
        if a == 0:
            if b == 0:
                print('введенные значения не соответствуют, т.к. равны нулю')
            else:
                x1 = 0
                x2 = -c / b
                print('X1 = ' + str(x1))
                print('X2 = ' + str(x2))

        elif c == 0:
            x = -b / a
            print('X = ' + str(x))
        elif b == 0:
            x = -c / a
            if x >= 0:
                print('Выражение имеет два конря +' + str(x))
                print('Выражение имеет два конря -' + str(x))
            else:
                print('уравнение во множестве действительных числе не имеет решений')
#  решаем полное квадратное уравнение
        else:
#  D > 0
            d = b**2 - 4*a*c
            if d > 0:
                d = math.sqrt(d)
                x1 = (-b + d) / (2 * a)
                x2 = (-b - d) / (2 * a)
                print("d > 0")
                print('x1 =  ' + str(x1))
                print('x2 =  ' + str(x2))
#  D = 0
            elif d == 0:
                x2 = -b / (2*a)
                x1 = x2
                print ('два двукратных корня, d = 0')
                print('x1 =  ' + str(x1))
                print('x2 =  ' + str(x2))

#  D < 0
            else:
                print("Уравнение не имеет корней, т.к. d < 0")


        qws3 = input("хотите продолжить?")
        if qws3 in answer:
            print('Goodbye')
            break
    else:
        continue