# Домашнее задание к лекции 2.1 «Функции — использование встроенных и создание собственных»
#
# Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять
# ни один документ. Каталог документов хранится в следующем виде:

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

# Перечень полок, на которых находятся документы хранится в следующем виде:

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people():  # people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
    number_input = input('Номер документа: ')
    found = 0
    for search_people in documents:
        if number_input in search_people.values():
            print(search_people['name'])
            found += 1
    if found == 0:
        print('Документ с таким номером не обнаружен!')


def all_docs():  # l-  команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
    for doc_list in documents:
        print(doc_list["type"], '"' + doc_list["number"] + '"', '"' + doc_list["name"] + '"')


def shelf():  # s - команда, которая спросит номер документа и выведет номер полки, на которой он находится
    number_input = input('Введите номер документа: ')
    stop_word = False
    for shelf_dir in directories.items():
        for num_doc in shelf_dir[1]:
            if num_doc == number_input:
                print('Документ на полке -', shelf_dir[0])
                stop_word = True
                break
        if stop_word == True:
            break
    else:
        print('Такого номера документа нет в базе.')


def add():  # a – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя')
    for add_command in documents and directories:
        directories_num_input = input('Введите номер полки для добавления документа: ')
        if int(directories_num_input) == 1 or int(directories_num_input) == 2 or int(directories_num_input) == 3:
            number_input = input('Введите номер документа: ')
            type_doc_input = input('Введите тип нового документа: ')
            name_doc_input = input('Введите имя владельца документа: ')
            documents.append({"type": type_doc_input, "number": number_input, "name": name_doc_input})
            directories[directories_num_input].append(number_input)
            break
        else:
            print('Введенной полки не существует')
            break
    print(directories)
    print(documents)


def main():  # главное меню
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            people()
        elif user_input == 'l':
            spisok()
        elif user_input == 's':
            shelf()
        elif user_input == 'a':
            add()
        elif user_input == 'q':
            print('До свидания')
            break


main()  # Запуск связующей функции

'''
Задача №1

Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя
владельца и номер полки, на котором он будет храниться.
Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное
название, передающие её действие.


Задача №2. Дополнительная (не обязательная)

d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
Задача №3

Почитать про lambda-функции. И что такое *args и **kwargs.
'''