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


# записываем песню в файл
file1 = open(r"C:\test_file\lalala.txt", "w")
file1.write(song_func(end=1))
file1.close()

# Читаем прошло д/з
with open(r"C:\Users\Администратор\PycharmProjects\HomeWork\hw5_Task_1.py", "r", encoding="utf-8") as file2:
    print(file2.read())

# выводим на экран из файла + "!"
with open(r"C:\test_file\1.txt", "r", encoding="utf-8") as file3:
    while True:
        line = file3.readline().rstrip()
        if line:
            print(line + '!')
        else:
            break

print('-'*100)
# чтение и запись номерованных строк используя with as:
with open(r"C:\test_file\1.txt", "r", encoding="utf-8") as file4:
    with open(r"C:\test_file\num_txt.txt", "w", encoding="utf-8") as file5:
        while True:
            if file4.readline():
                for number, line in enumerate(file4.readlines(), 1):
                    file5.write(f'{number}. {line}')
            else:
                break


def from_file_to_int(file: str):
    """пытается преобразовать текст из файла в
    число. Файл должен все равно закрываться в блоке finally.
    Если преобразование удалось (в блоке else)
    выводится сообщение «I did it!»"""

    file6 = open(file, 'r', encoding='utf-8')
    try:
        convert_data = int(file6.read())
    except ValueError:
        print('это нельзя преобразовать в число')
    else:
        print('I did it!')
    finally:
        file6.close()


from_file_to_int(r'C:\test_file\5.txt')
