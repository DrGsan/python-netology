class Contact:
    def __init__(self, name, surname, number, chosen=False, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        self.other = kwargs
        self.other_print = '     нет\n'
        self.chosen = chosen

    def __str__(self):
        if self.other:
            self.other_print = ''
            for key, value in self.other.items():
                self.other_print += ('     {}: {}\n'.format(key, value))

        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Телефон: {self.number}\n' \
               f'Дополнительная информация:\n{self.other_print}'


class NumBook(object):

    def __init__(self, namebook):
        self.namebook = namebook
        self.abonents = []

    def __str__(self):
        print(f'\n---Телефонная книга "{self.namebook}"---')
        str_book = ''
        for num, abonent in enumerate(self.abonents, 1):
            str_book += f"{num}.\n{str(abonent)}"
        return str_book

    def add_abonent(self, abonent):
        self.abonents.append(abonent)

    def del_abonent(self, number):
        del_list = []
        for abonent in self.abonents:
            if abonent.number == number:
                del_list.append(abonent)
        print("\n---Удаленные абоненты---\n", ', '.join(list(map(lambda x: f'{x.name} {x.surname}', del_list))))
        list(map(lambda x: self.abonents.remove(x), del_list))

    def find_num_abonent(self, number):
        find_list = []
        for abonent in self.abonents:
            if abonent.number == number:
                find_list.append(abonent)
        if not find_list:
            find_list.append("не дал результатов")
        print(f"\n--Поиск по номеру {number}---\n" + '\n'.join(list(map(lambda x: f'{str(x)}', find_list))))

    def find_chosen_abonent(self):
        find_list = []
        for abonent in self.abonents:
            if abonent.chosen == True:
                find_list.append(abonent)
        if not find_list:
            find_list.append("Поиск не дал результатов")
        print("\n---Избранные абоненты---\n" + '\n'.join(list(map(lambda x: f'{str(x)}', find_list))))

    def find_abonent_by_name(self, name, surname):
        find_list = []
        for abonent in self.abonents:
            if abonent.name == name and abonent.surname == surname:
                find_list.append(abonent)
        if not find_list:
            find_list.append("не дал результатов")
        print(f"\n---Поиск по имени {name} {surname}---\n" + '\n'.join(list(map(lambda x: f'{str(x)}', find_list))))


if __name__ == '__main__':
    # Создание телефонной книги
    num_book = NumBook(input('Введите название телефонной книги: '))
    # Создание контакта и добавление в книгу
    num_book.add_abonent(Contact('Евгений', 'Лыков', '+79141234050', telegram='@jhony', email='jhony@mal.com'))
    num_book.add_abonent(Contact('Владимир', 'Симигин', '+71233214667', vkontakte='id123123', email='simigay@ya.com'))
    num_book.add_abonent(Contact('Ирина', 'Ошлакова', '+77777777777', twich='@ashe', chosen=True))
    num_book.add_abonent(Contact('Денис', 'Поляков', '+79991232341', twich='@polyak', chosen=True, email='poly@db.com'))
    num_book.add_abonent(Contact('Анна', 'Буторина', '+71233214666', telegram='@butor', email='butor@ann.com'))
    num_book.add_abonent(Contact('Александр', 'Тихомиров', '+9872345696', twitter='tihi', chosen=True))
    num_book.add_abonent(Contact('Роман', 'Симонов', '+79141234052', twitter='simon'))
    num_book.add_abonent(Contact('Джавид', 'Байрамалиев', '+79141234073'))
    num_book.add_abonent(Contact('Георгий', 'Лабзеев', '+79141234087'))
    # Вывод телефонной книги
    print(num_book)
    # Удаление контакта по номеру телефона
    num_book.del_abonent('+79141234052')
    # Поиск всех избранных номеров
    num_book.find_chosen_abonent()
    # Поиск контакта по имени и фамилии
    num_book.find_abonent_by_name('Анна', 'Буторина')
    # Поиск контакта по номеру телефона
    num_book.find_num_abonent('+71233214667')
    num_book.find_num_abonent('+79141234052')
    # Вывод телефонной книги
    print(num_book)