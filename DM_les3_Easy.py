#  Задание-1:
#  Напишите функцию, округляющую полученное произвольное десятичное число
#  до кол-ва знаков (кол-во знаков передается вторым аргументом).
#  Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
#  Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    if float(number) - int(number) > 0.5:
        print((int(number*10**ndigits)+1)/(10**ndigits))
    else:
        print(int(number*10**ndigits)/(10**ndigits))

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if len(ticket_number) % 2 == 1:
        return False
    elif sum(list(map(int, str(ticket_number)[:len(ticket_number) // 2]))) == \
            sum(list(map(int, str(ticket_number)[len(ticket_number) // 2:]))):
        return True
    else:
        return False

print(lucky_ticket('123006'))
print(lucky_ticket('12321'))
print(lucky_ticket('436751'))

while True:
    try:
        print(lucky_ticket(input('Введите число')))
        break
    except ValueError:
        print("Вы ввели не число")
