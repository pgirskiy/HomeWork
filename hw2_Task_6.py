print('Hello in Task_6\n')

a = int(input('введите первое число '))
b = int(input('введите второе число '))
c = int(input('введите последнее число '))

if a == b == c:
    print('Совпадает 3 числа')

elif a == b or b == c or a == c:
    print('Совпадает 2 числа')

else:
    print('совпадений нет')