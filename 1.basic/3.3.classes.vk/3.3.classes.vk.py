import requests
from pprint import pprint
# from urllib.parse import urlencode

app_id = '7049864'
auth_url = 'https://oauth.vk.com/authorize'

auth_data = {
    'client_id': app_id,
    'display': 'page',
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'response_type': 'token',
    'scope': 'friends',
    'v': '5.52'
}

# print('?'.join((auth_url, urlencode(auth_data))))

class User:

    token = '0d223dc79e7cf93fda04955e5dca3b3d5562d5dfe52e316e923f5c57d90a82ee056be3c9eac5bd1d07926'

    def __init__(self, user_id):
        self.user_id = user_id

    def get_params(self):
        return {
            'access_token': self.token,
            'v': '5.52'
        }

    def request(self, method, params):
        response = requests.get(
            'https://api.vk.com/method/' + method,
            params=params
        )
        return response

    def get_status(self):
        params = self.get_params()
        response = self.request(
            'status.get',
            params=params
        )
        return response.json()['response']['text']

    def __and__(self, other):
        params = self.get_params()
        params['source_uid'] = self.user_id
        params['target_uid'] = other.user_id
        response = self.request(
            'friends.getMutual',
            params=params
        )
        return response.json()['response']

    def __str__(self):
        return 'https://vk.com/id{}'.format(self.user_id)

drg = User(3178423)
tih = User(2941614)

print(drg & tih, '\n')

print(drg)