print('Hello in Task_4\n')

user_side = input('введите три стороны треугольника ')

# если в качестве разделителя пробел
if user_side.count(' '):
    side_list = list(user_side.split(' '))

# если в качестве разделителя запятая
if user_side.count(','):
    side_list = list(user_side.split(','))

a, b, c = side_list

if (a + b) > c and (b + c) > a and (a + c) > b:
    print('треугольник существует')
else:
    print('треугольник не существует')
if a == b == c != 0:
    print('Треугольник равносторонний')
