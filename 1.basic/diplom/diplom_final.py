import json
import requests
from time import sleep
from tqdm import tqdm


token = input('Введите токен: ')


def default_params():
    return {
        'access_token': token,
        'v': 5.92
    }


def get_user_id(nickname_id):
    params = default_params()
    params['user_ids'] = nickname_id
    response_for_id = requests.get('https://api.vk.com/method/users.get', params)
    result_for_id = response_for_id.json()['response'][0]['id']
    return result_for_id


def get_group_list(ids):
    id = get_user_id(ids)
    params = default_params()
    params['user_id'] = id
    response_group_list = requests.get('https://api.vk.com/method/groups.get', params)
    result_groups_list = response_group_list.json()['response']['items']
    return result_groups_list


def get_user_friends_list(ids):
    id = get_user_id(ids)
    params = default_params()
    params['user_id'] = id
    response_friends_list = requests.get('https://api.vk.com/method/friends.get', params)
    result_friends_list = response_friends_list.json()['response']['items']
    return result_friends_list


def split_friends(ids):
    friends_list = get_user_friends_list(ids)
    friends_in_500 = list()
    while len(friends_list) > 500:
        piece_500 = friends_list[:500]
        friends_in_500.append(piece_500)
        friends_list = friends_list[500:]
    friends_in_500.append(friends_list)
    return friends_in_500


def check_for_friends_in_groups(ids):
    group_list = get_group_list(ids)
    friend_list_500 = split_friends(ids)
    result_list_1 = set()
    result_list_0 = set()
    result_list = set()
    count = int()
    group_list = tqdm(group_list)
    for group in group_list:
        for friends_500 in friend_list_500:
            while True:
                params = default_params()
                params['group_id'] = group
                params['user_ids'] = ', '.join(str(fr) for fr in friends_500)
                try:
                    response_friend_in_group = requests.get('https://api.vk.com/method/groups.isMember', params)
                    result = response_friend_in_group.json()['response']
                    for result_dict in result:
                        group_list.set_description('Друг ids{} в группе ids{}: {}. Осталось проверить {} друзей'.format(
                            result_dict['user_id'],
                            group,
                            result_dict['member'],
                            len(friends_500) * len(group_list) - count))
                        if result_dict['member'] == 1:
                            result_list_1.add(group)
                            count += 1
                        elif result_dict['member'] == 0:
                            result_list_0.add(group)
                            count += 1
                except requests.exceptions.ReadTimeout:
                    continue
                except KeyError:
                    sleep(1)
                    continue
                break
        result_list = result_list_0.difference(result_list_1)
    print('-' * 100)
    return create_json_file(result_list)


def create_json_file(set_income):
    json_list = list()
    params = default_params()
    params['fields'] = 'members_count'
    for group in set_income:
        while True:
            params['group_id'] = group
            print('Запрос информации по группе № {}'.format(group))
            try:
                response_for_group_info = requests.get('https://api.vk.com/method/groups.getById', params)
                result_for_group_info = response_for_group_info.json()['response'][0]
                group_dict = dict()
                group_dict['name'] = result_for_group_info['name']
                group_dict['gid'] = result_for_group_info['id']
                group_dict['members_count'] = result_for_group_info['members_count']
                json_list.append(group_dict)
            except requests.exceptions.ReadTimeout:
                continue
            except KeyError:
                sleep(1)
                continue
            break
    with open('groups.json', 'w', encoding='utf-8') as json_text:
        data = json_list
        json.dump(data, json_text, indent=2, ensure_ascii=False)
        some_text = json.dumps(data, indent=2, ensure_ascii=False)
    print('-' * 100)
    print('Запрос выполнен успешно! Результат записан в файл "groups.json"')
    print('-' * 100)
    return some_text


if __name__ == '__main__':
    nickname_id = input('Введите id или ник-нейм пользователя (eshmargunov или 171691064): ')
    print(check_for_friends_in_groups(nickname_id))