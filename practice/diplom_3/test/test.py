import unittest
import os
import json

from diplom import User
import db


def setUpModule():
    print('Set Up Tests')


def tearDownModule():
    print('Tests were ended')


class TestDiplomProgram(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user_login = input('Please input your VK login: ')
        user_password = input('Please input your VK password: ')
        cls.user = User(user_login, user_password)
        cls.session = cls.user.act_session()
        cls.user.get_info()
        cls.user.search_users()
        cls.user.user_is_group_member()
        cls.user.user_is_friend()
        cls.user.sort_users()
        cls.user.load_photo()
        cls.user.sort_photo()

    def test_auth(self):
        self.assertIs(self.session, None)

    def test_load_user_params(self):
        test_params = (self.user.info + ',friends' + ',groups').split(",")
        for param in test_params:
            self.assertIn(param.strip(), self.user.user_info.keys())

    def test_search_users_count(self):
        self.user.search_users()
        self.assertGreater(len(self.user.users_result), 0)

    def test_additional_param_exist(self):
        for user in self.user.users_result:
            self.assertIn('groups_common_count', user.keys())
            self.assertIn('coincidences', user.keys())

    def test_save_sorted_users(self):
        cur, conn, dbname = db.connect_database()
        db.del_all_photos(cur, conn)
        cur.execute('select count(*) from Person')
        result = cur.fetchall()
        self.assertEqual(result[0][0], 0)
        self.assertEqual(len(self.user.sorted_photos), 10)
        for k, v in self.user.sorted_photos.items():
            like_count = 0
            for item in v:
                if isinstance(item, type(dict)):
                    item_like = item.get('likes')
                    if item_like and like_count == 0:
                        self.assertGreater(item_like, like_count)
                    elif item_like:
                        self.assertGreater(like_count, item_like)
                    like_count = item_like
        self.user.save_photos_db()
        cur.execute('select count(*) from Person')
        result = cur.fetchall()
        self.assertEqual(result[0][0], 10)
        current_path = str(os.path.dirname(os.path.abspath(__file__)))
        current_path = current_path[:-4]
        save_directory = os.path.join(current_path, 'fixtures\\test_data')
        self.user.save_photos_json(save_directory)
        save_directory += '.json'
        with open(save_directory, encoding='utf-8') as new_directory:
            test_data = json.load(new_directory)
            self.assertEqual(len(test_data), 10)


if __name__ == '__main__':
    unittest.main()
