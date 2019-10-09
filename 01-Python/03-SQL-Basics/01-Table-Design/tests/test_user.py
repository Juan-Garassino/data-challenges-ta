# pylint: disable-all

import unittest
from bs4 import BeautifulSoup

class Users(unittest.TestCase):

    def test_user_table_exists(self):
        with open('users.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        self.assertEqual(soup.table['name'],'users')

    def test_should_only_have_users_table(self):
        with open('users.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        self.assertEqual(len(soup.find_all("table", attrs={"name": "users"})), 1)

    def test_should_have_the_correct_fields(self):
        with open('users.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        for row in soup.find_all('row'):
            self.assertEqual(row.get('name') in ['email', 'first_name', 'id', 'last_name'], True)


#contexte à modifier

#text-schema-in-users.
