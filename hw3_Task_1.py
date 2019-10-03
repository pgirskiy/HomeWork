def task_menu(opt_menu):
    """
    :param opt_menu: dict, where 'number:txt'
    :return: user choice - key from dict
    """
    try:
        opt_menu == dict(opt_menu)
    except TypeError:
        print('TypeError Нужно передать "dict"')
        return
    except ValueError:
        print('ValueError Нужно передать "dict"')
        return
    else:
        opt_menu['0'] = 'Выход'
        user_choice = None
        while not user_choice:
            print('-' * 20)
            for key, value in opt_menu.items():
                print('Введите', key, ' - для', value)
            print('-' * 20)
            user_choice = user_dic_choice(opt_menu)
        return user_choice


def user_fl_input(message='Введите действительное число'):
    '''
    :param message: message to input
    :return: float user input
    '''
    while True:
        try:
            val = float(input(message))
        except ValueError:
            print('это не действительное число\n')
        else:
            return val


def user_dig_input(message='Введите целое число', min_d=0, max_d=9999999):
    """
    :param message: user txt message
    :param min_d: min number
    :param max_d: max number
    :return: user number
    """
    while True:
        try:
            val = int(input(message))
        except ValueError:
            print('это не целое число\n')
        else:
            if val in range(min_d, max_d):
                return val
            else:
                print('число за пределами диапазона')


def user_str_input(message='Введите текст', min_s=0, max_s=9999999):
    """
    :param message: user txt message
    :param min_s: min str len
    :param max_s: max str len
    :return: user str
    """
    while True:
        val = input(message)
        l_val = len(val)
        if l_val < min_s:
            print('Слишком короткая строка. Минимальная длинна', min_s, 'символов')
        elif l_val > max_s:
            print('Слишком длинная строка. Максимальная длинна', max_s, 'символов')
        else:
            return val


def user_dic_choice(user_dict, message=''):
    """
    :param user_dict: dict
    :param message: user message str
    :return: user choice key - from dic
    """
    val = input(message)
    if val in user_dict.keys():
        return val
    else:
        print('такого значения нет')
        return


def user_str_nsp(message='Введите текст'):
    '''
    :param message: txt message
    :return: user input str without ' '
    '''
    while True:
        a = input(message)
        if not a.strip(' ').count(' '):
            return a


def is_year_leap(year):
    '''
    :param year: year
    :return: True or False
    '''
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def is_triangle(a, b, c,):
    '''
    :param a: side a
    :param b: side b
    :param c: side c
    :return: True or False
    '''
    if (a + b) > c and (b + c) > a and (a + c) > b:
        return True
    else:
        return False


def full_triangle_info(a, b, c,):
    '''
    :param a: side a
    :param b: side b
    :param c: side c
    :return: txt string
    '''
    if (a + b) > c and (b + c) > a and (a + c) > b:
        if a == b == c:
            return 'равносторонний'
        elif a == b or a == c or b == c:
            return 'равнобедренный'
        else:
            return 'разносторонний'
    else:
        return None


def distance(x1, y1, x2, y2):
    '''
    :param x1: int
    :param y1: int
    :param x2: int
    :param y2: int
    :return: result int
    '''
    d = ((x2-x1)**2+(y2-y1)**2)**0.5
    return d



def task_1():
    user_str1 = user_str_input('Введите строку\n', 5, 12)

    # Хотя ввод и заранее ограничен, нужен try согластно задаче
    try:
        print(user_str1[2], '\n',
              user_str1[-2], '\n',
              user_str1[0:5], '\n',
              user_str1[0:-2], '\n',
              user_str1[0::2], '\n',
              user_str1[1::2], '\n',
              user_str1[::-1], '\n',
              user_str1[-1::-2], '\n',
              user_str1[-2::-2], '\n',
              user_str1[-2:0:-1], '\n',
              len(user_str1))
    except IndexError:
        print('Нет символа для индексации')


