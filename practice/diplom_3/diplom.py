import vk_api
from datetime import datetime
import json
import re

import db


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.vk_session = vk_api.VkApi(self.login, self.password)
        self.user_info = {}
        self.info = "bdate, sex, city, interests, books, movies, music"
        self.users_result = []
        self.sorted_photos = {}
        self.offset = 0
        self.target_uids = []

    def act_session(self):
        try:
            session = self.vk_session.auth()
        except vk_api.AuthError as error_msg:
            print(error_msg)

    def get_info(self):
        vk = self.vk_session.get_api()
        response = vk.users.get(fields=self.info)
        if response:
            for element in response:
                self.user_info = element
        response = vk.friends.get()
        if response:
            self.user_info['friends'] = response['items']
        response = vk.groups.get()
        if response:
            self.user_info['groups'] = response['items']
        if self.user_info.get('sex') == "":
            print('Please input your sex: m - male, f -female, n - not applicable: ')
            person_input = input().strip().lower()
            if person_input == 'm':
                self.user_info['sex'] = 2
            elif person_input == 'f':
                self.user_info['sex'] = 1
            else:
                self.user_info['sex'] = 0

        if self.user_info.get('city') == "":
            print('Please input name of your city: ')
            person_input = input().strip().lower()
            response = vk.database.getCities(country_id=1, q=person_input[:15], count=1)
            self.user_info['city'] = response['items']

        if self.user_info.get('interests') == "":
            print('Please input your interests: ')
            person_input = input()
            self.user_info['interests'] = person_input

        if self.user_info.get('music') == "":
            print('Please input your favourite music: ')
            person_input = input()
            self.user_info['music'] = person_input

        if self.user_info.get('movies') == "":
            print('Please input your favourite movies: ')
            person_input = input()
            self.user_info['movies'] = person_input

        if self.user_info.get('books') == "":
            print('Please input your favourite books: ')
            person_input = input()
            self.user_info['books'] = person_input

        if self.user_info.get('bdate') == "":
            print('Please input your bdate in format XX.XX.XXXX: ')
            person_input = input()
            self.user_info['bdate'] = person_input

        if len(self.user_info['bdate']) == 5:
            print('Please input year of your birth in format XXXX: ')
            person_input = input()
            self.user_info['bdate'] = self.user_info['bdate'] + "." + person_input

    def search_users(self, count=100):
        status = 6
        current_year = datetime.now().year
        birth_year = int(self.user_info['bdate'][-4:])
        user_age = current_year - birth_year
        age_from = user_age - 3
        age_to = age_from + 6
        if self.user_info['sex'] == 2:
            sex = 1
        elif self.user_info['sex'] == 1:
            sex = 2
        else:
            sex = 0
        city = self.user_info['city']['id']

        vk = self.vk_session.get_api()
        response = vk.users.search(offset=self.offset, has_photo=1, status=status,
                                   city=city, sex=sex, age_from=age_from, age_to=age_to,
                                   count=count, fields=self.info)
        self.offset += count
        self.users_result = response['items']

    def user_is_group_member(self):
        vk = self.vk_session.get_api()
        group_dict = {}
        for user in self.users_result:
            self.target_uids.append(user['id'])
            group_dict[user['id']] = 0
        list_id = [self.target_uids[i:i + 500] for i
                   in range(0, len(self.target_uids), 500)]
        for user_ids in list_id:
            for group in self.user_info['groups']:
                group_result = vk.groups.isMember(group_id=group, user_ids=user_ids)
                for member in group_result:
                    if member['member'] == 1:
                        group_dict[member['user_id']] += 1
        for user in self.users_result:
            for member in group_dict:
                if member == user['id']:
                    user['groups_common_count'] = group_dict[member]
                    continue

    def user_is_friend(self):
        vk = self.vk_session.get_api()
        response = vk.friends.getMutual(target_uids=self.target_uids)
        for item in response:
            for user in self.users_result:
                if item['id'] == user['id']:
                    user['friends_common_count'] = item['common_count']
                    continue
        self.target_uids.clear()

    def sort_users(self):
        user_friends_count = len(self.user_info['friends'])
        user_groups_count = len(self.user_info['groups'])

        for user in self.users_result:
            coincidences = 0
            if user.get('friends_common_count'):
                if user['friends_common_count'] >= user_friends_count / 2:
                    coincidences += 30
                elif user['friends_common_count'] >= user_friends_count / 4:
                    coincidences += 25
                elif user['friends_common_count'] >= 1:
                    coincidences += 20
            if user.get('music'):
                for music in user.get('music').split(','):
                    music = re.sub("[\W]", ' ', music)
                    music = music.strip().lower()
                    if music in self.user_info['music'].lower():
                        coincidences += 20
            if user.get('movies'):
                for movie in user.get('movies').split(','):
                    movie = re.sub("[\W]", ' ', movie)
                    movie = movie.strip().lower()
                    if movie in self.user_info['movies'].lower():
                        coincidences += 10
            if user.get('books'):
                for book in user.get('books').split(','):
                    book = re.sub("[\W]", ' ', book)
                    book = book.strip().lower()
                    if book in self.user_info['books'].lower():
                        coincidences += 10
            if user.get('interests'):
                for interest in user.get('interests').split(','):
                    interest = interest.lower()
                    interest = re.sub("[\W]", ' ', interest)
                    interest = interest.strip()
                    for word in interest.split():
                        word = word[:-1]
                        pattern = re.compile(word+"[а-яА-Я]*")
                        result = re.search(pattern, self.user_info['interests'].lower())
                        if result:
                            coincidences += 10
                            break
            if user.get('groups_common_count') >= user_groups_count / 2:
                coincidences += 25
            elif user.get('groups_common_count') >= user_groups_count / 4:
                coincidences += 20
            elif user.get('groups_common_count') >= 1:
                coincidences += 15
            user['coincidences'] = coincidences
        self.users_result = sorted(self.users_result,
                                   key=lambda x: x['coincidences'], reverse=True)

    def load_photo(self):
        users_photo = {}
        vk = self.vk_session.get_api()

        for user in self.users_result[:10]:
            photo_list = []
            try:
                photo_result = vk.photos.get(owner_id=user['id'], album_id='profile',
                                             extended=1)
                if photo_result.get('items'):
                    for photo in photo_result['items']:
                        photo_info = {}
                        photo_info['id'] = photo['id']
                        photo_info['url'] = photo['sizes'][-1]['url']
                        photo_info['likes'] = photo['likes']['count']
                        photo_list.append(photo_info)
            except vk_api.exceptions.ApiError:
                print("The profile is private, therefore we can't get profile photos")
            try:
                photo_result_2 = vk.getUserPhotos(user_id=user['id'], extended=1)
                if photo_result_2.get('items'):
                    for photo in photo_result_2['items']:
                        photo_info = {}
                        photo_info['id'] = photo['id']
                        photo_info['url'] = photo['sizes'][-1]['url']
                        photo_info['likes'] = photo['likes']['count']
                        photo_list.append(photo_info)
            except vk_api.exceptions.ApiError:
                print("Access to user's marked photo is private, therefore "
                      "we can't get photos where user is marked ")
            if photo_list:
                users_photo[user['id']] = photo_list

        for user in users_photo:
            sorted_users_photos = sorted(users_photo[user],
                                         key=lambda x: x['likes'], reverse=True)
            self.sorted_photos[user] = sorted_users_photos
        self.users_result.clear()

    def sort_photo(self):
        for k, v in self.sorted_photos.items():
            account_link = 'https://vk.com/id' + str(k)
            if len(v) >= 3:
                save_info = v[:3]
            else:
                save_info = v
            save_info.append(account_link)
            self.sorted_photos[k] = save_info

    def save_photos_db(self):
        cur, conn, dbname = db.connect_database()
        db.create_table(cur, conn)
        for k, v in self.sorted_photos.items():
            db.add_photos(k, v, cur, conn)
        print(f'Photos have been saved in database {dbname}!')

    def save_photos_json(self, file_name):
        file_name = file_name + ".json"
        with open(file_name, 'w', encoding='utf-8') as save_file:
            json.dump(self.sorted_photos, save_file, ensure_ascii=False, indent=2)
        self.sorted_photos.clear()
        print(f'Photos have been saved in file {file_name}!')

    def find_user_from_db(self, user_id):
        cur, conn, dbname = db.connect_database()
        result = db.get_person_by_id(user_id, cur)
        return result

    def make_user_chosen(self, user_id):
        cur, conn, dbname = db.connect_database()
        db.make_id_chosen(user_id, cur, conn)
        print(f'Person with id {user_id} now is chosen!')

    def put_user_to_blacklist(self, user_id):
        cur, conn, dbname = db.connect_database()
        db.put_id_to_blacklist(user_id, cur, conn)
        print(f'Person with id {user_id} now is in blacklist!')

    def users_from_db(self):
        cur, conn, dbname = db.connect_database()
        result = db.get_all_ids(cur)
        ids = []
        for item in result:
            ids.append(item[0])
        print(ids)

    def is_liked(self, owner_id, item_id):
        vk = self.vk_session.get_api()
        response = vk.likes.isLiked(type='photo', owner_id=owner_id, item_id=item_id)
        return response["liked"]

    def add_like(self, user_id):
        vk = self.vk_session.get_api()
        cur, conn, dbname = db.connect_database()
        photos = db.get_photos(user_id, cur)
        for photo in photos[0][-1]:
            if isinstance(photo, dict):
                current_liked = self.is_liked(user_id, photo['id'])
                if current_liked == 0:
                    print(f"Do you want to add like to photo {photo['url']}? Input Yes or No: ")
                    person_input = input().strip()
                    if person_input.lower() == 'yes':
                        vk.likes.add(type='photo', owner_id=int(user_id), item_id=int(photo['id']))
                        print(f"Photo with id {photo['id']} was liked!")
        print("All photos have been looked!")

    def delete_like(self, user_id):
        vk = self.vk_session.get_api()
        cur, conn, dbname = db.connect_database()
        photos = db.get_photos(user_id, cur)
        for photo in photos[0][-1]:
            if isinstance(photo, dict):
                current_liked = self.is_liked(user_id, photo['id'])
                if current_liked == 1:
                    print(f"Do you want to delete like from photo {photo['url']}?"
                          " Input Yes or No: ")
                    person_input = input().strip()
                    if person_input.lower() == 'yes':
                        vk.likes.delete(type='photo', owner_id=int(user_id), item_id=int(photo['id']))
                        print(f"Like from photo with id {photo['id']} was deleted!")
        print("All photos have been looked")


