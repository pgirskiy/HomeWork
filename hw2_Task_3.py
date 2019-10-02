print('Hello in Task_3\n')

print('Проверка года на высокосность\n')

user_year = int(input('Введите интересующий вас год '))

if user_year % 4 == 0 or user_year % 400 == 0 and user_year % 100 != 0:
    print('Yes')
else:
    print('No')