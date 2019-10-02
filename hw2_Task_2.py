print('Hello in Task_2\n')

print('-' * 20)
print('''Дано: Прямоугольный треугольник с сторонами 179 и 971
Найти: гипотенузу''')
print('-' * 20)
print('a^2 + b^2 = c^2')
print('-' * 20)

a = 179
b = 971
c = (a**2 + b**2)**0.5
print('Гипотенуза = ', round(c, 3))

print('-' * 20)
print('''Дано: Двузначное число
Найти: число десятков в нем''')
print('-' * 20)

user_dig2 = input('Введите двузначное число:\n')

if 9 < int(user_dig2) < 100:
    print('В числе', str(user_dig2)[0], 'десятков')
else:
    print('Введено не правильное значение')

print('-' * 20)
print('''Дано: Трехзначное число
Найти: сумму его цифр''')
print('-' * 20)

user_dig3 = input('Введите трехзначное число:\n')

if int(user_dig3) in range(100, 1000):
    l = list(user_dig3)
    i = 0
    for dig in list(user_dig3):
        i += int(dig)
    print('Сумма всех элементов числа =', i)
else:
    print('не правильное значение')

print('-' * 20)
print('''Дано: Целое число
Найти: следующее за ним чётное число''')
print('-' * 20)

user_dig4 = input('Введите любое число:\n')

if int(user_dig4) % 2 == 0:
    print('следующее четное число = ', int(user_dig4) + 2)
elif int(user_dig4) % 2 == 1:
    print('следующее четное число = ', int(user_dig4) + 1)
else:
    print('Введено не верное значение')

print('-' * 20)
print('''Дано: Действительное число Х
Найти: его дробную часть''')
print('-' * 20)

user_dig5 = float(input('введите дробное число\n'))
print('дробная часть ', (user_dig5 - int(user_dig5)))

print('-' * 20)
print('''Дано: Действительное число Х
Найти: первое число после точки''')
print('-' * 20)

user_dig6 = float(input('введите дробное число\n'))
print('число после точки ', int((user_dig6 * 10) % 10))