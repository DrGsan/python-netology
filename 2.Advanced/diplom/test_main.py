import unittest
from .main import *


class MyTestCase(unittest.TestCase):
    def test_get_group_list(self):
        self.assertIsInstance(user.get_group_list(), list)


if __name__ == '__main__':
    unittest.main()