def task_2():
    user_str1 = user_str_input('Введите строку\n')

    user_str1_l = len(user_str1) + 1  # Добавляем 1 к длинне строки, чтоб при делении первая часть была больше
    a = user_str1[(user_str1_l // 2):] + user_str1[:(user_str1_l // 2)]  # Делим и срезаем наоборот
    print(a)


def task_3():
    # Счетчик от 0 до 10
    user_c1 = 0
    while user_c1 < 11:
        print(user_c1, end=' ')
        user_c1 += 1

    print('\n', '-' * 20)

    # Счетчик от 20 до 1
    user_c1 = 20
    while user_c1 != 0:
        print(user_c1, end=' ')
        user_c1 -= 1

    print('\n', '-' * 20)

    # Если число четное уменьшаем в половину и считаем количество делений
    user_c1 = 0
    user_dig = user_dig_input('Введите целое четное число')

    if user_dig % 2 == 1:
        print('число', user_dig, 'не четное')
    else:
        while user_dig % 2 == 0:
            user_dig /= 2
            user_c1 += 1
        print('Число можно поделить надвое без остатка', user_c1, 'раз')


def task_4():
    # Выводим элемент списка и удаляем
    u1 = [1, 15, 67, 44, 83, 312, 60, 148, 130, 11, 24, 140, 18]
    while u1:
        print(u1.pop(0), end=' ')

    print('\n', '-' * 20)

    # Выводим первый симовл строки и создаем новую строку без него
    u2 = 'Строка из нескольких слов для задания 4'
    while u2:
        print(u2[0], end=' ')
        u2 = u2[1:]

    print('\n', '-' * 20)

    # Выводит элемент списка и удаляет по возрастанию
    u3 = [1, 15, 67, 44, 83, 312, 60, 148, 130, 11, 24, 140, 18]
    u3.sort()
    while u3:
        print(u3.pop(0), end=' ')

    print('\n', '-' * 20)

    # Сравниваем числа в последовательности и считаем повторения подряд
    u4 = [15, 48, 59, 140, 140, 140, 72, 72, 10, 10, 96, 40, 0]
    prev_val = 0
    cur_i = 0
    max_i = 0

    for u4_val in u4:
        if u4_val == prev_val:
            cur_i += 1
        else:
            prev_val = u4_val
            max_i = max(max_i, cur_i)
            cur_i = 1
    print('Число повторяется', max_i, 'раз подряд')


def task_5():
    a = user_str_input('Введите первое значение\n')
    b = user_str_input('Введите второе значение\n')

    # Если введенные значения числа складывавем, если хоть один не число - конкатенация
    try:
        c = int(a) + int(b)
    except ValueError:
        c = str(a) + str(b)
    print('Результат:', c)


def task_6():
    print(user_str_nsp('Введите текст без пробелов\n'))

    leap_year = user_dig_input('Введите год\n', 1, 3025)
    if is_year_leap(leap_year):
        print('Этот год высокосный')
    else:
        print('Этот год не высокосный')

    #Существует ли треугольник
    a = user_dig_input('Введите первую сторону\n')
    b = user_dig_input('Введите вторую сторону\n')
    c = user_dig_input('Введите третью сторону\n')
    if is_triangle(a, b, c):
        print('Треугольник существует')
    else:
        print('Треугольник не существует')

    #Тип треугольника
    full_tr_inf = full_triangle_info(a, b, c)
    if full_tr_inf:
        print('Треугольник', full_tr_inf)

    print('\nНаходим растоние между x1y1 и x2y2\n')
    x1 = user_fl_input('Введите значение x1 ')
    y1 = user_fl_input('Введите значение y1 ')
    x2 = user_fl_input('Введите значение x2 ')
    y2 = user_fl_input('Введите значение y2 ')
    print('Растояние', distance(x1, y1, x2, y2))


def task_7():
    pass


#Задания согластно ДЗ
all_tasks = {'1': 'Задание 1 (срез строки)', '2': 'Задание 2 (деление строки)', '3': 'Задание 3 (while)',
             '4': 'Задание 4 (список)', '5': 'Задание 5 (Исключение)', '6': 'Задание 6 (функции)',
             '7': 'Задание 7 (строки)'}

user_task_choice = task_menu(all_tasks)

if user_task_choice == '1':
    task_1()
elif user_task_choice == '2':
    task_2()
elif user_task_choice == '3':
    task_3()
elif user_task_choice == '4':
    task_4()
elif user_task_choice == '5':
    task_5()
elif user_task_choice == '6':
    task_6()
elif user_task_choice == '7':
    task_7()
elif user_task_choice == '0':
    print('Выход')
else:
    print('Произошла неизвестная ошибка')

