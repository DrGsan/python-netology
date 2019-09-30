"""
Домашнее задание к лекции 1.2 «Iterators. Generators. Yield»

1. Написать класс итератора, который по каждой стране из файла [countries.json](https://github.com/mledoze/countries/blob/master/countries.json) ищет страницу из википедии.
Записывает в файл пару: страна – ссылка.
"""

import json
import hashlib


class Iterator:

    def __init__(self, path):
        self.counter = -1
        with open(path, encoding='utf-8') as file:
            self.data = json.load(file)

    def __iter__(self):
        return (self)

    def __next__(self):
        self.counter += 1
        if self.counter < len(self.data):
            country_name = self.data[self.counter]['name']['common']
            pair = country_name + ' - ' + 'https://en.wikipedia.org/wiki/' + country_name
            with open('countries.txt', 'a', encoding='utf-8') as file:
                file.writelines(pair + '\n')
        else:
            raise StopIteration


country_list = Iterator('countries.json')

for item in country_list:
    next(country_list)

"""
2. Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
"""


def md5_generator(path):
    with open(path, 'r', encoding='utf-8') as file:
        while True:
            try:
                yield hashlib.md5(file.readline().splitlines()[0].encode()).hexdigest()
            except IndexError:
                break


for i in md5_generator('countries.txt'):
    print(i)