class Config:
    def __init__(self):
        self.token = '9c4b09af23df0e8d2453405ed382ceeb4f55c4108e2e1e17cd49e029b2b07bc90193f856bf72dc14ace8c'


# Запрос токена
def get_access_token(user_id):
    """
    Запрашивает токен упользователяпо его id vk или псевдониму
    :return: ссылка для авторизации пользователя
    """
    oauth_url = 'https://oauth.vk.com/authorize'
    app_id = 7049864
    auth_data = {
        'client_id': app_id,
        'redirect_uti': 'www.ok.ru',
        'display': 'page',
        'scope': 'status, friends, users, photos, offline',
        'response_type': 'token',
        'v': 5.101
    }
    result = print('?'.join((oauth_url, urlencode(auth_data))))
    return result


# Запрашиваем токен
# get_access_token(3178423)

# access_token = 9c4b09af23df0e8d2453405ed382ceeb4f55c4108e2e1e17cd49e029b2b07bc90193f856bf72dc14ace8c
