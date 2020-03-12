import unittest
from .main import *
import psycopg2 as pg


class MyTestCase(unittest.TestCase):
    def test_get_group_list(self):
        self.assertIsInstance(user.get_group_list(), list)


if __name__ == '__main__':
    unittest.main()



import unittest
from app import user, database
import psycopg2 as pg

PATH = '/Users/antongrutsin/Desktop/Python/advanced_python/Diplom_2/config.json'


class TestData(unittest.TestCase):
    def setUp(self):
        self.config = user.take_config(PATH)

    def tearDown(self):
        pass

    def test_init(self):
        with self.assertRaises(TypeError):
            self.user = user.User('544454')
            self.user = user.User()

    def test_have_config(self):
        self.assertTrue(type(self.config) == dict)
        self.assertEqual(len(self.config), 3)


class TestDB(unittest.TestCase):
    def setUp(self):
        self.config = user.take_config(PATH)
        self.db = pg.connect(**self.config['data'])
        self.vk_db = database.Database()

    def test_check_table(self):
        self.assertTrue(self.vk_db.check_tables)


if __name__ == '__main__':
    unittest.main()