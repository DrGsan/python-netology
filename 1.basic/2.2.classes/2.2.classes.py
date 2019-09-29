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


homework('Домашнее задание к лекции 2.2 «Классы и их применение в Python', 43)
task('1, 2, 3', 43)


from abc import ABC, abstractmethod


class Animals(ABC):

    def __init__(self, name, sex, weight):
        self.name = name
        self.sex = sex
        self.weight = weight

        if self.sex == 'муж' and self.__class__.__name__ != 'Sheep':
            self.harvest_status = 'нечего собрать'

        if self.sex == 'муж':
            self.hunger_status = 'голоден'
            if self.__class__.__name__ == 'Sheep':
                self.type_nominative_case = 'баран'
            elif self.__class__.__name__ == 'Cow':
                self.type_nominative_case = 'бык'
            elif self.__class__.__name__ == 'Goat':
                self.type_nominative_case = 'козел'
            elif self.__class__.__name__ == 'Chicken':
                self.type_nominative_case = 'петух'
            elif self.__class__.__name__ == 'Goose':
                self.type_nominative_case = 'гусь'
            elif self.__class__.__name__ == 'Duck':
                self.type_nominative_case = 'утка'
        else:
            self.hunger_status = 'голодна'

    def making_sound(self):
        print('Умеет говорить: {}'.format(self.sound))

    def how_heavy(self):
        print('Вес: {} кг'.format(self.weight))

    def if_hungry(self):
        if self.hunger_status == 'голодна' or self.hunger_status == 'голоден':
            print('нужно покормить (введите команду F)')
            return True
        else:
            print(self.hunger_status)
            return False

    def if_have_harvest_stuff(self):
        if self.harvest_status != 'нечего собрать':
            print(self.harvest_status, '(введите команду H)')
            return True
        else:
            print(self.harvest_status)
            return False

    def harvest(self):
        if self.harvest_status != 'нечего собрать':
            print()
            print(' → Вы собрали {} у {} по имени {}'.format(self.harvest_stuff, self.type_genitive_case, self.name))
            self.harvest_status = 'нечего собрать'
        else:
            print()
            print(' → {} у {} по имени {}! Проверьте, может у других что-нибудь завалялось.'.format(self.harvest_status,
                                                                                                    self.type_genitive_case,
                                                                                                    self.name))
        print()
        quit = input('Нажмите Enter чтобы продолжить')

    def feed(self):
        if self.hunger_status == 'голоден' or self.hunger_status == 'голодна':
            if self.sex == 'муж':
                self.hunger_status = 'Сыт'
            else:
                self.hunger_status = 'Сыта'
            print()
            print(' → Вы дали {} {} по имени {}'.format(self.eating_food, self.type_dative_case, self.name))
            print(' → {} говорит Вам "{}" (что означает "большое спасибо")'.format(self.name, self.sound))
        else:
            print()
            print(' → {} по имени {} уже не хочет кушать! Проверьте, сыты ли жругие животные.'.format(
                self.type_nominative_case.capitalize(), self.name))
        print()
        quit = input('Нажмите Enter чтобы продолжить')


class Artiodactyls(Animals):
    harvest_status = 'нужно подоить'
    eating_food = 'траву'
    harvest_stuff = 'молоко'
    type_nominative_case = 'животное'
    type_genitive_case = 'животного'
    type_dative_case = 'животному'


class Cow(Artiodactyls):
    sound = 'Муу'
    type_nominative_case = 'корова'


class Goat(Artiodactyls):
    sound = 'Беее'
    type_nominative_case = 'коза'


class Sheep(Artiodactyls):
    harvest_stuff = 'шерсть'
    sound = 'Меее'
    harvest_status = 'нужно постричь'
    type_nominative_case = 'овца'


class Birds(Animals):
    harvest_status = 'нужно собрать яйца'
    eating_food = 'зерно'
    harvest_stuff = 'яйца'
    type_nominative_case = 'птица'
    type_genitive_case = 'птицы'
    type_dative_case = 'птице'


class Goose(Birds):
    sound = 'Га-га-га'
    type_nominative_case = 'гусыня'


class Chicken(Birds):
    sound = 'Ко-ко-ко'
    type_nominative_case = 'курица'


class Duck(Birds):
    sound = 'Кря-кря'
    type_nominative_case = 'утка'


# ---------- ФУНКЦИИ ----------------


