# pylint: disable-all

import unittest
from bs4 import BeautifulSoup

class Users(unittest.TestCase):
    def test_should_only_have_users_table(self):
        with open('users.xml', 'r') as file:
            data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        self.assertEqual(len(soup.find_all("table", attrs={"name": "users"})), 1)
