# coding=utf-8
__author__ = 'Дегтянников Михаил Александрович'


task = ""
answer = ["нет", "Нет", "No", "no"]
while task != answer:
    print("Домашнее задание")
    print("Задача №1 - Вывести поочередно цифры исходного числа")
    print("Задача №2 - Поменять местами переменные и вывести на экран")
    print("Задача №3 - Запросить возраст и определить доступ")
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
        while number:
            ls.append(number % 10)
            number //= 10
        print(list(ls))
        qws1 = input("хотите продолжить? ")
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
        let3 = let1
        let1 = let2
        let2 = let3
        print("Первое число  ", let1)
        print("Второе число  ", let2)
        qws2 = input("хотите продолжить? ")
        if qws2 in answer:
            print('Goodbye')
            break
    elif task == '3':
        old = int(input("Пожалуйста, скажите сколько Вам лет  "))
        if old >= 18:
            print("Доступ разреш")
        else:
            print("Извините, пользование данным ресурсом только с 18 лет")
        qws3 = input("хотите продолжить? ")
        if qws3 in answer:
            print('Goodbye')
            break
    else:
        continue