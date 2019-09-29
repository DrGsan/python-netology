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


homework('Домашнее задание к лекции 1.3.Decorators.1.3.Decorators «Как сделать красивую шапку»', 100)
task('1', 100)
print('TEST 1')
task('2', 75)
print('TEST 2')