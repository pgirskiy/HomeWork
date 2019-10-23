
#Читаем из одного файла текст, записываем в другой слова по алфавиту и считаем совпадения

with open(r'C:\test_file\1.txt', 'r', encoding='utf-8') as s_file:
    words = [word for line in s_file for word in line.split()]
    words.sort()
    with open(r'C:\test_file\sort_list.txt', 'w', encoding='utf-8') as w_file:
        for item in words:
            w_file.write(f'{item} | count: {words.count(item)}\n')

