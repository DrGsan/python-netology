def for_fun(number):
    import time
    if number == 1:
        time.sleep(1)
        print('\nХм...')
        time.sleep(1)
        print('Что-то пошло не так...')
        time.sleep(2)
        print('Попробуйте ещё раз\n')
        time.sleep(1)
    elif number == 2:
        time.sleep(2)
        print('\nНе знаю в чём проблема, но пора бы вам уже что-то написать...\n')
        time.sleep(3)
    elif number == 3:
        time.sleep(2)
        print('\nНеожиданно...')
        time.sleep(2)
        print('Рад что у вас получилось:)\n')
        time.sleep(1)

def translate_me():
    i = 0
    while True:
        input_file = input('Введите путь или название исходного файла: ')

        if len(input_file) == 0:
            if i % 2 == 0:
                for_fun(1)
                i += 1
            else:
                for_fun(2)
                i += 1
        else:
            print('Принял-понял')
            if i > 1:
                for_fun(3)
            break
    i = 0
    while True:
        output_file = input('Введите путь или название исходного файла: ')

        if len(input_file) == 0:
            if i % 2 == 0:
                for_fun(1)
                i += 1
            else:
                for_fun(2)
                i += 1
        else:
            print('Принял-понял')
            if i > 1:
                for_fun(3)
            break

translate_me()