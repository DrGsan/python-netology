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
        y = 1
    else:
        y = 0
    x = (distance * '-' + name + task_number + (distance + y) * '-')
    print('\n' + x + '\n')


def read_cook_book():
    recipts = {}
    file = open("tasks/2.4.files/recipes.txt", encoding="UTF8")
    for line in file:
        name = line.strip().lower()
        if name != "":
            count = int(file.readline().strip())
            ingridients = []
            for i in range(count):
                ingridients_list = file.readline().strip().split(' | ')
                ingridient = {'ingridient_name': ingridients_list[0],
                              'quantity': int(ingridients_list[1]),
                              'measure': ingridients_list[2]}
                ingridients.append(ingridient)
            recipts[name] = ingridients
    return recipts


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'],
                                shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    cook_book = read_cook_book()
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)


homework('Домашнее задание к лекции 2.4 «Открытие и чтение файла, запись в файл»', 100)
task('1', 100)
create_shop_list()