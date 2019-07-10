# coding=utf-8
__author__ = 'Дегтянников Михаил Александрович'


task = ""
answer = "нет" or "Нет" or "No" or "no"
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
        if qws1 == answer:
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
        if qws2 == answer:
            print('Goodbye')
            break
    elif task == '3':
        input("К сожалению моего мозга не зватает решать такие задачи, Увы :) ")
        qws3 = input("хотите продолжить?")
        if qws3 == answer:
            print('Goodbye')
            break
#    else:
#        print('определитесь чего вы хотите')
#        print("Досвидания")
    else:
        continue