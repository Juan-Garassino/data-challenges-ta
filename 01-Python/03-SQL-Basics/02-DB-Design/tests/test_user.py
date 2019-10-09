# pylint: disable-all

import unittest
from bs4 import BeautifulSoup

class Users(unittest.TestCase):

#1 in the good folders

#2 should have a survey table
    def test_customers_table_exists(self):
        with open('ecommerce.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
           t.append(table['name'])
        self.assertEqual('customers' in t, True)

#2' should have user_id, foreign_key?
    def test_customers_should_have_the_correct_fields(self):
        with open('ecommerce.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "customers"})
        for row in table[0].find_all('row'):
            self.assertEqual(row.get('name') in ['first_name', 'last_name', 'email', 'city', 'id'], True)

#3 should have a product table
    def test_products_table_exists(self):
        with open('ecommerce.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
           t.append(table['name'])
        self.assertEqual('products' in t, True)

#3' should have survey_id, foreign_key
    def test_products_should_have_the_correct_fields(self):
        with open('ecommerce.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "products"})
        for row in table[0].find_all('row'):
            self.assertEqual(row.get('name') in ['name', 'unit_price', 'id'], True)

#4 should have an orders table
    def test_orders_table_exists(self):
        with open('ecommerce.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
           t.append(table['name'])
        self.assertEqual('orders' in t, True)

#4' should have anwser_id, foreign_key
    def test_orders_should_have_the_correct_fields(self):
        with open('ecommerce.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "orders"})
        for row in table[0].find_all('row'):
            self.assertEqual(row.get('name') in ['date_of_order', 'customer_id', 'id'], True)

#5 should havee a product_orders table
    def test_products_orders_table_exists(self):
        with open('ecommerce.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
           t.append(table['name'])
        self.assertEqual('product_orders' in t, True)

    def test_users_should_have_the_correct_fields(self):
        with open('ecommerce.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "product_orders"})
        for row in table[0].find_all('row'):
            self.assertEqual(row.get('name') in ['product_id', 'order_id', 'quantity', 'id'], True)




