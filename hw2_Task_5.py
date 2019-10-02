print('Hello in Task_5\n')

user_dig = input('введите три числа ')

# если в качестве разделителя указали пробел
if user_dig.count(' '):
    user_list = list(user_dig.split(' '))

# если в качестве разделителя указана запятая
if user_dig.count(','):
    user_list = list(user_dig.split(','))

user_list.sort()

a, b, c = user_list
print('a =', a)
print('b =', b)
print('c =', c)