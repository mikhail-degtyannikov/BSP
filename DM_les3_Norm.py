__author__ = 'Дегтянников Михаил Александрович'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
def fibonacci(n, m):

    a, b = 1, 1
    fbnc = [1, ]

    for i in range(m):
        a, b = b, a + b
        fbnc.append(a)

    return fbnc[n - 1:m]

x = int(input('введите первую цифру ряда фибоначчи '))
y = int(input('введите вторую цифру ряда фибоначчи '))
print('fibonacci вида(x, y): ', fibonacci(x, y))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    if len(origin_list) > 1:
        base = len(origin_list) // 2
        first = []
        last = []
        for x, y in enumerate(origin_list):
            if x != base:
                if y < origin_list[base]:
                    first.append(y)
                else:
                    last.append(y)
        sort_to_max(first)
        sort_to_max(last)
        origin_list[:] = first + [origin_list[base]] + last
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(f, i):
    return (val for val in i if f(val))


print(list(my_filter(lambda x: True if x % 2 != 0 else False,[100, 200, 333, 4444, 543, 6000, -7, 81])))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_parallelogram(a1_x, a1_y, a2_x, a2_y, a3_x, a3_y, a4_x, a4_y):
    if (a3_x - a2_x) == (a4_x - a1_x) and \
            (a2_y - a1_y) == (a3_y - a4_y):
        print('rfsdsd')
    print('no')


is_parallelogram(
a1_x = abs(float(input('введите х1'))),
a1_y = abs(float(input('введите y1'))),
a2_x = abs(float(input('введите х2'))),
a2_y = abs(float(input('введите y2'))),
a3_x = abs(float(input('введите х3'))),
a3_y = abs(float(input('введите y3'))),
a4_x = abs(float(input('введите х4'))),
a4_y = abs(float(input('введите y4'))))