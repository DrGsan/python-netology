import unittest
from diplom.main import User
from mock import patch

info_user = [{'id': , 'first_name': 'Александр', 'last_name': 'Драгой',
              'sex': 2, 'bdate': '29.12.1991', 'city': {'id': 1, 'title': 'Москва'},
              'interests': '', 'music': '', 'books': ''}]


@patch('builtins.input', lambda *args: '22', '23')
class Test(unittest.TestCase):

    # def test_is_instance_of_vkinder(self):
    #     user = User()
    #     self.assertIsInstance(user, User)

    # def test_find_users(self):
    #     user = User()
    #     self.assertIsInstance(user.get_users_info(info_user), tuple)

    # def test_get_raiting_users(self):
    #     user = User()
    #     self.assertIsInstance(user.get_raiting_users(info_user), list)

    # def test_get_users_photo(self):
    #     user = User()
    #     self.assertEqual(len(user.get_users_photo(info_user)), 10)