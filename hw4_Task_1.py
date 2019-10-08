import re
# импортируем свой файл (задание 4)
import hw4_letters_only as l_filter


def song_func(i=3, j=3, end=0) -> str:
    """
    :param i: int - string count
    :param j: int - 'la' count
    :param end: int - 0 or 1
    :return: song str
    Create a famous song la la la with a given repetitions count
    """
    song = ('-'.join(['la'] * j) + '\n') * i
    if end:
        return song[:-1] + '!'
    else:
        return song[:-1] + '.'


def next_big_number(*args):
    """
    :param args: any args
    :return: 2-th sorted arg
    Defines the second highest value.
    """
    s = sorted(set(args))
    return s[1]


def letters_only(a: str) -> str:
    """
     :param a: string
     :return: filtered str
     Using regular expressions, this function filter all characters except Latin
     """
    let = re.sub(r"[^a-zA-Z]", "", a)
    assert let.isalpha()
    return let


# Задание 1: функция возвращает песню с заданным числом повторов
print(song_func(6, 6, 1))

# Задание 2: Функция выводит второе по возрастанию значение, с учетом повторов
print(next_big_number(1, 90, 1, 90, 5, 7, 11, 45, 10))

# Задание 3: функция удаляет из строки всё кроме символов латинского алфавита
letters_only('t3+-(*)(*e*&&%^s&^%$%t^')

# Задание 4.1
a_list = [2 ** n for n in range(20)]

# Задание 4.2
a_list = [3, 7, 9, 44, 18, 343, 325, 324, 223, 113, 453, 564]
b_list = [x % 3 for x in a_list]

# Задание 4.3
a_list = [['test', 'new'], 7, 9, 'la-la-la', 18, 'sss', 343, {'1': 'one', '2': 'test2'}, 324, 223, 113, 453, 564]
b_list = [x for x in a_list if isinstance(x, int)]

# Задание 4.4 (Импортировал функцию letters_only второй раз, с новым именем, так-как того требует задание)
a_list = [['test', 'new'], 't*(&%e37^s@#t', 9, 'la-la-la', 18, 's%s_0s', 343, {'1': 'one'}, 453, 564]
b_list = [l_filter.letters_only(x) for x in a_list if isinstance(x, str)]

# Задание 4.5
a_dic = {'name': 'Andrey',
         'surname': 'Ivanov',
         'age': 20,
         'position': 'tester',
         'address': 'London-23',
         'skills': 'test'}

b_dic = {x: type(y) for x, y in a_dic.items()}
c_dic = {x: letters_only(y.lower()) for x, y in a_dic.items() if isinstance(y, str)}

