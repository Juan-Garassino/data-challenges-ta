# pylint: disable-all

import unittest
from bs4 import BeautifulSoup

class Users(unittest.TestCase):

    def test_customers_table_exists(self):
        with open('customers.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        self.assertEqual(soup.table['name'],'customers')

    def test_should_only_have_users_table(self):
        with open('customers.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        self.assertEqual(len(soup.find_all("table", attrs={"name": "customers"})), 1)

    def test_should_have_the_correct_fields(self):
        with open('customers.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        for row in soup.find_all('row'):
            self.assertEqual(row.get('name') in ['email', 'first_name', 'id', 'city', 'last_name'], True)


#contexte à modifier

#text-schema-in-users.
