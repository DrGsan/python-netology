import unittest

from main import Vkinder
from mock import patch

info_user = [{'id': '3178423', 'first_name': 'Александр', 'last_name': 'Драгой',
              'sex': 2, 'bdate': '29.12.1991', 'city': {'id': 1, 'title': 'Москва'},
              'interests': '', 'music': '', 'books': ''}]


@patch('builtins.input', lambda *args: '18', '30')
class Test(unittest.TestCase):

    def test_is_instance_of_vkinder(self):
        vkinder = Vkinder()
        self.assertIsInstance(vkinder, Vkinder)

    def test_find_users(self):
        vkinder = Vkinder()
        self.assertIsInstance(vkinder.get_users_info(info_user), tuple)

    def test_get_raiting_users(self):
        vkinder = Vkinder()
        self.assertIsInstance(vkinder.get_raiting_users(info_user), list)

    def test_get_users_photo(self):
        vkinder = Vkinder()
        self.assertEqual(len(vkinder.get_users_photo(info_user)), 10)