# Задача №1
#
# Нужно реализовать Польскую нотацию для двух положительных чисел. Реализовать нужно будет следующие операции:
#
# Сложение
# Вычитание
# Умножение
# Деление
# Например, пользователь вводит: + 2 2 Ответ должен быть: 4

task = 'Домашнее задание к лекции 2.3 «Исключения»'
line = '\n' + '-' * (len(task))
print(task + line)


def polish():
    ask = 'Введите через пробел сначала операцию, а потом два положительных числа: '
    operation, number_1, number_2 = input('\n' + ask).split()
    all_operation = ['+', '-', '*', '/']
    number_1 = int(number_1)
    number_2 = int(number_2)
    assert number_1 >= 0 and number_2 >= 0, 'Отрицательное число'
    assert operation in all_operation, 'Вы не ввели операцию! (+, -, *, /)'  # подпись к задаче №2
    if operation == '+':
        answer = number_1 + number_2
    elif operation == '-':
        answer = number_1 - number_2
    elif operation == '*':
        answer = number_1 * number_2
    elif operation == '/':
        answer = number_1 / number_2
    return answer


# Задача №2
#
# С помощью выражения assert проверять, что первая операция в списке доступных операций (+, -, *, /). С помощью
# конструкций try/expcept ловить ошибки и выводить предупреждения Типы ошибок:
#
# Деление на 0
# Деление строк
# Передано необходимое количество аргументов
# и тд.


try:
    print(polish())
except ZeroDivisionError:
    print('Вы пытались разделить на ноль')
except AssertionError:
    print('Assert: отрицательное число или не соответствующий знак')
except ValueError:
    print('Не корректное значение')
else:
    print('Передано необходимое количество аргументов')

# Задача №3
#
# Расширить домашние задание из лекции 1.4 «Функции — использование встроенных и создание собственных» новой функцией,
# выводящей имена всех владельцев документов. С помощью исключения KeyError проверяйте, если поле "name" у документа.

task_3 = 'Задача №3'
ask = 'Введите вашу команду("n" - для поика владельца документа,'
line = '\n' + '-' * (len(task_3))
print('\n' + task_3 + line)

documents = [
    {"type": "card", "number": "007"},
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]


def names():
    for search_names in documents:
        try:
            print('{} "{}" "{}"'.format(search_names['type'],search_names['number'] ,search_names['name']))
        except KeyError:
            print('В документах {} номер "{}" нет имени'.format(search_names['type'], search_names['number']))

names()