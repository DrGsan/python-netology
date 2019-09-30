import json
import requests
from time import sleep
from tqdm import tqdm


# token = input('Введите токен: ')
token = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
version = 5.92


def call_api(method, other_params):
    params = {'access_token': token, 'v': 5.92}
    params.update(other_params)
    url = 'https://api.vk.com/method/'
    response = requests.get(url + method, params).json()
    return response


def get_user_id(nickname_id):
    return call_api('users.get', {'user_ids': nickname_id})['response'][0]['id']


def get_friends_list(user_id):
    return call_api('friends.get', {'user_id': user_id, })['response']['items']


def get_groups_list(user_id):
    return call_api('groups.get', {'user_id': user_id})['response']['items']


def is_member_group(user_id, group_id):
    return call_api('groups.isMember', {'user_id': user_id, 'group_id': group_id})


def get_group_list(user_id):
    group_1 = []
    friends_list = get_friends_list(user_id)
    groups_list = get_groups_list(user_id)
    for friend in friends_list:
        for group in groups_list:
            while True:
                try:
                    test = is_member_group(friend, group)['response']
                    print(test, friend, group)
                except KeyError:
                    sleep(2)
                    continue
                break
    return group_1











def main():
    # nickname_id = input('Введите id или ник-нейм пользователя (eshmargunov или 171691064): ')
    nickname_id = 'eshmargunov'
    user_id = get_user_id(nickname_id)  # Получаем id пользователя



if __name__ == '__main__':
    main()