def run_program():
    print("Program starts!")
    user_login = input('Please input your VK login: ')
    user_password = input('Please input your VK password: ')
    file_name = input("Please input file name where you want to save info: ")
    user = User(user_login, user_password)
    user.act_session()
    user.get_info()
    while True:
        user.search_users()
        user.user_is_group_member()
        user.user_is_friend()
        user.sort_users()
        user.load_photo()
        user.sort_photo()
        user.save_photos_db()
        user.save_photos_json(file_name)
        user_input = input("Do you want to see current ids from Table Person?"
                           " Input Yes or No ")
        if user_input.lower() == 'yes':
            user.users_from_db()
        user_input = input("Do you want to make some additional actions with users? Input Yes or No ")
        if user_input.lower() == 'yes':
            user_id = int(input("Please enter the id of user who you want to make additional actions: "))
            result = user.find_user_from_db(user_id)
            if result:
                print("You can choose next commands:\n"
                      f"a - add like to photos of user {user_id}\n"
                      f"b - put user {user_id} to blacklist\n"
                      f"c - make user {user_id} chosen\n"
                      f"d - delete like from photos of user {user_id}\n"
                      "e - exit\n"
                      )
                user_input = input("Please input command: ")
                if user_input.lower() == 'a':
                    user.add_like(str(user_id))
                elif user_input.lower() == 'd':
                    user.delete_like(str(user_id))
                elif user_input.lower() == 'c':
                    user.make_user_chosen(str(user_id))
                elif user_input.lower() == 'b':
                    user.put_user_to_blacklist(str(user_id))
                else:
                    print('Program ends!')
                    break
        user_input = input("Do you want to restart searching users? Input Yes or No ")
        if user_input.lower() == 'no':
            print('Program ends!')
            break


if __name__ == '__main__':
    run_program()


