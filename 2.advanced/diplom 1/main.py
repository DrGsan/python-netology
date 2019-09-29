import pprint
from vkinder.vkclass import Vkinder

if __name__ == '__main__':
    victim = input('ID жертвы: ')
    age_min = input('Возраст от: ')
    age_max = input('Возраст до: ')
    vkinder = Vkinder(victim)
    finded_users = vkinder.find_users(age_min, age_max)
    sorted_users = vkinder.sort_users(finded_users)
    final_users = vkinder.find_and_sort_photos(sorted_users)
    vkinder.insert_db(final_users)
    print()
    pprint.pprint(final_users)
