class Animals:
    def __init__(self, name):
        self.name = name

    def making_sound(self):
        if self.animal_type == 'алкоголик':
            return ('Я точно не {0} и меня зовут {1}, "{2}"'.
                format(
                self.animal_type,
                self.name,
                self.sound
            ))
        else:
            return ('Я {0} {1}, и я могу говорить "{2} - {2} - {2}! И дай еды!"'.
                format(
                self.animal_type,
                self.name,
                self.sound
            ))


class Dog(Animals):
    sound = 'гав'
    animal_type = 'пёс'


class Cat(Animals):
    sound = 'мяу'
    animal_type = 'кот'


class Alcoholic(Animals):
    sound = 'денег дай ... похмелиться ... hyibliat'
    animal_type = 'алкоголик'


animals = ['Василий Петрович', 'Фёдор', 'Коля', 'Омар Василич']
animals[0] = Dog(animals[0])
animals[1] = Dog(animals[1])
animals[2] = Cat(animals[2])
animals[3] = Alcoholic(animals[3])

print('\n')
print('1ый результат:', Animals.making_sound(animals[0]), '\n')
print('2ой результат:', Animals.making_sound(animals[1]), '\n')
print('3ий результат:', Animals.making_sound(animals[2]), '\n')
print('4ый результат:', Animals.making_sound(animals[3]), '\n')