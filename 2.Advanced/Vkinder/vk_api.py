class VkApi:

    TOKEN = '5fe54a5c9d3d89e522fe8a36f91eeb739fd986361dc2bf58a3703e003f80270795e873dc99ec17d573ef7'

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
