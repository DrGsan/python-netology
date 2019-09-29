from collections import Counter
import time
import base64
import requests
from db.mysql import MySQLdb


class User:

    def __init__(self, id, info, weight=0):

        self.id = id
        self.info = info
        self.weight = weight


class Vkinder(MySQLdb):
    TOKEN = ''
    VERSION = '5.101'

    def __init__(self, main_user_id):
        super().__init__()
        with open('/home/dukov/PycharmProjects/ADPY/token') as token:
            coded_token = token.readline()
            self.TOKEN = base64.b64decode(coded_token).decode('utf-8')
        response_main_user = requests.get('https://api.vk.com/method/users.get', {
            'access_token': self.TOKEN,
            'user_ids': main_user_id,
            'fields': 'bdate, sex, interests, music, books, city',
            'v': self.VERSION
        })

        main_user_info = response_main_user.json()['response'][0]
        self.main_user = User(main_user_info.pop('id'), main_user_info)

    def find_users(self, min_age, max_age):
        sex_for_find = 0
        if self.main_user.info['sex'] == 1:
            sex_for_find = 2
        elif self.main_user.info['sex'] == 2:
            sex_for_find = 1

        params = {
            'access_token': self.TOKEN,
            'sex': sex_for_find,
            'age_from': min_age,
            'age_to': max_age,
            'has_photo': 1,
            'fields': 'interests, music, books, sex, city',
            'count': 1000,
            'city': self.main_user.info['city']['id'],
            'v': self.VERSION
        }

        response_find_users = requests.get('https://api.vk.com/method/users.search', params)
        users = []
        for user in response_find_users.json()['response']['items']:
            users.append(User(user.pop('id'), user))
        return users

    def count_weight(self, users, field='interests', multiplier=1):
        if self.main_user.info[field] != '':
            splitted_main_user_interests = self.main_user.info[field].split(',')
            for user in users:
                counter = 0
                if field in user.info:
                    splitted_interests = user.info[field].split(',')
                    word_counter = Counter(splitted_interests)
                    for interest in splitted_main_user_interests:
                        counter += word_counter[interest]
                user.weight += counter * multiplier
        return users

    def sort_users(self, finded_users):
        self.count_weight(finded_users, 'interests', 3)
        self.count_weight(finded_users, 'music', 2)
        self.count_weight(finded_users, 'books', 1)

        finded_users.sort(key=lambda user: user.weight, reverse=True)
        old_users = self.select_from_db([self.main_user.id])
        try:
            old_users[0]
            for old_user in old_users[0]['finded_users']:
                for user in finded_users:
                    if user.id == old_user or user.info['is_closed']:
                        finded_users.remove(user)
        except IndexError:
            for user in finded_users:
                if user.info['is_closed']:
                    finded_users.remove(user)

        return finded_users[0:10]

    def insert_db(self, final):
        for user in final:
            for photo in user.get('photos'):
                # print(photo.items())
                self.insert_to_db([user['id'], photo['id'], photo['likes']])

    def find_and_sort_photos(self, finded_users):
        sorted_users = []
        for user in finded_users:
            params = {
                'access_token': self.TOKEN,
                'owner_id': user.id,
                'extended': 1,
                'album_id': 'profile',
                'v': self.VERSION
            }
            response_get_photos = requests.get('https://api.vk.com/method/photos.get', params)
            unsorted_photos = {
                'id': user.id,
                'photos': response_get_photos.json()['response']['items']
            }
            unsorted_ids_of_photos = []
            for photo in unsorted_photos['photos']:
                unsorted_ids_of_photos.append({
                    'id': photo['id'],
                    'likes': photo['likes']['count']
                })
            unsorted_ids_of_photos.sort(key=lambda dict: dict['likes'], reverse=True)
            unsorted_ids_of_photos = unsorted_ids_of_photos[0:3]
            sorted_users.append({
                'id': unsorted_photos['id'],
                'photos': unsorted_ids_of_photos
            })
            time.sleep(0.33)
            print('.', end='', flush=True)
        return sorted_users
