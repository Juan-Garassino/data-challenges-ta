# pylint: disable-all
import unittest
from join_queries import detailed_orders
import sqlite3

conn = sqlite3.connect('db/ecommerce.db')
db = conn.cursor()

# 1. check the type of the results
# 2. Check the first result
# 3. Check the last result
class TestDetailOrders(unittest.TestCase):
    def check_type_results(self):
        results = detailed_orders(db)
        results = results.fetchall()
        self.assertEqual(1, 20)

    def check_type_results(self):
        results = detailed_orders(db)
        results = results.fetchall()
        self.assertEqual(1, 20)

    def check_type_results(self):
        results = detailed_orders(db)
        results = results.fetchall()
        self.assertEqual(1, 20)
