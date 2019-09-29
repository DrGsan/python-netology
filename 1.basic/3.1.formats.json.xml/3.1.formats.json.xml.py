task_discription = """Домашнее задание к лекции 3.1 «Работа с разными форматами данных»

Взять из папки 3.1.formats.json.xml файлы с новостями newsafr.json и newsafr.xml
Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов
для каждого файла.
Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(),
sort или sorted.
Задача №1: написать программу для файла в формате json.
Задача №2: написать программу для файла в формате xml."""


def homework(home_work_name, distance_default):
    distance = int((distance_default - len(home_work_name)) / 2)
    if len(home_work_name) % 2 == 0:
        y = 0
    else:
        y = 1
    x = ('\n' + distance * '-' + home_work_name + (distance + y) * '-')
    print(x)


def task(task_number, distance_default):
    name = 'Задача № '
    distance = int((distance_default - len(name) - len(task_number)) / 2)
    if len(task_number) % 2 == 0:
        y = 1
    else:
        y = 0
    x = (distance * '-' + name + task_number + (distance + y) * '-')
    print('\n' + x + '\n')


def json_part(file):
    import json
    # from pprint import pprint
    with open(file) as read_file:
        data = json.load(read_file)
    # pprint(data)  # Проверка файла json
    words_from_discription = list()
    for i in data['rss']['channel']['items']:
        split_discription = list(i['description'].lower().split(' '))
        words_from_discription += split_discription
        six_words_list = list()
        for six_words in words_from_discription:
            if len(six_words) > 6:
                six_words_list.append(six_words)
        six_words_list.sort()
    # print(six_words_list)  # Список слов из описания
    from collections import Counter
    six_words_dict = dict(Counter(six_words_list))
    # pprint(six_words_dict)  # Словарь с количеством повторяющихся слов
    n = 1
    for k in sorted(six_words_dict, key=six_words_dict.get, reverse=True):  # Сортировка словаря
        if n <= 10:
            print('{2}. Слово "{0}". Количество повторений - {1}.'.format(k.upper(), six_words_dict[k], n))
            n += 1


def xml_part(file):
    import xml.etree.ElementTree as ET
    # from pprint import pprint
    tree = ET.parse(file)
    discriptions = tree.findall('channel/item/description')
    words_from_discription = list()
    for i in discriptions:
        split_discription = list(i.text.lower().split(' '))
        words_from_discription += split_discription
        six_words_list = list()
        for six_words in words_from_discription:
            if len(six_words) > 6:
                six_words_list.append(six_words)
        six_words_list.sort()
    # pprint(six_words_list)  # Список слов из описания
    from collections import Counter
    six_words_dict = dict(Counter(six_words_list))
    # pprint(six_words_dict)  # Словарь с количеством повторяющих ся слов
    n = 1
    for k in sorted(six_words_dict, key=six_words_dict.get, reverse=True):  # Сортировка словаря
        if n <= 10:
            print('{2}. Слово "{0}". Количество повторений - {1}.'.format(k.upper(), six_words_dict[k], n))
            n += 1


def menu():
    homework('Домашнее задание к лекции 3.1 «Работа с разными форматами данных»', 100)
    print('\nЗдравствуйте!')
    print('\nПеред вам меню взаимодействия\n'
          'Чтобы передвигаться по меню введите символ (без ковычек)\n'
          '"1" - просмотр первого задания\n'
          '"2" - просмотр второго задания\n'
          '"h" - отобразить текст задания\n'
          '"q" - закончить выполнение кода\n')
    stop_program = False
    while not stop_program:
        ask = input('')
        if ask == '1':
            task('1 (json)', 100)
            json_part('tasks/3.1.formats.json.xml/newsafr.json')
            button = input('\nНажмите enter чтобы вызвать меню')
            menu()
        elif ask == '2':
            task('2 (xml)', 100)

            xml_part('tasks/3.1.formats.json.xml/newsafr.xml')
            button = input('Нажмите enter чтобы вызвать меню')
            menu()
        elif ask == 'h' or ask == 'H':
            print(task_discription)
            button = input('\nНажмите enter чтобы вызвать меню')
            menu()
        elif ask == 'q' or ask == 'Q':
            print('Досвидания!\n')
            print('-' * 27)
            print('--> Программа завершена <--')
            stop_program = True
        else:
            print('Вы явно что-то делаете не так')
            button = input('\nНажмите enter чтобы вызвать меню')
            menu()


# homework('Домашнее задание к лекции 3.1 «Работа с разными форматами данных»', 100)
# task('1 (json)', 100)
# json_part('tasks/3.1.formats.json.xml/newsafr.json')
# task('2 (xml)', 100)
# xml_part('tasks/3.1.formats.json.xml/newsafr.xml')
menu()