def start_program():
    print('Добро пожаловать на ферму Дядюшки Джо!')
    print('Сейчас на ферме {} животных и птиц!'.format(len(animals)))
    stop_program = False;

    while stop_program != True:
        print()
        print("------------- СПИСОК ЖИВОТНЫХ -------------")
        list_animals()
        print("-------------------------------------------")

        print("Вы можете сделать следующие действия:")
        print("- Подойти поближе к животному (введите номер животного из списка) -")
        print("- Узнать кто на ферме самый тяжелый и общий вес всех животных (введите команду W) -")
        print("- Уехать домой (введите команду Q) -")
        print("-------------------------------------------")

        what_to_do = input("Что бы вы хотели сделать?")
        if what_to_do == "Q" or what_to_do == "q":
            print("-------------------------------------------")
            print("Счастливого пути!")
            print("--> Программа завершена <--")
            stop_program = True
        elif what_to_do.isdigit() == True:
            if int(what_to_do) > len(animals):
                print('Wrong comm')
            else:
                go_to_animal(what_to_do)
        elif what_to_do.lower() == "w":
            most_heavy_animal()
        else:
            print('Введена неверная команда! Попробуйте еще раз.')


def list_animals():
    i = 0
    for animal in animals:
        i += 1
        animal.id = i
        print('{}) {} {} ({}, {})'.format(animal.id, animal.type_nominative_case.capitalize(), animal.name,
                                          animal.hunger_status, animal.harvest_status))


def go_to_animal(animal_id):
    def message_what_to_do(hungry, have_harvest_stuff):
        if hungry or have_harvest_stuff:
            return 'Введите команду или нажмите Enter чтобы вернуться к списку животных: '
        else:
            return 'Нажмите Enter чтобы вернуться к списку животных'

    for animal in animals:
        if animal.id == int(animal_id):
            go_away = False
            while go_away != True:
                print()
                print('~~~~~~ {} {} ~~~~~~'.format(animal.type_nominative_case.upper(), animal.name.upper()))
                animal.making_sound()
                animal.how_heavy()
                hungry = animal.if_hungry()
                have_harvest_stuff = animal.if_have_harvest_stuff()
                print('------------------------------')

                what_to_do = input(message_what_to_do(hungry, have_harvest_stuff))
                if what_to_do.lower() == 'f':
                    animal.feed()
                elif what_to_do.lower() == 'h':
                    animal.harvest()
                elif what_to_do == '':
                    go_away = True
                else:
                    print('Введена неверная команда! Попробуйте еще раз.')


def most_heavy_animal():
    biggest_wheight = 0
    most_heavy_animal = ''
    all_ainmals_weight = 0

    for animal in animals:
        all_ainmals_weight += animal.weight
        if animal.weight > biggest_wheight:
            biggest_wheight = animal.weight
            most_heavy_animal = '{} {}'.format(animal.type_nominative_case.capitalize(), animal.name)
            sound = animal.sound
    print()
    print(' → Вы слышите протяжнное {}... '.format(sound))
    print(' → Вы правильно поняли! {} говорит что имеет самый большой вес на всей ферме - аж {} кг!'.format(
        most_heavy_animal, biggest_wheight))
    print(' → А общий вес всех животных на ферме составляет {} кг!'.format(all_ainmals_weight))
    print()
    print("-------------------------------------------")
    quit = input('Нажмите Enter чтобы вернуться к списку животных')


# ---------- ДАННЫЕ И ЗАПУСК ПРОГРАММЫ ----------------

animals = ['Серый', 'Белый', 'Манька', 'Барашек', 'Кудрявый', 'Ко-Ко', 'Кукареку', 'Рога', 'Копыта', 'Кряква']
animals[0] = Goose(animals[0], 'муж', 10)
animals[1] = Goose(animals[1], 'муж', 8)
animals[2] = Cow(animals[2], 'жен', 600)
animals[3] = Sheep(animals[3], 'муж', 70)
animals[4] = Sheep(animals[4], 'муж', 65)
animals[5] = Chicken(animals[5], 'жен', 3)
animals[6] = Chicken(animals[6], 'муж', 4)
animals[7] = Goat(animals[7], 'жен', 50)
animals[8] = Goat(animals[8], 'муж', 65)
animals[9] = Duck(animals[9], 'жен', 3)

start_program()