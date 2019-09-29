def homework(home_work_name, distance_default):
    distance = int((distance_default - len(home_work_name)) / 2)
    if len(home_work_name) % 2 == 0:
        y = 0
    else:
        y = 1
    x = ('\n' + distance * '-' + home_work_name + (distance + y) * '-')
    print(x)


def task(task_number, distance_default):
    name = 'Задача №'
    distance = int((distance_default - len(name) - len(task_number)) / 2)
    if len(task_number) % 2 == 0:
        y = 0
    else:
        y = 1
    x = (distance * '-' + name + task_number + (distance + y) * '-')
    print('\n' + x + '\n')


homework('Домашнее задание к лекции 2.5 «Менеджер контекста»', 100)
task('1', 100)

from time import sleep
import datetime


class MyManager:

    def __init__(self, file_path):
        self.file_path = file_path
        self.time_start = datetime.datetime.now()

    def __enter__(self):
        self.file = open(self.file_path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.time_stop = datetime.datetime.now()
        print('Время запуска кода:    ', self.time_start)
        print('Время окончания работы:', self.time_stop)
        print('На выполнение кода было потрачено: {0} сек.'.format(self.time_stop - self.time_start))


try:
    with MyManager("tasks/2.4.files/recipes.txt") as file:
        for line in file:
            print(line)
            sleep(0.05)
except EnvironmentError as error:
    print(error)