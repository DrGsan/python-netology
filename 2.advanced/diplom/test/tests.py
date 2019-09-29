import unittest

from vkinder.vkclass import Vkinder, User


class Test(unittest.TestCase):
    def test_is_instance_of_vkinder(self):
        vkinder = Vkinder('418095195')
        self.assertIsInstance(vkinder, Vkinder)

    def test_find_users(self):
        vkinder = Vkinder('418095195')
        self.assertIsInstance(vkinder.find_users(), list)

    def test_find_users_is_instance_of_user(self):
        vkinder = Vkinder('418095195')
        self.assertIsInstance(vkinder.find_users()[0], User)

    def test_count_weight(self):
        vkinder = Vkinder('418095195')
        self.assertNotEqual(vkinder.find_users(), vkinder.count_weight(vkinder.find_users()))

    def test_sort_users(self):
        vkinder = Vkinder('418095195')
        for_sort = vkinder.find_users()
        self.assertEqual(len(vkinder.sort_users(for_sort)), 10)

    def test_sort_users_is_instance_of_user(self):
        vkinder = Vkinder('418095195')
        for_sort = vkinder.find_users()
        self.assertIsInstance(vkinder.sort_users(for_sort)[0], User)

    def test_find_and_sort_photos(self):
        vkinder = Vkinder('418095195')
        for_photos = vkinder.sort_users(vkinder.find_users(35, 45))
        self.assertEqual(len(vkinder.find_and_sort_photos(for_photos)), 10)

    def test_find_and_sort_photosv_is_list(self):
        vkinder = Vkinder('418095195')
        for_photos = vkinder.sort_users(vkinder.find_users())
        self.assertIsInstance(vkinder.find_and_sort_photos(for_photos), list)


if __name__ == '__main__':
    unittest.main()
