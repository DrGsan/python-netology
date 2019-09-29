import requests

KEY = 'trnsl.1.1.20190704T091449Z.f4938f047cc91270.52f1cdb7b28ffa3fcb2f6fc096e4457b24279cbe'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

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


task_info = '''Домашнее задание к лекции 3.2 «Работа с библиотекой requests, http-запросы»

Задача №1
Необходимо расширить функцию переводчика так, чтобы она принимала следующие параметры:

Путь к файлу с текстом;
Путь к файлу с результатом;
Язык с которого перевести;
Язык на который перевести (по-умолчанию русский).
У вас есть 3 файла (DE.txt, ES.txt, FR.txt) с новостями на 3 языках: французском, испанском, немецком.
Функция должна взять каждый файл с текстом, перевести его на русский и сохранить результат в новом файле.
Для переводов можно пользоваться API Yandex.Переводчик.'''


# функция для чтения файла и записи его в переменную
def file_to_str(file):
    text_to_translate = ''
    with open(file, 'r') as f:
        for line in f:
            text_to_translate += line
    return text_to_translate


# функция для записи строки в файл
def str_to_file(text, file):
    with open(file, 'w') as f:
        f.write(text)


# функция перевода
def translate_it(text, from_lang, to_lang='ru'):
    params = {
        'key': KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }
    response = requests.get(URL, params=params)
    return ''.join(response.json()['text'])


# функция читает исходный файл, переводит и записыват в указанный файл
def translate_to_file(input_file, output_file, from_lang, to_lang='ru'):
    input_text = file_to_str(input_file)
    translated_text = translate_it(input_text, from_lang, to_lang)
    str_to_file(translated_text, output_file)


print('Приветствую вас в моей версии переводчика который работает на основе API Yandex.Переводчика\n', '-' * 100, '\n')
print(task_info, '\n')
homework('Домашнее задание к лекции 3.2 «Работа с библиотекой requests, http-запросы', 100)
task('1', 100)
translate_to_file('tasks/3.2.http.requests/ES.txt', './ES-RU.txt', 'es')
print('Исходный файл прочитан, переведён и записан в указанный файл.')