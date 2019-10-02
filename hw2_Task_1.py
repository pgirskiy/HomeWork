print('Hello in Task_1\n')

u_input = input('Введите любую строку\n')

#Проверяем введенные данные
if u_input.isdigit():
    print('Вы ввели число!\n')

if ' ' in u_input:
    print('В введенной строке', u_input.count(' '), 'пробелов\n')

if '.' in u_input:
    print('В введенной строке', u_input.count('.'), 'симовлов "."\n')
elif not u_input.isdigit():
    print('В вашей строке нет точек\n')

#Строка из 100 симоволов с текстом по средине
HW_STR = 'homework'

print('-' *100,)
print(HW_STR.center(100, ' '))
print('-' *100, '\n')